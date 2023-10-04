#!/usr/bin/env ruby
# script of a regular expression that matches only capital letters
puts ARGV[0].scan(/[A-Z]/).join
