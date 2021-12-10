# With diagonals -> (X-1, Y-1), (X, Y-1), (X+1, Y-1), (X+1, Y), (X+1, Y+1), (X, Y+1), (X-1, Y+1), (X-1, Y)
# Without diagonals -> (X, Y-1), (X+1, Y), (X, Y+1), (X-1, Y)
def get_point(adjacent_index, coord, lines):
  (x_coord, y_coord) = coord
  is_final_x = (x_coord == (len(lines[y_coord]) - 1))
  is_final_y = (y_coord == (len(lines) - 1))
  if adjacent_index == 0:
    if (y_coord == 0):
      return None
    return lines[y_coord-1][x_coord]
  if adjacent_index == 1:
    if is_final_x:
      return None
    return lines[y_coord][x_coord+1]
  if adjacent_index == 2:
    if is_final_y:
      return None
    return lines[y_coord+1][x_coord]
  if adjacent_index == 3:
    if (x_coord == 0):
      return None
    return lines[y_coord][x_coord-1]

def is_low_point(value, adjacents):
  for adjacent in adjacents:
    if adjacent != None:
      if value >= int(adjacent):
        return False
  return True

def get_adjacent_points(for_coords, lines):
  # If the X of a coord is 0, then there is nothing to the left of it
  # If the X coord is (len(lines[X]) - 1), then there is nothing to the right of it
  # If the Y coord is 0, there is nothing above it
  # If the Y coord is (len(lines) - 1), there is nothing below it
  #
  # Data is returned as a tuple, with (coord, adjacents)
  # Adjacents is a list starting from the value above and to the left of the element, going clockwise. If nothing is present, we use None
  # Diagonals are not included
  # The length of adjacents is always 4, if not diagonals
  # Therefore, the first item in the list begins at (X, Y-1)
  adjacents = []
  value = int(lines[for_coords[1]][for_coords[0]])
  for adjacent_item in range(0, 4):
    adjacents.append(get_point(adjacent_item, for_coords, lines))
  return {
    'value': value,
    'coords': for_coords,
    'adjacents': adjacents,
    'is_low_point': is_low_point(value, adjacents),
    'risk_level': value + 1
  }

def get_all_adjacent_points(lines):
  all_adjacents = []
  for y_coord, value in enumerate(lines):
    for x_coord, line in enumerate(value):
      all_adjacents.append(get_adjacent_points((x_coord, y_coord), lines))
  return all_adjacents

def main():
  with open('./input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  all_adjacent_points = get_all_adjacent_points(content)
  low_points = [point for point in all_adjacent_points if point['is_low_point']]
  print(len(low_points))
  print(low_points)
  print(sum(item['risk_level'] for item in low_points))

if __name__ == '__main__':
  main()