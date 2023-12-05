#!/usr/bin/env bash
# automating config files using puppet
file { 'etc/ssh/ssh_config' :
	ensure => present,
content =>" 
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no",
}
