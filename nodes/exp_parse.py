#!/usr/bin/python
import sys
import re

class TestParser():
    
    def __init__(self):
        self.make_lists()
        self.produce_output()

    def make_lists(self):
        f = open(sys.argv[1])
        data = f.read()
        
        # split each test to a separate list, ignoring the blank
        confs = data.split('newconf\n')[1:] 
        tests = []
        for conf in confs:
            # each test has a number of positions that the sonar goes
            # through according to the movelist, so split those up
            tests.append(re.split('\nnewtest', conf))
            splitsteps = []
        for test in tests:
            for num in map(lambda x: x + 1, range(len(test[1:]))):
                test[num] = re.split('step \d+\n', test[num])
                for step in range(len(test[num])):
                    test[num][step] = test[num][step].split('\n')
        
        confs = []
        starts = []
        ends = []
        steps = []
        for test in tests:
            confs.append(test[0])
            t_end = []
            t_start = []
            t_step = []
            for item in test[1:]:
                end = item[-1]
                t_end.append(end[0].split(' ')[1])
                start = item[0][1].split(' ')[1]
                t_start.append(start)
                step = item[1:-1]
                t_step.append(step)
            steps.append(t_step)
            ends.append(t_end)
            starts.append(t_start)
        self.confs = confs
        self.starts = starts
        self.steps = steps
        self.ends = ends
                            
    def produce_output(self):
        res = ''
        for i in range(len(self.confs)):
            for j in range(len(self.starts[i])):
                res += '%s\n'%(self.confs[i])
                start = self.starts[i][j]
                end = self.ends[i][j]
                res += 'Start time: %s\nEnd time: %s\n'%(start, end)
                timediff = float(self.ends[i][j]) - float(self.starts[i][j])
                res += 'Time taken: %4.2f seconds\n'%(timediff)
                avgtstep = timediff/len(self.steps[i][j][:-1])
                res += 'Average time per step: %4.2f seconds\n'%(avgtstep)
                for step in self.steps[i][j][:-1]:
                    self.get_tuple(step[0])
                    self.get_point_list(step[3])
                    #res += 'Sonar position: %s\n'%(re.findall(sonar))
                    #res += 'Best particle position: %s\n'%(re.findall(' (.*)',step[2])[0])
                    #res += 'Particle difference: %s\n'%(re.findall(' (.*)'), step[2])
        print res

    def get_tuple(self, string):
        """Makes a 2 element tuple from a string of integers in the tuple format"""
        a = re.search('\((\d+\.\d+), (\d+\.\d+)\)', string)
        if not a:
            return None
        else:
            return (float(a.group(1)), float(a.group(2)))    

    
    def get_point_list(self, string):
        """Converts a string of tuples in list format to a list"""
        a = re.findall('\(\d+\.\d+, \d+\.\d+\)', string)
        lst = []
        for tp in a:
            lst.append(self.get_tuple(tp))
        print lst

    def get_flt_list(self, string):
        print 'a'
        
        


if __name__ == '__main__':
    TestParser()
