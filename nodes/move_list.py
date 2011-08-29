#!/usr/bin/python
from shapely.geometry import Point
import sys, s_math

class MoveList:
    
    def __init__(self, movelist=[], fname=''):
        self.movelist = movelist
        self.pointer = -1
        self.math = s_math.SonarMath()
        if fname:
            self.read_from_file(fname)

    def __repr__(self):
        s = ''
        for point in self.movelist:
            s += 'Point: %s \nRotation: %s\n'%(str(point[0].coords[0]), str(point[1]))
        return s[:-2] # crude way to get rid of last newline

    def read_from_file(self, filename):
        tmp = []
        ml = []
        tmp = open(filename, 'r').read().split(' ')
        print tmp
        tmp = map(float,tmp[:-1])
        for i in range(len(tmp)/3):
            ml.append([Point(tmp[i*3], tmp[i*3+1]), tmp[i*3+2]])
        self.movelist =  ml
        #self.avg_move_length()

    def get_next(self):
        try:
            n = self.movelist[self.pointer + 1]
            return n
        except IndexError:
            return -1
            
    def next(self):
        self.pointer += 1
        return self.current()

    def previous(self):
        self.pointer -= 1
        return self.current()
    
    def get_previous(self):
        return self.movelist[self.pointer - 1]
    
    def first(self):
        return self.movelist[0]

    def current(self):
        try:
            if self.pointer < 0:
                raise IndexError
            return self.movelist[self.pointer]
        except IndexError:
            print 'Either the start or end of the list has been reached.'
            return -1
            
    def get_list(self):
        return self.movelist

    def reset(self):
        self.pointer = -1
    
    def avg_move_length(self):
        pts = [x[0].coords[0] for x in self.movelist]
        a = self.math.make_lines(pts)
        self.lines = a
        l = [line.length for line in self.lines]
        return sum(l)/len(self.lines)
 
if __name__ == '__main__':
    m = MoveList()
    m.read_from_file(sys.argv[1])
    m.avg_move_length()
    print m
