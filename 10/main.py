opener_to_expected_map = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}
openers = opener_to_expected_map.keys()

illegal_to_points_map = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

completed_to_points_map = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

def main():
  with open('./input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  
  illegal_finds = []
  illegal_lines = []
  def find_illegal_characters(line, line_index):
    # As we trawl the line
    # If we encounter an chunk opener, we add it to our trawled characters
    # If we encounter a closing element, we verify if its valid
    # We then check if this was what we expected, by seeing if the character we popped, is equal to the closer tags value in expected_character_to_opener_map
    # If it is, we carry on, else we add the illegally found character to illegal finds, and return
    trawled_characters = []
    for index, character in enumerate(line):
      if character in openers:
        trawled_characters.append(character)
      else:
        previous_opener = trawled_characters.pop()
        expected_closer = opener_to_expected_map.get(previous_opener)
        if character != expected_closer:
          illegal_finds.append(character)
          illegal_lines.append(line_index)
          return

  for index, line in enumerate(content):
    find_illegal_characters(line, index)
  
  #summed_finds = sum([illegal_to_points_map[find] for find in illegal_finds])
  #print(summed_finds)

  def complete_line(line):
    # It's similair to before!
    # We know that whatever characters remain, have not been closed
    # Well we can just map them to the closing characters required, simple!
    trawled_characters = []
    completion_required = []
    for index, character in enumerate(line):
      if character in openers:
        trawled_characters.append(character)
      else:
        previous_opener = trawled_characters.pop()
    if len(trawled_characters) > 0:
      for incomplete in trawled_characters:
        completion_required.insert(0, opener_to_expected_map[incomplete])
    return completion_required

  completed_lines = []
  for index, line in enumerate(content):
    if index not in illegal_lines:
      completed_lines.append(complete_line(line))

  print(completed_lines)
  completed_scores = []
  for completed in completed_lines:
    score = 0
    for character in completed:
      score_for_char = completed_to_points_map[character]
      score = (score * 5)
      score += score_for_char
    completed_scores.append(score)

  sorted_scores = sorted(completed_scores)
  print(sorted_scores)
  print(len(sorted_scores))
  print(round(len(sorted_scores) / 2))

  middle_score = sorted_scores[round(len(sorted_scores) / 2)]
  print(sorted_scores[23])
  print(middle_score)

if __name__ == '__main__':
  main()