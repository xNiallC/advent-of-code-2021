from functools import reduce

# With diagonals -> (X-1, Y-1), (X, Y-1), (X+1, Y-1), (X+1, Y), (X+1, Y+1), (X, Y+1), (X-1, Y+1), (X-1, Y)
# Without diagonals -> (X, Y-1), (X+1, Y), (X, Y+1), (X-1, Y)
def get_point(adjacent_index, coord, lines):
  (x_coord, y_coord) = coord
  is_final_x = (x_coord == (len(lines[y_coord]) - 1))
  is_final_y = (y_coord == (len(lines) - 1))
  if adjacent_index == 0:
    adjacent_coord = (x_coord, y_coord-1)
    if (y_coord == 0):
      return (adjacent_coord, None)
    return (adjacent_coord, lines[y_coord-1][x_coord])
  if adjacent_index == 1:
    adjacent_coord = (x_coord+1, y_coord)
    if is_final_x:
      return (adjacent_coord, None)
    return (adjacent_coord, lines[y_coord][x_coord+1])
  if adjacent_index == 2:
    adjacent_coord = (x_coord, y_coord+1)
    if is_final_y:
      return (adjacent_coord, None)
    return (adjacent_coord, lines[y_coord+1][x_coord])
  if adjacent_index == 3:
    adjacent_coord = (x_coord-1, y_coord)
    if (x_coord == 0):
      return (adjacent_coord, None)
    return (adjacent_coord, lines[y_coord][x_coord-1])

def is_low_point(value, adjacents):
  for adjacent in adjacents:
    if adjacent != None:
      if value >= int(adjacent):
        return False
  return True

def get_all_adjacent_points(lines):
  all_basins = []
  visited = []
  for line in lines:
    new_visited = []
    for value in line:
      new_visited.append(False)
    visited.append(new_visited)

  curr_basin = []
  def get_adjacent_points_recursively(for_coords):
    value = lines[for_coords[1]][for_coords[0]]
    visited_value = visited[for_coords[1]][for_coords[0]]
    # Already been here, so can't be part of another basin
    if visited_value:
      return
    if int(value) == 9:
      return
    visited[for_coords[1]][for_coords[0]] = True
    curr_basin.append(int(value))
    adjacents = []
    for a_index in range(0, 4):
      adjacent_item = get_point(a_index, for_coords, lines)
      if adjacent_item[1] != None:
        if int(adjacent_item[1]) != 9:
          adjacents.append(adjacent_item[0])
    for a in adjacents:
      get_adjacent_points_recursively(a)

  for y_coord, value in enumerate(lines):
    for x_coord, line in enumerate(value):
      get_adjacent_points_recursively((x_coord, y_coord))
      if len(curr_basin) > 0:
        all_basins.append(curr_basin)
      curr_basin = []
  return all_basins

def main():
  with open('./input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  all_basins = get_all_adjacent_points(content)
  summed_basins = [len(basin) for basin in all_basins]
  print(all_basins)
  print(summed_basins)
  sorted_basins = sorted(summed_basins)
  print(sum(sorted_basins[-3:]))
  print(reduce(lambda x, y: x*y, sorted_basins[-3:]))

if __name__ == '__main__':
  main()