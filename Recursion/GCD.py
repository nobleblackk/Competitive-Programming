import sys 
sys.stdout = open("Recursion/../IO/output.txt", "w")
sys.stdin = open("Recursion/../IO/input.txt", "r")


n, m = map(int, input().split())

# GCD is the largest positive number that divides the numbers without a remainder 

def gcdUtil(n, m):
  if (n % m == 0):
    return m 
  return gcdUtil(m, n%m)

def gcd(n = 1, m = 1):
  assert n > 0 and m > 0 and int(n) == n and int(m) == m, "Numbers must be positive and integers"

  if (n > m):
    return gcdUtil(n,m)
  else: 
    return gcdUtil(m, n)

print(gcd(n, m))
