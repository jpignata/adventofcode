steps = {}

ARGF.readlines.map { |line|
  line =~ /Step ([A-Z]+) must be finished before step ([A-Z]+) can begin./
  steps[$1] ||= []
  steps[$2] ||= []
  steps[$2] << $1
}

done = []

until done.length == steps.keys.length
  steps.sort.each do |(step, requirements)|
    next if done.include?(step)

    if requirements & done == requirements
      done << step
      break
    end
  end
end

puts done.join

done.clear

Worker = Struct.new(:current, :started)

workers = 5.times.map { Worker.new }
duration = 60
clock = 0

until done.length == steps.keys.length
  workers.each do |worker|
    if worker.current
      if (worker.started - clock).abs >= (duration + worker.current.ord - 64)
        done << worker.current
        worker.current = nil
        worker.started = nil
      else
        next
      end
    end

    steps.sort.each do |(step, requirements)|
      next if done.include?(step)
      next if workers.map(&:current).compact.include?(step)

      if requirements & done == requirements
        worker.current = step
        worker.started = clock
        break
      end
    end
  end

  clock += 1
end

puts clock - 1
