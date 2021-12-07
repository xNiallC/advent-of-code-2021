


def draw_line(vent, sea_floor_map):
  print(vent)
  moving_direction = 1 if (vent[0][0] == vent[1][0]) else 0 # 1 indicates vertical movement, 0 indicates horizontal

  vent_start = min(vent[0][moving_direction], vent[1][moving_direction])
  vent_end = max(vent[0][moving_direction], vent[1][moving_direction]) + 1
  fixed_orientation = vent[0][1 if moving_direction == 0 else 0]

  movement = range(vent_start, vent_end)

  # Move vertically
  if vent[0][0] == vent[1][0]:
    for y_movement in movement:
      sea_floor_map[y_movement][fixed_orientation] += 1
  # Move horizontally
  elif vent[0][1] == vent[1][1]:
    for x_movement in movement:
      sea_floor_map[fixed_orientation][x_movement] += 1
  else:
    lower_y = 0 if vent[0][1] > vent[1][1] else 1
    upper_y = int(not lower_y)

    start_x = min(vent[0][0], vent[1][0])
    stop_x = max(vent[0][0], vent[1][0]) + 1

    direction = 1 if vent[lower_y][0] > vent[upper_y][0] else -1

    y = vent[upper_y][1] if direction == 1 else vent[lower_y][1]
    
    for x in range(start_x, stop_x):
        sea_floor_map[y][x] += 1
        y += direction   


def create_sea_map(input):
  # Get the highest X and Y value. Then we can populate an empty map
  highest_x = 0
  highest_y = 0
  for line in input:
    for coord in line:
      if coord[0] > highest_x:
        highest_x = coord[0]
      if coord[1] > highest_y:
        highest_y = coord[1]

  sea_floor_map = []
  x_map_list = []
  for x in range(highest_x + 1):
    x_map_list.append(0)
  for y in range(highest_y + 1):
    sea_floor_map.append([item for item in x_map_list])

  return sea_floor_map

def calculate_hits(sea_floor_map, vents):
  for vent in vents:
    draw_line(vent, sea_floor_map)
  return sea_floor_map

def main():
  with open('./input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  
  # Turn input into list of lists with path of vents
  vents = []
  for line in content:
    new_line = []
    vent_coords = line.split(' -> ')
    for coord in vent_coords:
      new_line.append([int(item) for item in coord.split(',')])
    vents.append(new_line)

  sea_floor_map = create_sea_map(vents)
  final_sea_floor_map = calculate_hits(sea_floor_map, vents)
    
  for row in final_sea_floor_map:
    print(row)

  overlaps = 0
  for row in final_sea_floor_map:
    for number in row:
      if number > 1:
        overlaps += 1
  print(overlaps)

if __name__ == '__main__':
  main()