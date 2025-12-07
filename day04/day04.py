import argparse, time

def parse_input(f):
  return [[c for c in row.strip()] for row in f]

def adjacent_rolls(grid, x, y):
  count = 0

  to_check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  for xi, yi in to_check:
    if x + xi >= 0 and x + xi < len(grid[0]) and \
    y + yi >= 0 and y + yi < len(grid) and \
    grid[y+yi][x+xi] == "@":
      count += 1

  return count

def part_one(f) -> int:
  grid = parse_input(f)

  count = 0
  for y, row in enumerate(grid):
    for x, char in enumerate(row):
      if char != "@":
        continue
      if adjacent_rolls(grid, x, y) < 4:
        count += 1

  return count
      
def remove_rolls(grid) -> int:
  to_remove = []

  count = 0
  for y, row in enumerate(grid):
    for x, char in enumerate(row):
      if char != "@":
        continue
      if adjacent_rolls(grid, x, y) < 4:
        count += 1
        to_remove.append((x, y))

  for x, y in to_remove:
    grid[y][x] = "."

  return count

def part_two(f) -> int:
  grid = parse_input(f)
  count = 0

  while True:
    removed = remove_rolls(grid)
    count += removed
    if removed == 0:
      break

  return count


if __name__ == "__main__":  
  parser = argparse.ArgumentParser()
  parser.add_argument("parts", nargs="*")
  parser.add_argument("-t", "--test", action=argparse.BooleanOptionalAction)
  args = parser.parse_args()
  
  file_name = "input_test.txt" if args.test else "input.txt"
  f = open(file_name)
  
  run_pt_1 = not args.parts or "1" in args.parts
  run_pt_2 = not args.parts or "2" in args.parts
  
  if run_pt_1:
    start = time.perf_counter()
    pt_1_result = part_one(f)
    elapsed = (time.perf_counter() - start) * 1000 
    
    print("Part One:", pt_1_result, "(Ran in", round(elapsed, 8), "ms)")
  
  f.seek(0)
  
  if run_pt_2:
    start = time.perf_counter()
    pt_2_result = part_two(f)
    elapsed = (time.perf_counter() - start) * 1000 
    
    print("Part Two:", pt_2_result, "(Ran in", round(elapsed, 8), "ms)")
    
  f.close()