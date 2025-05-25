with open(r'cau6\matrix.txt', 'w') as f:
    f.write("4\n")
    f.write("211 133 180 5\n")
    f.write("192 168 1 254\n")
    f.write("11 1 11 233\n")
with open(r'cau6\matrix.txt', 'r') as f:
    cac_dong = f.readlines()

#a. 
print("a. Noi dung dong 1: ", cac_dong[0].strip())
print("a. Noi dung dong 2: ", cac_dong[2].strip())

# b. 
print("\nb. Cac noi dung trong file trong matrix.txt:")
for dong in cac_dong:
    print(dong.strip())

# c.
matrix = []
for dong in cac_dong[1:]:
    hang = list(map(int, dong.strip().split()))
    hang_moi = [str(so) if so % 2 == 1 else '0' for so in hang]
    matrix.append(hang_moi)

with open(r'cau6\ODD.txt', 'w') as f_odd:
    for hang in matrix:
        f_odd.write(' '.join(hang) + '\n')
# d.
with open(r'cau6\ODD.txt', 'r') as f_odd:
    cac_dong_odd = f_odd.readlines()
    print("d. Noi dung dong cuoi: ", cac_dong[3].strip())