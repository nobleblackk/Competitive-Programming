import sys 
sys.stdout = open("Recursion/../IO/output.txt", "w")
sys.stdin = open("Recursion/../IO/input.txt", "r")

n = int(input())
# Program to print power of 2 
def Power(n):
  # Unintentional Case 
  assert int(n) == n and n >= 0, "Number should be Positive Integer only"
  
  # Base Case
  if (n < 1):
    return 1  
  else: 
    return 2 * Power(n-1)

print(Power(n))
