#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy
from loc_sonar.msg import proc_sonar, point
from Tkinter import Tk, Canvas, Button
import s_math

class ExpSonar:

    def __init__(self, fileloc, rng=5, sleeptime=2):
        # experiment with range rng
        self.rng = rng
        self.sleeptime = sleeptime
        self.fileloc = fileloc
        # list of points and coords of experiments
        self.pt_dict = {'1': '68,68', '2': '67,136','3': '138,68','4': '138,136','5': '197,68','6': '197,136','7': '259,68','8': '259,136','9': '327,68','10': '327,136','11': '366,25','12': '366,136','13': '353,204','14': '353,272','15': '295,204','16': '295,272','17': '353,348','18': '353,408','19': '353,476','20': '295,348','21': '295,408','22': '295,476'}

        self.make_pub()

        self.r = Tk()
        self.c = Canvas(self.r, width=400, height=600)
        self.c.pack()
        self.mv = []
        self.smath = s_math.SonarMath()
        self.pts = []
        self.ovals = []
        self.run = Button(self.r, text='run', command=self.run)
        self.run.pack()
        self.reset = Button(self.r, text='reset', command=self.reset)
        self.reset.pack()
        for key in self.pt_dict:
            a = map(int, self.pt_dict[key].split(','))
            self.pts.append(a)
            self.c.create_oval(a[0] -1, a[1] -1, a[0] + 1, a[1] + 1)
    
        self.c.bind("<Button-1>", self.path)
        self.r.mainloop()

    def path(self, event):
        x = event.x
        y = event.y
        pe = [x,y]
        
        for pt in self.pts:
            if self.smath.pt_dist(pt, pe) <= 10:
                self.mv.append(pt)

        if len(self.mv) > 1:
            self.c.create_line(self.mv[-2][0], self.mv[-2][1], self.mv[-1][0], self.mv[-1][1], tags='mvline')

    def reset(self):
        self.mv = []
        self.c.delete('mvline')
        
    def run(self):
        for i, p in enumerate(self.mv):
            fname = '%s/prc_%d_%d_%d.txt'%(self.fileloc, p[0],p[1], self.rng)
            data = proc_sonar()
            try:
                f = open(fname, 'r')
                # print '%s/prc_%d_%d_%d.txt'%(self.fileloc, p[0],p[1], self.rng)
                data.prev = point(self.mv[i - 1][0],self.mv[i - 1][1]) if i != 0 else point(self.mv[i][0], self.mv[i][1])
                data.next = point(self.mv[i][0], self.mv[i][1])
                data.angle = 0
                data.ranges = map(float, f.read().split(' '))
                data.actual = point(p[0], p[1])
                self.pub.publish(data)
            except IOError:
                print 'file %s does not exist'%(fname)

            rospy.sleep(self.sleeptime) # artificial time an action takes
        self.run.config(state='disabled')
        
    def make_pub(self):
        self.pub = rospy.Publisher('sonar_sim_readable', proc_sonar)
        rospy.init_node('experiment_gui')

if __name__ == '__main__':
    ExpSonar(rospy.get_param('exp_dir'))
