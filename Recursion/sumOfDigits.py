import sys 
sys.stdout = open("Recursion/../IO/output.txt", "w")
sys.stdin = open("Recursion/../IO/input.txt", "r")

n = int(input())

def sumOfDigits(n = 0):
    # Constraints
    assert int(n) == n and n >= 0, "Number must be positive"
    if (n < 10):
      return n 
    return ((n%10) + sumOfDigits(n//10))

print(sumOfDigits(n))

