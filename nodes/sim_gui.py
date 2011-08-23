#!/usr/bin/python
import map_rep
from Tkinter import Tk, Canvas, Button

class gui:

    def __init__(self, sonar):
        self.tk = Tk()
        self.canvas = Canvas(self.tk, height=800, width=800)
        self.canvas.pack()
        self.next = Button(self.tk, text='next', command=self.step)
        self.next.pack()
        self.rb = Button(self.tk, text='run', command=self.run)
        self.rb.pack()
        self.sonar = sonar
        self.draw_map()
        self.draw_move_points()
        self.delete_old = True
        #self.tk.after(20,self.redraw)

        self.tk.mainloop()

    def run(self):
        self.next.config(state='disabled')
        self.rb.config(state='disabled')
        self.manual = False
        self.tk.after(50, self.redraw)

    def step(self):
        self.manual = True
        self.redraw()
        
    def redraw(self):
        check = self.sonar.sim_step()
        if self.delete_old:
            self.canvas.delete('scan')
            self.canvas.delete('intersect')
            self.canvas.delete('particle')
            self.canvas.delete('mvln')
            
        self.draw_sonar_data()
        self.draw_particle_data()
        if check is not -1 and self.manual is False:
            self.tk.after(50, self.redraw)
        
    def draw_sonar_data(self):
        #print 'data'
        #for line in self.sonar.scan_lines:
            #draw_line(self.canvas, line, tag='scan')
            
        #for point in self.sonar.intersection_points:
            #draw_point(self.canvas, point, tag='intersect')
        draw_point(self.canvas, self.sonar.loc, tag='sonar', colour='red')

    def draw_particle_data(self):
        particles = self.sonar.particles.list()
        for particle in particles:
            draw_point(self.canvas, particle.loc, weight=particle.wt, tag='particle')
            if particle.move_line:
                draw_line(self.canvas, particle.move_line, tag='mvln')
            #for line in particle.scan:
             #   draw_line(self.canvas, line, tag='scan')
            #for intersect in particle.int:
                #draw_point(self.canvas, intersect, tag='intersect')
        
    def draw_map(self):
        #print 'map'
        for line in self.sonar.map.lines:
            draw_line(self.canvas, line, tag='map')

    def draw_move_points(self):
        for point in self.sonar.get_move_list():
            draw_point(self.canvas, point[0], tag='mvpt')
        #for line in self.sonar.move_list.lines:
            #draw_line(self.canvas, line)

def draw_line(canvas, line, tag=''):
    c = line.coords
    canvas.create_line(c[0][0], c[0][1], c[1][0], c[1][1], tags=tag)

def draw_point(canvas, point, weight=0, colour='black', tag=''):
    pt = point
    if not point: return
    if weight == 0:
        canvas.create_oval(pt.x - 1, pt.y - 1, pt.x + 1, pt.y + 1, tags=tag, outline=colour)
    else:
        canvas.create_oval(pt.x - weight*5, pt.y - weight*5, pt.x + weight*5, pt.y + weight*5, tags=tag, outline=colour)
def draw_circle_from_centre(canvas, radius, centre):
    # probably the wrong way around, technically, but since it's a
    # circle it makes no difference really.
    tl = Point(centre.x - radius, centre.y + radius)
    br = Point(centre.x + radius, centre.y - radius)
    canvas.create_oval(tl.x, tl.y, br.x, br.y)
