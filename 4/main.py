def create_boards(lines, index=0, current_board=[], boards=[]):
  if index == len(lines):
    return boards
  if (lines[index] == ''):
    boards.append(current_board)
    return create_boards(lines, index + 1, [], boards)
  else:
    current_board.append([int(item) for item in lines[index].split(' ') if item != ''])
    return create_boards(lines, index + 1, current_board, boards)

def get_match(drawn_number, starting_board):
  matched_board = []
  for line_index, line in enumerate(starting_board):
    new_line = []
    for number_index, number in enumerate(line):
      if number == int(drawn_number):
        new_line.append(True)
      else:
        new_line.append(number)
    matched_board.append(new_line)
  return matched_board

def has_won(drawn_number, matched_board):
  won_indicator = False
  for line in matched_board:
    if all(match==line[0] for match in line):
      won_indicator = True
  for column_index in range(len(matched_board)):
    column_numbers = []
    for line in matched_board:
      column_numbers.append(line[column_index])
    if all(match==column_numbers[0] for match in column_numbers):
      won_indicator = True
  return won_indicator

def calculate_winner(drawn_numbers, boards, index=0, winning_boards=[], last_winning_number=0):
  matched_boards = []
  if index == len(drawn_numbers):
    print(len(boards))
    print(len(winning_boards))
    print(winning_boards)
    return {
      'winning_boards': winning_boards,
      'last_winning_number': last_winning_number
    }
  number = int(drawn_numbers[index])
  for board in boards:
    matched_board = get_match(number, board)
    known_winner = has_won(number, matched_board)
    if known_winner:
      winning_boards.append(matched_board)
      last_winning_number = number
    else:
      matched_boards.append(matched_board)
  return calculate_winner(drawn_numbers, matched_boards, index + 1, winning_boards, last_winning_number)

def get_winning_sum(drawn_number, winning_board):
  total = 0
  for line in winning_board:
    for result in line:
      if result != True:
        total += result
  print(total)
  return total * int(drawn_number)

def main():
  with open('./input_test.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  drawn_numbers = content[0].split(',')
  boards = create_boards(content[2:])
  result = calculate_winner(drawn_numbers, boards)
  print(result)
  final_score = get_winning_sum(result['last_winning_number'], result['winning_boards'][-1])
  print(final_score)
    

if __name__ == '__main__':
  main()