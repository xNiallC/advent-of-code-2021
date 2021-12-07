import time

def handle_progression(school):
  end_of_day_school = []
  for fish in school:
    # Fish has hit its birth time, reset to 6 and add another fish
    if fish['timer'] == 0:
      end_of_day_school.append({ 'timer': 6 })
      end_of_day_school.append({ 'timer': 8 })
    else:
      end_of_day_school.append({ 'timer': fish['timer'] - 1 })
  return end_of_day_school

def handle_days(initial_fish, days):
  if days == 0:
    return initial_fish
  else:
    updated_fish = handle_progression(initial_fish)
    return handle_days(updated_fish, days - 1)

default_day_tracker = {
  0: 0,
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
}

def create_day_tracker(school):
  day_tracker = {x:default_day_tracker[x] for x in default_day_tracker}
  for fish in school:
    day_tracker[fish['timer']] += 1
  return day_tracker

def handle_progression_2(day_tracker, day_counter):
  if day_counter == 0:
    return day_tracker
  else:
    new_day_tracker = {x:default_day_tracker[x] for x in default_day_tracker}
    # For each possible age of the fish, inversed. i.e. A fish at day 8 has a timer of 0, therefor the next day it will spawn a new one
    for day in range(9):
      # For a day 0 fish, they spawn a new one, therefore we remove all our day0s, add that number to our day6s, and add that number to our day8s
      if day == 0:
        fish_to_reset_and_spawn = day_tracker[0]
        new_day_tracker[8] += fish_to_reset_and_spawn
        new_day_tracker[6] += fish_to_reset_and_spawn
      else:
        fish_to_progress = day_tracker[day]
        new_day_tracker[day - 1] += fish_to_progress
    return handle_progression_2(new_day_tracker, day_counter - 1)

def get_total(final_progress):
  return sum(final_progress.values())

def main():
  with open('./input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  print(content)
  initial_fish_line = content[0].split(',')
  initial_fish = [{ 'timer': int(fish) } for fish in initial_fish_line]

  total_days = 256
  #finished_fish = handle_days(initial_fish, total_days)
  #print(finished_fish)
  #print(len(finished_fish))

  day_tracker = create_day_tracker(initial_fish)

  start_time = time.time()
  final_progress = handle_progression_2(day_tracker, total_days)
  print('Took ' + str(time.time() - start_time) + ' seconds')
  print(final_progress)
  print(get_total(final_progress))



if __name__ == '__main__':
  main()  