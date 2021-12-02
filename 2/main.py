def main():
  with open('./input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  movement_values = { 'x': 0, 'y': 0, 'aim': 0 }
  for command in content:
    direction, amount = command.split()
    if direction == 'forward':
      movement_values['x'] += int(amount)
      movement_values['y'] += (int(amount) * -int(movement_values['aim']))
    else: 
      movement_values['aim'] += (int(amount) if direction == 'up' else -int(amount))

  print(movement_values['x'] * movement_values['y'])
  print(movement_values)

if __name__ == '__main__':
  main()