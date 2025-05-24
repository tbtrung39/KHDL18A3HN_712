with open('nhapso.txt', 'w') as f:
    f.write("4\n")
    f.write("211 133 180 5\n")
    f.write("192 168 1 254\n")
    f.write("11 1 11 233\n")
with open('nhapso.txt', 'r') as f:
    cac_dong = f.readlines()

# a. 
print("a. Noi dung dong dau tien:", cac_dong[0].strip())
print("a. Noi dung dong 3:", cac_dong[2].strip())

# b. 
print("\nb. Noi dung toan bo file nhapso.txt:")
for dong in cac_dong:
    print(dong.strip())

# c.
matrix = []
for dong in cac_dong[1:]:
    hang = list(map(int, dong.strip().split()))
    hang_moi = [str(so) if so % 2 == 1 else '0' for so in hang]
    matrix.append(hang_moi)
    
with open('ODD.txt', 'w') as f_odd:
    for hang in matrix:
        f_odd.write(' '.join(hang) + '\n')
# d.
with open('ODD.txt', 'r') as f_odd:
    cac_dong_odd = f_odd.readlines()
    print("\nd. dong cuoi cung cua ODD.txt la:", cac_dong_odd[-1].strip())