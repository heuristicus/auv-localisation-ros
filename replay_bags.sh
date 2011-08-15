#!/bin/bash

for val in $(ls $1 | grep bag | awk 'BEGIN{FS=" "}{print $1}')

do
    rosbag info $1/$val >> bag_info.txt
done

echo `grep ERROR < bag_info.txt`

exit

do
    echo $val
    rosparam set sonar/x 10
    rosparam set sonar/y 10
    rosparam set sonar/rng 50
    rostopic pub /param_update std_msgs/String "update" &
    
    rosbag play $1/$val
    sleep 2
done
