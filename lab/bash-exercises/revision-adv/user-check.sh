#!/bin/bash

validate_user() {
	local user
	user=$1

	id $user &>/dev/null || return 1

	local get_passwd
	get_passwd=$(getent passwd "$user")

	local home_dir
	home_dir=$(echo "$get_passwd" | cut -d: -f6)

	local user_shell
	user_shell=$(echo "$get_passwd" | cut -d: -f7)

	[ -d "$home_dir" ] || return 2
	[[ "$user_shell" == /bin/bash ]] || return 3
	return 0

}

err() {
	echo "Forgot to enter the user."
	exit 4
}

main() {
	if [[ -z $1 ]]; then
		err
	fi
	validate_user $1
	code=$?
	if [[ $code -ne 0 ]]; then
		echo "Invalid: code $code"
		exit $code 
	fi
}

main $1
