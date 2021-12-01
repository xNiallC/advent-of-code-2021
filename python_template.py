def main():
  with open('input.txt') as f:
    content = f.readlines()
  content = [x.strip() for x in content]

if __name__ == '__main__':
  main()