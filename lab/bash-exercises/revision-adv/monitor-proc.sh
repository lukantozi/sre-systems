#!/bin/bash

trap 'exit 0' INT

log_alert() {
	local log="$(date '+%Y-%m-%d %H:%M:%S') - $1"
	echo "$log"
	echo "$log" >> "$HOME/proc_monitor.log"
}

main() {
	declare -i dur
	dur=${2:-10}
	cnt=0
	while [[ $cnt -le $dur ]]; do
		stat=$(pgrep -c "$1" 2>/dev/null)
		if [[ $stat -eq 0 ]]; then
			log_alert "ALERT: $1 is DOWN"
		elif [[ $stat -le 5 ]]; then
			log_alert "OK: $1"
		else
			log_alert "ALERT: $1 is HIGH ($stat procs)"
		fi
		(( cnt += 5 ))
		sleep 5
	done
}

main $1 $2
