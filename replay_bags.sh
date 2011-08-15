xparam=sonar/x
yparam=sonar/y
rparam=sonar/rng
utp=/param_update
umsg="update"


for val in $(ls $1 | grep bag | awk 'BEGIN{FS=" "}{print $1}')

do
    echo Checking filename $val for coordinate and range data...
    [[ $val =~ micron_([0-9]+.[0-9]+)_([0-9]+.[0-9]+)_([0-9]+).bag ]]
    
    
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
	echo $rparam = $rng
	rosparam set $xparam $x
	rosparam set $yparam $y
	rosparam set $rparam $rng
	echo Sending update notification to topic $utp
	rostopic pub $utp std_msgs/String $umsg &
	sleep 2 # give the process node some time to save data
	rosbag play $1/$val
    fi
    
    sleep 2
done
