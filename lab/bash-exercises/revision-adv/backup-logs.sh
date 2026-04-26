#!/bin/bash

#set -x

arg1=$1
logdir=${arg1:-"/var/log"}
echo "${logdir}"
mkdir -p ~/backup-logs/errors

counter=0
while true; do
	sudo journalctl --no-pager -u ssh >\
		$HOME/backup-logs/backup-ssh-$(date +%Y_%m_%d_%H:%M:%S).log 2>>\
		$HOME/backup-logs/errors/backup-ssh-errors.log

	space=$(df -h / | awk 'NR==2 {print $5}')
	if (( ${space::-1} > 80 )); then
		echo "disk reached 80%"
		exit 2
	fi

	(( counter++ ))
	if [[ $counter -ge 5 ]]; then
		break
	fi
sleep 10
done
