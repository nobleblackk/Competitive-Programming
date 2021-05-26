import sys 
sys.stdout = open("Recursion/../IO/output.txt", "w")
sys.stdin = open("Recursion/../IO/input.txt", "r")

n = int(input())

def factorial(n = 0):
  assert int(n) == n and n > 0, "Number should be positive"

  if (n < 2):
    return 1 
  return n * factorial(n-1)

print(factorial(n))
