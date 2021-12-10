def calculate_crab_movement(crab_positions, final_pos=0):
  # Movement is abs difference between values
  fuel_used = 0
  for crab_position in crab_positions:
    #print('For position ' + str(crab_position) + ' to final pos ' + str(final_pos))
    n_positions_moved = abs(crab_position - final_pos)
    #print(n_positions_moved)
    fuel_used += ((n_positions_moved * (n_positions_moved + 1)) / 2)
    #print(fuel_used)
  return fuel_used

def calculate_all_fuel_used(crab_positions):
  best_final_pos = {}
  for test_final_pos in range(0, len(crab_positions)):
    fuel_used = calculate_crab_movement(crab_positions, test_final_pos)
    print('Testing:')
    print({ 'position': test_final_pos, 'fuel_used': fuel_used })
    if not best_final_pos.get('position') or (fuel_used < best_final_pos['fuel_used']):
      best_final_pos = { 'position': test_final_pos, 'fuel_used': fuel_used }
  return best_final_pos

def main():
  with open('./input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  crab_positions = [int(item) for item in content[0].split(',')]
  avg_position = int(sum(crab_positions) / len(crab_positions))

  best_final_pos = calculate_all_fuel_used(crab_positions)
  print('Final:')
  print(best_final_pos)

if __name__ == '__main__':
  main()