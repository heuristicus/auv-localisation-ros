#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import map_rep, rospy, move_list
from loc_sonar.msg import particle_data, proc_sonar
from std_msgs.msg import String
from Tkinter import Tk, Canvas, Button

class gui:

    def __init__(self):
        self.get_params()
        self.tk = Tk()
        self.canvas = Canvas(self.tk, height=800, width=800)
        self.canvas.pack()
        #self.next = Button(self.tk, text='next', command=self.step)
        #self.next.pack()
        #self.rb = Button(self.tk, text='run', command=self.run)
        #self.rb.pack()
        #self.sonar = sonar
        #self.localiser = localiser
        self.draw_map()
        self.draw_move_points()
        self.delete_old = True
        self.create_subscribers()
        #self.tk.after(20,self.redraw)

        self.tk.mainloop()

    def create_subscribers(self):
        self.particlesub = rospy.Subscriber('particle', particle_data, self.particle)
        self.sonarsub = rospy.Subscriber('sonar_pre', proc_sonar, self.sonar)
        self.updatesub = rospy.Subscriber('particle_update', String, self.delete)
        rospy.init_node('sim_gui')

    def delete(self, msg):
        if self.delete_old:
            self.canvas.delete('mvln')
            self.canvas.delete('particle')

    def get_params(self):
        self.move_file = rospy.get_param('move_list')
        self.map_file = rospy.get_param('loc_map')
        self.map = map_rep.MapRep(fname=self.map_file) # Map to use the sonar in
        self.scale = self.map.scale
        self.move_list = move_list.MoveList(fname=self.move_file)

    def sonar(self, data):
        #self.canvas.delete('sonar')
        draw_point(self.canvas, data.actual, tag='sonar', colour='red')
        #for ln in data.scan:
         #   draw_line(self.canvas, ln, tag='scan')

    def particle(self, data):
        #self.canvas.delete('particle')
        if data.flag == 1:
            draw_point(self.canvas, data.loc, weight=data.weight, colour='red', tag='mean')
        else:
            draw_point(self.canvas, data.loc, weight=data.weight, colour='black', tag='particle')
        #for ln in data.scan:
         #   draw_line(self.canvas, ln, tag='scan')
        draw_line(self.canvas, data.moveline, tag='mvln')
        #self.canvas.create_text(data.loc.x, data.loc.y, text='%d'%(data.weight))

    def draw_map(self):
        #print 'map'
        for line in self.map.lines:
            draw_linestr(self.canvas, line, tag='map')

    def draw_move_points(self):
        for point in self.move_list.get_list():
            draw_point(self.canvas, point[0], tag='mvpt')
        
def draw_linestr(canvas, line, tag=''):
    c = line.coords
    canvas.create_line(c[0][0], c[0][1], c[1][0], c[1][1], tags=tag)

def draw_line(canvas, line, tag=''):
    canvas.create_line(line.start.x, line.start.y, line.end.x, line.end.y, tags=tag)

def draw_point(canvas, point, weight=0, colour='black', tag=''):
    pt = point
    print weight*10
    if not point: return
    fl = 'red' if tag == 'mean' else None        
    if weight == 0:
        canvas.create_oval(pt.x - 1, pt.y - 1, pt.x + 1, pt.y + 1, tags=tag, outline=colour, fill=fl)
    else:
        canvas.create_oval(pt.x - weight*10, pt.y - weight*10, pt.x + weight*10, pt.y + weight*10, tags=tag, outline=colour, fill=fl)

def draw_circle_from_centre(canvas, radius, centre):
    # probably the wrong way around, technically, but since it's a
    # circle it makes no difference really.
    tl = Point(centre.x - radius, centre.y + radius)
    br = Point(centre.x + radius, centre.y - radius)
    canvas.create_oval(tl.x, tl.y, br.x, br.y)

if __name__ == '__main__':
    gui()
