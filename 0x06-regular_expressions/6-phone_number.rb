#!/usr/bin/env ruby
# script of a regular expression that matches a 10 digit phone number
puts ARGV[0].scan(/^[0-9]{10}$/).join
