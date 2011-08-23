xparam=sonar/x
yparam=sonar/y
rparam=sonar/rng
utp=/param_update
umsg="update"

for r in 5 ; do
    
    echo $r
    
    for val in $(ls $1 | grep $r.bag | awk 'BEGIN{FS=" "}{print $1}'); do

	echo Checking filename $val for coordinate and range data...
	[[ $val =~ micron_([0-9]+.[0-9]+)_([0-9]+.[0-9]+)_$r.bag ]]
    
	
	if [ ! ${BASH_REMATCH} ]
	then
	    echo No match, skipping file.
	else
	    echo Match found...
	    x=${BASH_REMATCH[1]}
	    y=${BASH_REMATCH[2]}
	    rng=${BASH_REMATCH[3]}
	    echo Sending parameters to ros server...
	    echo $xparam = $x
	    echo $yparam = $y
	    echo $rparam = $r
	    rosparam set $xparam $x
	    rosparam set $yparam $y
	    rosparam set $rparam $r
	    echo Sending update notification to topic $utp
	    rostopic pub $utp std_msgs/String $umsg &
	    sleep 1 # give the process node some time to save data
	    rosbag play -i $1/$val
	fi
	sleep 1
    done
done