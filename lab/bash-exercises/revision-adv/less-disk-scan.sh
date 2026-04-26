#!/bin/bash

tresh=${1:-70}

echo $tresh

for disk in $(ls /dev/sd*); do
	echo "Monitoring: ${disk}"
	cnt=5
	while [[ $cnt -ge 0 ]]; do
		used=$(df -h $disk | awk 'NR==2{print $5}' | tr -d %)
		echo "used: ${used}"
		if [[ $used -ge $tresh ]]; then
			echo "${disk} over treshold ${tresh}"
		else
			echo "OK"
		fi
		(( cnt-- ))
		sleep 1;
	done
done
