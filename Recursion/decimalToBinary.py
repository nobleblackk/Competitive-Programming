import sys 
sys.stdout = open("Recursion/../IO/output.txt", "w")
sys.stdin = open("Recursion/../IO/input.txt", "r")

n = int(input())

def decimalToBinary(n, bin = ""):
  assert n >= 0 and int(n) == n, "Number must be postive and integer"
  if (n == 0):
    return bin[::-1]
  return decimalToBinary(n//2, bin+str(n%2))

# print(decimalToBinary(n))

# better approach 
# Formula => binary number: f(n) = n%2 + 10 * f(n//2) 

def decimalToBinaryEfficient(n):
  assert n >= 0 and int(n) == n, "Number must be positive and integer"
  if (n == 0):
    return 0 
  return ((n%2) + (10 * decimalToBinaryEfficient(n//2)))

print(decimalToBinaryEfficient(n))
