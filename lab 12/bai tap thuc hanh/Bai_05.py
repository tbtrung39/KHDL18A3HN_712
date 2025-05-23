def tong_s1(n):
    if n==1:
        return 1
    return n + tong_s1(n-1)

def tong_s2(n):
    if n==1: return 1
    return int(str(n)*n)+tong_s2(n-1)
try:
    n=int(input("Nhập n:"))
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
    print("S1=",tong_s1)
    print("S2=",tong_s2)
except ValueError as e:
    print(e)
except RecursionError as e:
    print(e)
except Exception as e:
    print(e)
    