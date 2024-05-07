def contain_virus(grid)
  return 0 if grid.empty?
  height = grid.size
  width = grid[0].size
  answer = 0.0

  # 定义四个方向：上，右，下，左
  directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

  (0...height).each do |i|
    (0...width).each do |j|
      if 1 == grid[i][j]
        perimeter = 4
        # 遍历每个方向
        directions.each do |dx, dy|
          x, y = i + dx, j + dy
          # 检查相邻单元格
          if x.between?(0, height - 1) && y.between?(0, width - 1) && grid[x][y] == 1
            perimeter -= 1 # 如果其中有1，那么则减去1
          end
        end
        answer += perimeter
      end
    end
  end

  answer
end

isInfected = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
result = contain_virus(isInfected)
puts "Number of walls needed: #{result}"
