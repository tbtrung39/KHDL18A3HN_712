def Ucln(a, b): return abs(a) if not b else Ucln(b, a % b)
def Bcnn(a, b): return abs(a * b) // Ucln(a, b)
def SumDivisor(n): return sum(i for i in range(1, n + 1) if n % i == 0)
