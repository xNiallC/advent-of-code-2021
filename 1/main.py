def main():
  with open('input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  # Part 1
  # print(len([line for index, line in enumerate([x.strip() for x in content]) if (index > 0 and (int(line) > int(content[index - 1])))]))

  # Part 2
  content = [int(value) for value in content]
  print(len([line for index, line in enumerate(content) if (index > 2 and (((content[index] + content[index - 1] + content[index - 2])) > (content[index - 1] + content[index - 2] + content[index - 3])))]))

  


if __name__ == '__main__':
  main()