#Bai6
def bcnn(a, b):
    max_ab = max(a, b)
    while True:
        if max_ab % a == 0 and max_ab % b == 0:
            return max_ab
        max_ab += 1
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("BCNN của", a, "và", b, "là:", bcnn(a, b))