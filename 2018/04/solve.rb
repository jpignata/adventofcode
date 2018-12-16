require "time"

guards = Hash.new { |h, k| h[k] = [] }

lines = ARGF.readlines.map do |line|
  timestamp, log = /\[([0-9:\- ]{16})\] (.*)/.match(line).captures
  [Time.parse(timestamp), log]
end

current_guard = nil
sleep_start = nil

lines.sort_by(&:first).each do |(timestamp, line)|
  case line
  when /Guard #([0-9]*) begins shift/
    current_guard = $1.to_i
    sleep_start = nil
  when "falls asleep"
    sleep_start = timestamp
  when "wakes up"
    until sleep_start == timestamp
      guards[current_guard] << sleep_start.min
      sleep_start += 60
    end
    sleep_start = nil
  end
end

index = guards.map do |id, mins|
  [id, Hash[mins.group_by { |m| m }.map { |k, v| [k, v.count] }]]
end

guard1 = index.max_by { |id, mins| mins.sum(&:last) }
p guard1.first * guard1.last.max_by(&:last).first

guard2 = index.max_by { |_, mins| mins.values }
p guard2.first * guard2.last.max_by(&:last).first
