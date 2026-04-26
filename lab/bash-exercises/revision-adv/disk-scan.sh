#!/bin/bash

thresh=${1:-70}

cnt=0
df -h | tail -n +2 | while read -r fs size used avail prc mnt; do
	prc=${prc%%%}
	if [[ ${prc} -ge $thresh ]]; then
		echo "ALERT: disk $fs at $prc. Over threshold!"
	else
		echo "OK: disk $fs at usage $prc" 
	fi

	(( cnt++ ))
	if [[ $cnt -ge 10 ]]; then
		break
	fi
done
