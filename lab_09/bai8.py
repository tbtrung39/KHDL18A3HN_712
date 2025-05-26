import math
def bai_a(n):
    if n==1: return 1/(1*2)
    return 1/(n*(n+1))+bai_a(n-1)
def giaithua(n):
    return 1 if n==0 else n*giaithua(n-1)
def bai_b(n):
    if n==0: return 0
    return 1/giaithua(n)+bai_b(n-1)
def bai_c(n):
    return math.sqrt(3*n+(bai_c(n-1) if n else 9+math.sqrt(6+math.sqrt(3))))
def bai_d(n, k=None):
    if k is None: k=n+1
    if k==n-1:
        return (2+1)**(1/n)
    if k>n:
        return (n+bai_d(n,n))**(1/(n+1))
    if k==n:
        return (n-1+bai_d(n,k-1))**(1/n)
    return (n-k+bai_d(n,k+1))**(1/n)
print("Chọn bài (a, b, c, d):")
bai=input().strip().lower()
n=int(input("Nhập n: "))
if bai=='a':
    print(f"Kết quả bài a: {bai_a(n)}")
elif bai=='b':
    print(f"Kết quả bài b: {bai_b(n)}")
elif bai=='c':
    print(f"Kết quả bài c: {bai_c(n):.4f}")
elif bai=='d':
    print(f"Kết quả bài d: {bai_d(n)}")
else:
    print("Lựa chọn không hợp lệ!")