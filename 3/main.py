def get_final_binary_value(diagnostics, index = 0, bit_priority = '1'):
  remaining_diagnostics = []
  number_of_0s = 0
  number_of_1s = 0
  for diagnostic in diagnostics:
    current_diagnostic_bit = int(diagnostic[index])
    if current_diagnostic_bit == 0:
      number_of_0s += 1
    if current_diagnostic_bit == 1:
      number_of_1s += 1
  most_popular_bit = (('0' if number_of_0s > number_of_1s else '1') if (bit_priority == '1') else ('1' if number_of_1s < number_of_0s else '0'))
  remaining_diagnostics = [d for d in diagnostics if d[index] == most_popular_bit]
  if len(remaining_diagnostics) < 2:
    return int(remaining_diagnostics[0], 2)
  return get_final_binary_value(remaining_diagnostics, index + 1, bit_priority)

def main():
  with open('./input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  # Part 1
  #gamma_rate = ''
  #epsilon_rate = ''
  #for bit in range(len(content[0])):
  #  number_of_0s = 0
  #  number_of_1s = 0
  #  for diagnostic in content:
  #    current_diagnostic_bit = int(diagnostic[bit])
  #    if current_diagnostic_bit == 0:
  #      number_of_0s += 1
  #    if current_diagnostic_bit == 1:
  #      number_of_1s += 1
  #  gamma_rate += ('0' if number_of_0s > number_of_1s else '1')
  #  epsilon_rate += ('1' if number_of_0s > number_of_1s else '0')
  #energy_consumption = (int(gamma_rate, 2) * int(epsilon_rate, 2))
  #print('Energy consumption:')
  #print(energy_consumption)

  # Part 2
  o2_rating = get_final_binary_value(content, 0, '1')
  print(o2_rating)

  co2_rating = get_final_binary_value(content, 0, '0')
  print(co2_rating)

  print(o2_rating * co2_rating)

if __name__ == '__main__':
  main()