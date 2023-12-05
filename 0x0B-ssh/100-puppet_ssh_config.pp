#!/usr/bin/env bash
file { 'etc/ssh/ssh_config' :
	ensure => present,
content =>" 
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no"
}
