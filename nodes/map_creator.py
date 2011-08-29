#!usr/bin/python
import os
import sys, s_math
from Tkinter import *
import tkFileDialog
import tkMessageBox
from math import degrees, sqrt, atan2


def init():
    global point_list
    global mv_flag
    global mv_points
    global rotations
    global m
    m = s_math.SonarMath()
    point_list = []
    mv_points = []
    rotations = []
    mv_flag = 0
    create_canvas()
   
def create_canvas():
    ms = Tk()
    global canvas

    sv = Button(ms, text='Save map', command=save_map_to_file)
    sv.pack()
    sm = Button(ms, text='Save move', command=save_move_to_file)
    sm.pack()
    mv = Button(ms, text='Movement list', command=create_move_list)
    mv.pack()
    canvas = Canvas(ms, width=800, height=800)
    canvas.pack()
    canvas.bind("<Button-1>", m1down)
    canvas.mainloop()

def create_move_list():
    global mv_flag
    if mv_flag == 0:
        tkMessageBox.showwarning("Info", "Click on the map to define a set of points to travel along. The first click indicates the point at which to put the sonar, and the second the rotation of the sonar.")
    mv_flag = 1 if mv_flag == 0 else 0
    
def save_map_to_file():
    ### You will need to manually add a scaling factor to the first line of the map, with no trailing spaces. The second line of the map should contain all of the lines that make up the map
    f = tkFileDialog.asksaveasfile(defaultextension='.map')
    for i, val in enumerate(point_list):
        if i != len(point_list) - 1:
            f.write(str(val) + ' ')
        else:
            f.write(str(val))
    f.close()

def save_move_to_file():
    if not mv_points:
        tkMessageBox.showwarning("Error", "You haven\'t made a move sequence.")
        return
    f = tkFileDialog.asksaveasfile(defaultextension='.mv')
    for val in range(len(mv_points)/2):
        pt = mv_points[val*2:val*2 + 2]
        rot = rotations[val*2:val*2 + 2]
        a = m.angle_at_pt2(rot, pt)
        f.write('%s %s %s '%(str(pt[0]), str(pt[1]), str(a)))
    f.close()

def m1down(event):
    # Might be nice to extend this to make it so that if you click
    # close to another point (say within 5 units), then the point
    # added is the same as the one that is close.
    global mv_flag
    if mv_flag: # Creates movement vectors and rotations
        if len(mv_points) != len(rotations):
            rotations.extend([event.x, event.y])
            if len(mv_points) != 0:
                draw_move_point()
        else:
            mv_points.extend([event.x, event.y])
    else: # Creates lines for the map
        point_list.extend([event.x, event.y])
        if len(point_list) % 4 == 0:
            canvas.create_line(*point_list[-4:])
    
def draw_move_point():
    pts = mv_points[-2:] + rotations[-2:]
    canvas.create_oval(pts[0] - 3, pts[1] + 3, pts[0] + 3, pts[1] - 3)
    canvas.create_line(*pts)

if __name__ == '__main__':
    init()
