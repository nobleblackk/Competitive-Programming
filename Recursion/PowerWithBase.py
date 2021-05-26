import sys 
sys.stdout = open("Recursion/../IO/output.txt", "w")
sys.stdin = open("Recursion/../IO/input.txt", "r")

base, power = map(int, input().split())

def powerWithBase(base = 1, power = 0):
  assert (base > 0) and int(power) == power and power >= 0, "Number can not be Negative"
  if (power < 1):
    return 1 
  return base * powerWithBase(base, power-1)

print(powerWithBase(base, power))