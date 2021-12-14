from queue import SimpleQueue

n_flashes = 0

def main():
  with open('./input.txt') as f:
    content = f.readlines()
  content = [[int(y) for y in x.strip()] for x in content]

  # For any given step:
  # - Octopuses are all moved up a step
  #     - We just move the array to the next value, with the exception of value 10, where nothing happens
  # - All octopuses at values 9 and 10 flash, if they haven't flashed this step
  #     - Their has_flash changes to true
  #     - They are all transferred to the array at value 0
  # - For the octopuses that flashed, we get their neighbours
  # - These neighbours are moved to the next level up, removed from their current level
  # - Once we handle all the flashes, we return to check the status of all the octopuses in value 9
  # - If there is anything in the row that hasn't flashed, we need to repeat the flash process
  # - If the array is empty or everything has flashed, we move to the next step

  def get_coords_to_increase(coord):
    coords_to_increase = []
    (x_coord, y_coord) = coord
    is_final_x = (x_coord == (len(content[y_coord]) - 1))
    is_final_y = (y_coord == (len(content) - 1))

    adjacent_coord = (x_coord, y_coord-1)
    if (y_coord == 0):
      coords_to_increase.append(None)
    else:
      coords_to_increase.append(adjacent_coord)

    adjacent_coord = (x_coord+1, y_coord)
    if is_final_x:
      coords_to_increase.append(None)
    else:
      coords_to_increase.append(adjacent_coord)

    adjacent_coord = (x_coord, y_coord+1)
    if is_final_y:
      coords_to_increase.append(None)
    else:
      coords_to_increase.append(adjacent_coord)

    adjacent_coord = (x_coord-1, y_coord)
    if (x_coord == 0):
      coords_to_increase.append(None)
    else:
      coords_to_increase.append(adjacent_coord)

    return coords_to_increase


  total_flash_count = 0

  def handle_step():
    to_flash = SimpleQueue()
    flash_count = 0

    for y_index, line in enumerate(content):
      for x_index, octopus in enumerate(line):
        content[y_index][x_index] += 1
        if content[y_index][x_index] > 9:
          to_flash.put((x_index, y_index))

    while to_flash.qsize() > 0:
      to_flash_coord = to_flash.get()
      if content[to_flash_coord[1]][to_flash_coord[0]] > 9:
        flash_count += 1
        content[to_flash_coord[1]][to_flash_coord[0]] = 0
        adjacents_to_flash = get_coords_to_increase(to_flash_coord)
        print(adjacents_to_flash)
        for adjacent in [item for item in adjacents_to_flash if item != None]:
          (adjacent_x, adjacent_y) = adjacent
          if content[adjacent_y][adjacent_x] != 0:
            content[adjacent_y][adjacent_x] += 1
          if content[adjacent_y][adjacent_x] > 9:
            to_flash.put(adjacent)
    return flash_count

  n_steps = 100

  for step in range(n_steps):
    new_count = handle_step()
    total_flash_count += new_count
  
  for line in content:
    print(line)

  print(total_flash_count)
  
if __name__ == '__main__':
  main()