import copy

n_flashes = 0

def main():
  with open('./input_test.txt') as f:
    content = f.readlines()
  content = [[int(y) for y in x.strip()] for x in content]
  handled_content = [{
    'value': item,
    'has_flashed': False
  } for item in content]

  global n_flashes
  steps_left = 1
  possible_values = [0,1,2,3,4,5,6,7,8,9,10]
  octopus_map = {
    0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []
  }

  def product_octopus_map():
    for y_coord, line in enumerate(content):
      for x_coord, octopus in enumerate(line):
        octopus_map[octopus].append({ 'has_flashed': False, 'coord': (x_coord, y_coord) })
  # Now we have a map of all possible values of an octopus
  product_octopus_map()
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
      coords_to_increase.append(content[y_coord-1][x_coord])

    adjacent_coord = (x_coord+1, y_coord)
    if is_final_x:
      coords_to_increase.append(None)
    else:
      coords_to_increase.append(content[y_coord][x_coord+1])

    adjacent_coord = (x_coord, y_coord+1)
    if is_final_y:
      coords_to_increase.append(None)
    else:
      coords_to_increase.append(content[y_coord+1][x_coord])

    adjacent_coord = (x_coord-1, y_coord)
    if (x_coord == 0):
      coords_to_increase.append(None)
    else:
      coords_to_increase.append(content[y_coord][x_coord-1])

    return coords_to_increase

  def handle_step():
    prev_octopus_coords = []
    new_octopus_map_state = {
      0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []
    }
    for energy_value in range(1,11):
      for item in prev_octopus_coords:
        new_octopus_map_state[energy_value - 1].append(item)
      print('Setting ' + str(energy_value) + ' to ' + str([item['coord'] for item in prev_octopus_coords]))
      prev_octopus_coords = [*octopus_map[energy_value]]
    print(new_octopus_map_state[2])

  def handle_increase(coords_to_increase):
    # For each coordinate
    # We find it in the map
    # Remove it from it's current value
    # Add it to the next value
    for coord in coords_to_increase:
      for energy_value in range(1,10):
        just_coords = [item['coord'] for item in octopus_map[energy_value]]
        if coord in just_coords:
          find_info = next((item for item in octopus_map[energy_value] if item['coord'] == coord))
          octopus_map[energy_value + 1].append(find_info)
          octopus_map[energy_value] = [item for item in octopus_map[energy_value] if item['coord'] != coord]

  def handle_flashes():
    octopuses_to_flash = [*octopus_map[9], *octopus_map[10]]
    all_coords_to_increase = []
    n_flashes = 0
    for octopus in [octopus for octopus in octopuses_to_flash if not octopus['has_flashed']]:
      octopus['has_flashed'] = True
      n_flashes = n_flashes + 1
      coords_to_increase = get_coords_to_increase(octopus['coord'])
      for coord in coords_to_increase:
        if coord != None and coord not in all_coords_to_increase:
          all_coords_to_increase.append(coord)
    return all_coords_to_increase

  def should_continue_step():
    if len(octopus_map[9]) == 0: return False
    return len([item for item in octopus_map[9] if not item['has_flashed']]) > 0

  def recurse_step(should_step=True, n_flashes_local = 0):
    if should_step:
      handle_step()
    to_increase = handle_flashes()
    handle_increase(to_increase)
    should_continue = should_continue_step()
    if should_continue:
      recurse_step(should_step=False, n_flashes_local=n_flashes_local)

  for step in range(0, steps_left):
    recurse_step()


  
if __name__ == '__main__':
  main()