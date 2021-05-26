import sys 
sys.stdout = open("Iteration/../IO/output.txt", "w")
sys.stdin = open("Iteration/../IO/input.txt", "r")

n = int(input())

# Program to print Power of 2 
def Power(n):
  assert int(n) == n and n >= 0, "Number should be positive"
  power = 1 
  i = 0 
  while i < n: 
    power *= 2 
    i += 1 
  return power 

print(Power(n))