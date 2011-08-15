#!/bin/bash

for val in $(ls $1 | grep bag | awk 'BEGIN{FS=" "}{print $1}')

do
    echo $val
done
