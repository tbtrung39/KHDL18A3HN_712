#a
def tinh_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tinh_a(n - 1)

print("Kết quả biểu thức a):", tinh_a(5))
#b
def giai_thua(n):
    if n == 1:
        return 1
    return n * giai_thua(n - 1)

def tinh_b(n):
    if n == 1:
        return 1
    return 1 / giai_thua(n) + tinh_b(n - 1)

print("Kết quả biểu thức b):", tinh_b(5))
