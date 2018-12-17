Node = Struct.new(:header, :children, :metadata) do
  def sum
    metadata.sum + children.sum(&:sum)
  end

  def value
    return sum if children.empty?

    metadata.sum do |node|
      children[node - 1] ? children[node - 1].value : 0
    end
  end
end

def extract_node(data)
  num_children = data.next
  num_metadata = data.next

  header = [num_children, num_metadata]
  children = num_children.times.map { extract_node(data) }
  metadata = num_metadata.times.map { data.next }

  return Node.new(header, children, metadata)
end

data = ARGF.readlines[0].chomp.split(" ").map(&:to_i)
root = extract_node(data.each)

puts root.sum
puts root.value
