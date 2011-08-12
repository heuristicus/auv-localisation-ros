#!/bin/bash

for range in 5 10 20 50 ; do

for ext in bag err out record.out ; do

mv micron_353.5_342.0_$range.$ext micron_353.5_348.0_$range.$ext

done
done
