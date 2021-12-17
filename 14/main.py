

def part_1(content):
  polymer_template = [letter for letter in content[0]]
  polymer_rules = [(rule.split(' -> ')[0], rule.split(' -> ')[1]) for rule in content[2:]]

  print(polymer_template)
  print(polymer_rules)

  # We start by iterating for N steps
  n_steps = 40
  # For each step, we iterate over the existing polymer_template, starting at index 1
  previous_step_template = polymer_template[:]
  current_step_template = []
  for step in range(n_steps):
    for index, item in enumerate(previous_step_template):
      # Add item to current step template
      # If at index 0, no pair is needed, continue loop
      if index != 0:
        # Else we get current pair, which is current item, and item at the previous index
        current_pair = previous_step_template[index-1] + item
        for rule in polymer_rules:
          if rule[0] == current_pair:
            current_step_template.append(rule[1])
      current_step_template.append(item)
      
    previous_step_template = current_step_template[:]
    current_step_template = []

  print(''.join(previous_step_template))

  most_common_item = max(set(previous_step_template), key=previous_step_template.count)
  least_common_item = min(set(previous_step_template), key=previous_step_template.count)

  print('Most common: ' + most_common_item)
  print('Least common: ' + least_common_item)
  print('Most common: ' + str(len([item for item in listified_characters if item == most_common_item])))
  print('Most - least = ' + str(len([item for item in listified_characters if item == most_common_item]) - len([item for item in listified_characters if item == least_common_item])))

def part_2(content):
  polymer_template = [letter for letter in content[0]]
  polymer_rules = [(rule.split(' -> ')[0], rule.split(' -> ')[1]) for rule in content[2:]]

  print(polymer_template)
  print(polymer_rules)

  n_steps = 201

  # Make dict of every pair

  def make_pairs(template):
    pairs = {}
    for index, item in enumerate(template):
      if index != 0:
        pair = template[index-1] + item
        if pair not in pairs:
          pairs[pair] = 1
        else:
          pairs[pair] += 1
    return pairs

  pairs = make_pairs(polymer_template)

  def make_insertions(rules, template):
    updated_template = template.copy()
    for pair_index, existing_pair in enumerate(template.keys()):
      for rule in rules:
        rule_pair = rule[0]
        rule_insertion = rule[1]
        if rule_pair == existing_pair:
          # If we find a match, then we need to insert between the values in the pair
          # What this does is GET RID of the existing pair, as its not a pair anymore! So do -1 to that
          # It creates two NEW pairs - One on either side of the insertion
          new_pair_before = existing_pair[0] + rule_insertion
          new_pair_after = rule_insertion + existing_pair[1]
          if new_pair_before in updated_template:
            updated_template[new_pair_before] += 1
          else:
            updated_template[new_pair_before] = 1
          
          if new_pair_after in updated_template:
            updated_template[new_pair_after] += 1
          else:
            updated_template[new_pair_after] = 1

          updated_template[existing_pair] -= 1
          if updated_template[existing_pair] == 0:
            updated_template.pop(existing_pair)
          print('Current template: ' + str(template))
          print('Matched ' + rule_pair + ', inserted ' + new_pair_before + ' and ' + new_pair_after)
          print(updated_template)
    print('Finished step')
    print(updated_template)
    return updated_template

  curr_pairs = pairs.copy()
  for step in range(n_steps):
    new_pairs = make_insertions(polymer_rules, curr_pairs)
    curr_pairs = new_pairs.copy()

  def make_string(pairs):
    new_string = ''
    for pair, amount in pairs.items():
      if amount > 0:
        new_string += (pair * amount)
    return new_string

  all_characters = make_string(curr_pairs)
  listified_characters = [item for item in all_characters]

  most_common_item = max(set(listified_characters), key=listified_characters.count)
  least_common_item = min(set(listified_characters), key=listified_characters.count)

  print(all_characters)
  print('Most common: ' + most_common_item)
  print('Least common: ' + least_common_item)
  print('Most common: ' + str(len([item for item in listified_characters if item == most_common_item])))
  print('Most - least = ' + str(len([item for item in listified_characters if item == most_common_item]) - len([item for item in listified_characters if item == least_common_item])))
  test_string = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
  for key, value in curr_pairs.items():
    print(key)
    print(test_string.count(key))
    print(value)
    print('----')

def main():
  with open('./input_test.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  #part_1(content)
  part_2(content)

if __name__ == '__main__':
  main()