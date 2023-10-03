#!/usr/bin/env ruby

# Check if the input argument is provided
if ARGV.length != 1
  puts "Usage: ./100-textme.rb 'log_entry'"
  exit 1
end

# Extract the sender, receiver, and flags using regex
log_entry = ARGV[0]
match = log_entry.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# Check if the log entry matches the expected format
if match
  sender = match[1]
  receiver = match[2]
  flags = match[3]
  puts "#{sender},#{receiver},#{flags}"
else
  puts "Invalid log entry format."
end
