import argparse, time
from typing import List

def parse_input(f) -> List[int]:
  result = []

  for row in f:
    direction = row[0]
    amt = int(row.strip()[1:])

    num = amt if direction == "R" else -amt
    result.append(num)

  return result


def part_one(f) -> int:
  parsed = parse_input(f)
  zero_count = 0

  pos = 50
  for n in parsed:
    pos += n
    pos %= 100
    if pos == 0:
      zero_count += 1

  return zero_count

def part_two(f) -> int:
  parsed = parse_input(f)
  zero_count = 0

  pos = 50
  for n in parsed:
    for _ in range(abs(n)):
      pos = pos + 1 if n > 0 else pos - 1
      pos %= 100
      if pos == 0:
        zero_count += 1

  return zero_count


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