#!/bin/bash

x=`echo "428-$1-16.5" | bc`
y=`echo "$2+0.0" | bc`

echo "$x, $y"

for range in 5 10 20 50 ; do

echo  "Running sonar at $x, $y with range $range";

roslaunch launch/${range}sonar.launch 1>bags/micron_${x}_${y}_${range}.out 2>bags/micron_${x}_${y}_${range}.err  &
rosbag record -a &> bags/micron_${x}_${y}_${range}.record.out &

sleep 60

rospid=`ps aux | grep roslaunch | awk  ' {split($0,a," "); print a[2]; } '`
bagpid=`ps aux | grep record | awk  ' {split($0,a," "); print a[2]; } '`

kill -2 $rospid
sleep 1
kill -2 $bagpid

mv *.bag.active bags/micron_${x}_${y}_${range}.bag

done
date
echo "Done!"