#!/bin/bash

parse_ip() {
	
	first_field=($(awk '{print $1}' | sort | uniq -c))
	declare -i ind=0
	while [[ $ind -lt ${#first_field[@]} ]]; do
		if [[ ${first_field[ind]} -ge 100 ]]; then
			echo "FLOOD: ${first_field[ind+1]} ${first_field[ind]}"
			exit 3
		else
			echo "OK: ${first_field[ind+1]} ${first_field[ind]}"
		fi
		(( ind += 2))
	done
}

parse_ip
