import argparse, time, math

def valid(num):
  str_num = str(num)

  if len(str_num) % 2 != 0:
    return false

  return str_num[:len(str_num) // 2] == str_num[len(str_num) // 2:]

def parse_ranges(f):
  ranges = []
  data = f.read().split(",")
  for d in data:
    parts = d.split("-")
    ranges.append((int(parts[0]), int(parts[1])))
  
  return ranges

def invalid_count_one(low, high):
  count = 0
  for i in range(low, high+1):
    str_i = str(i)
    if len(str_i) % 2 == 1:
      continue

    if str_i[:len(str_i) // 2] == str_i[len(str_i) // 2:]:
      count += i

  return count


def part_one(f) -> int:
  ranges = parse_ranges(f)
  
  count = 0
  for a, b in ranges:
    count += invalid_count_one(a, b)
  return count


def invalid_two(n):
  str_n = str(n)
  for l in range(1, len(str_n) // 2+1):
    if len(str_n) % l != 0:
      continue

    seq = str_n[:l]
    to_repeat = len(str_n) // l
    if seq * to_repeat == str_n:
      return True

  return False

def part_two(f) -> int:
  ranges = parse_ranges(f)

  count = 0
  for a, b in ranges:
    for i in range(a, b+1):
      if invalid_two(i):
        count += i

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
