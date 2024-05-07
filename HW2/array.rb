class Array
  alias_method :original_brackets, :[]
  alias_method :original_map, :map

  # 重定义 [] 方法
  def [](index)
    index.between?(-self.length, self.length - 1) ? original_brackets(index) : '\0'
  end

  # 重定义 map 方法，使其可以接受一个可选的序列参数
  def map(*args)
    sequence = args.first.is_a?(Range) ? args.shift : nil
    if sequence
      sequence.map { |i| self[i] ? yield(self[i]) : nil }.compact
    else
      original_map { |item| yield(item) }
    end
  end
end

# 示例测试
a = [1, 2, 34, 5]
puts a[1]    # 输出: 2
puts a[10]   # 输出: \0

puts a.map(2..4) { |i| i.to_f }.inspect  # 输出: [34.0, 5.0]
puts a.map { |i| i.to_f }.inspect        # 输出: [1.0, 2.0, 34.0, 5.0]

b = ["cat", "bat", "mat", "sat"]
puts b[-1]   # 输出: sat
puts b[5]    # 输出: \0

puts b.map(2..10) { |x| x[0].upcase + x[1, x.length] }.inspect  # 输出: ["Mat", "Sat"]
puts b.map(2..4) { |x| x[0].upcase + x[1, x.length] }.inspect   # 输出: ["Mat", "Sat"]
puts b.map(-3..-1) { |x| x[0].upcase + x[1, x.length] }.inspect # 输出: ["Bat", "Mat", "Sat"]
puts b.map { |x| x[0].upcase + x[1, x.length] }.inspect         # 输出: ["Cat", "Bat", "Mat", "Sat"]
