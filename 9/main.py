class BasinItem:
  def __init__(self, val):
    self.val = val
    self.above = ((0, 0), None)
    self.right = ((0, 0), None)
    self.below = ((0, 0), None)
    self.left = ((0, 0), None)

# With diagonals -> (X-1, Y-1), (X, Y-1), (X+1, Y-1), (X+1, Y), (X+1, Y+1), (X, Y+1), (X-1, Y+1), (X-1, Y)
# Without diagonals -> (X, Y-1), (X+1, Y), (X, Y+1), (X-1, Y)
def get_point(coord, lines):
  (x_coord, y_coord) = coord
  try:
    value = int(lines[y_coord][x_coord])
  except:
    return BasinItem(None)

  current_item = BasinItem(value)

  is_final_x = (x_coord == (len(lines[y_coord]) - 1))
  is_final_y = (y_coord == (len(lines) - 1))

  adjacent_coord = (x_coord, y_coord-1)
  if (y_coord == 0):
    current_item.above = (adjacent_coord, None)
  else:
    current_item.above = (adjacent_coord, lines[y_coord-1][x_coord])

  adjacent_coord = (x_coord+1, y_coord)
  if is_final_x:
    current_item.right = (adjacent_coord, None)
  else:
    current_item.right = (adjacent_coord, lines[y_coord][x_coord+1])

  adjacent_coord = (x_coord, y_coord+1)
  if is_final_y:
    current_item.below = (adjacent_coord, None)
  else:
    current_item.below = (adjacent_coord, lines[y_coord+1][x_coord])

  adjacent_coord = (x_coord-1, y_coord)
  if (x_coord == 0):
    current_item.left = (adjacent_coord, None)
  else:
    current_item.left = (adjacent_coord, lines[y_coord][x_coord-1])

  return current_item

def is_low_point(value, adjacents):
  for adjacent in adjacents:
    if adjacent != None:
      if value >= int(adjacent):
        return False
  return True


def get_adjacent_points_recursively(current_point, lines, basin_values = [], prev_point = None):
  # If current point is nothing, well, we do nothing
  if current_point.val == None:
    return
  # If current value is less than it's previous, or previous, doesn't exist, begin tracking basin
  # Else do nothing and return basin values
  if prev_point and (current_point.val >= prev_point.val):
    return

  basin_values.append(current_point.val)
  print(basin_values)

  # For all children, recurse
  get_adjacent_points_recursively(get_point(current_point.above[0], lines), lines, basin_values, current_point)
  get_adjacent_points_recursively(get_point(current_point.right[0], lines), lines, basin_values, current_point)
  get_adjacent_points_recursively(get_point(current_point.below[0], lines), lines, basin_values, current_point)
  get_adjacent_points_recursively(get_point(current_point.left[0], lines), lines, basin_values, current_point)

def get_all_adjacent_points(lines):
  all_basins = []
  for y_coord, value in enumerate(lines):
    for x_coord, line in enumerate(value):
      current_point = get_point((x_coord, y_coord), lines)
      all_basins.append(get_adjacent_points_recursively(current_point, lines))
      break
    break
  return all_basins

def main():
  with open('./input_test.txt') as f:
    content = f.readlines()
  content = [[y for y in x.strip()] for x in content]
  all_basins = get_all_adjacent_points(content)
  print(all_basins)

if __name__ == '__main__':
  main()