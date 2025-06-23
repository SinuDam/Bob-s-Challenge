# Author: Sinura Damsath Perera
# Problem: Bob's Challenge
# Language: Python 3

MOD = 10**9 + 7
MAX = 2 * 10**5 + 5

fact = [1] * MAX
inv_fact = [1] * MAX

def modinv(x):
    return pow(x, MOD - 2, MOD)

# Precompute factorials and inverse factorials
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD
inv_fact[MAX - 1] = modinv(fact[MAX - 1])
for i in range(MAX - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def nCk(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

# Process test cases
import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    ones = s.count(1)
    zeros = n - ones
    result = 0
    min_ones_needed = k // 2 + 1

    for ones_in_sub in range(min_ones_needed, min(k, ones) + 1):
        zeros_in_sub = k - ones_in_sub
        if zeros_in_sub > zeros:
            continue
        count = nCk(ones, ones_in_sub) * nCk(zeros, zeros_in_sub) % MOD
        result = (result + count) % MOD

    print(result)
