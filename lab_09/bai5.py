def permutation(n):
    if n==1: return [[1]]
    return [p[:i]+[n]+p[i:] for p in permutation(n-1) for i in range(n)]

n=int(input("Nhập số tự nhiên n: "))
print(", ".join(str([p]) for p in permutation(n)))