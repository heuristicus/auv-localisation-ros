#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
from loc_sonar.msg import sonar_return, point_range
from std_msgs.msg import String
from Tkinter import Tk, Canvas
import rospy
import s_math


class gui:
    
    def __init__(self):
        self.tk = Tk()
        self.math = s_math.SonarMath()
        self.canvas = Canvas(self.tk, height=700, width=800)
        self.canvas.pack()
        self.sub = rospy.Subscriber('point_data', point_range, self.update)
        rospy.init_node('gui')
        self.count = 0
        self.tk.mainloop()
        
    def update(self, rdata):
        centre = self.math.make_point(rdata.y ,rdata.x)
        pt = self.math.point_at_angle(centre, rdata.angle, rdata.range*100)
        draw_point(self.canvas, pt)
        self.count += 1
        if self.count is 180:
            self.canvas.create_text((rdata.y, rdata.x), text='%d, %d'%(rdata.x, rdata.y), fill="red")
            self.count = 0
        

def draw_line(canvas, line, tag=''):
    c = line.coords
    canvas.create_line(c[0][0], c[0][1], c[1][0], c[1][1], tags=tag)

def draw_point(canvas, point, weight=0, colour='black', tag='', invert=False):
    pt = point
    if not invert:
        x = pt.x
        y = pt.y
    else:
        x = pt.y
        y = pt.x

    if not point: return
    if weight == 0:
        canvas.create_oval(x - 1, y - 1, x + 1, y + 1, tags=tag, outline=colour)
    else:
        canvas.create_oval(x - weight*5, y - weight*5, x + weight*5, y + weight*5, tags=tag, outline=colour)

if __name__ == '__main__':
    gui()
