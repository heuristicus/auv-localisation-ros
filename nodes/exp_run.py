#!/usr/bin/python
import sys, map_rep, move_list, sonar_sim, time


def main():
    out = sys.argv[1]
    m1 = map_rep.map_(fname='i.map')
    mv1 = move_list.MoveList(fname='i.mv')
    
    out_keys = ['max_rng', 'step', 'particle_number'] # keys from the dict to add to file
    
    s1 = {'map_':m1, 'move_list':mv1, 'max_rng':50, 'step': 25, 'particle_number': 1, 'out_file': out}
    #s2 = {'map_':m1, 'move_list':mv1, 'max_rng':50, 'step': 15, 'particle_number': 5, 'out_file': 'data.txt'}
    #s3 = {'map_':m1, 'move_list':mv1, 'max_rng':50, 'step': 5, 'particle_number': 5, 'out_file': 'data.txt'}
    #s4 = {'map_':m1, 'move_list':mv1, 'max_rng':75, 'step': 15, 'particle_number': 5, 'out_file': 'data.txt'}
    s5 = {'map_':m1, 'move_list':mv1, 'max_rng':50, 'step': 15, 'particle_number': 3, 'out_file': out}
    s6 = {'map_':m1, 'move_list':mv1, 'max_rng':50, 'step': 15, 'particle_number': 5, 'out_file': out}
    s7 = {'map_':m1, 'move_list':mv1, 'max_rng':50, 'step': 15, 'particle_number': 8, 'out_file': out}
    s8 = {'map_':m1, 'move_list':mv1, 'max_rng':50, 'step': 15, 'particle_number': 15, 'out_file': out}
    s9 = {'map_':m1, 'move_list':mv1, 'max_rng':50, 'step': 15, 'particle_number': 25, 'out_file': out}
    srs = [s1,s5]
    testnum = 2
    

    for cfg in srs:
        f = open(out, 'a')
        f.write('newconf\n')
        for key in out_keys:
            f.write('%s:%s/'%(key, cfg[key]))
        f.write('\n')
        f.close()
        s = sonar_sim.sonar(**cfg)
        for i in range(testnum):
            f = open(out, 'a')
            f.write('newtest\n')
            f.write('----START----: %s\n'%(time.time()))
            f.close()
            while s.sim_step() is not -1:
                continue
            f = open(out, 'a')
            f.write('step 99999\n')
            f.write('----END----: %s\n'%(time.time()))
            f.close()
            mv1.reset()
     
if __name__ == '__main__':
    main()
