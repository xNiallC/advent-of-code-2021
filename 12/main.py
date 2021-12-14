

def main():
  with open('./input.txt') as f:
    content = f.readlines()
  content = [x.strip().split('-') for x in content]
  rooms = {}
  # Convert content into object
  for line in content:
    for subroom in line:
      if subroom not in rooms:
        rooms[subroom] = []
  
  # For each room, find it's adjacent rooms
  for room in rooms:
    for path in content:
      # Each path has two items
      # We need to seek both of them
      start_p = path[0]
      end_p = path[1]
      if end_p not in rooms[start_p]:
        rooms[start_p].append(end_p)
      if start_p not in rooms[end_p]:
        rooms[end_p].append(start_p)
  
  # Starting from "start"
  # Visit each branching path
  # At every possible branching point, we traverse each one, recording where we have been
  # If we reach a dead end: i.e. the only possible adjacent is a small room, and we have already been there, we just exit. Failed
  # If we reach the end, we recor the visit
  visited = []
  paths_visited = []

  def find_end(room_currently_in, visited=[]):
    visited = visited[:]
    visited.append(room_currently_in)
    if room_currently_in == 'end':
      #print('Reached end with ' + str(visited))
      paths_visited.append(visited)
    else:
      possible_options = rooms[room_currently_in]
      # Part 1 We can only go to big rooms, or small rooms we HAVEN'T visited
      #possible_options = [option for option in possible_options if (option.isupper() or (option not in visited))]

      # Part 2
      # - We can visit big rooms infinite times
      # - We get one oppurtunity to visit a small cave twice, as long as it's not the start or the end
      final_possible_options = []
      for option in possible_options:
        if option.isupper():
          final_possible_options.append(option)
        elif (option == 'end') or (option == 'start'):
          if option not in visited:
            final_possible_options.append(option)
        else:
          if (option not in visited):
            final_possible_options.append(option)
          else:
            # If we condense our visited list to JUST lowercase
            # If there are any duplicates
            # WE MUSTNT GO!
            lower_visited = [item for item in visited if not item.isupper()]
            if len(lower_visited) == len(set(lower_visited)):
              final_possible_options.append(option)

      #print('Currently in ' + room_currently_in)
      #print('Visited ' + str(visited))
      #print(final_possible_options)
      #print('-')
      for option in final_possible_options:
        find_end(option, visited)

  find_end('start')
  for path in paths_visited:
    print(path)
  print(len(paths_visited))

if __name__ == '__main__':
  main()