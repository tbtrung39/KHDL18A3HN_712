import os
def doc_file_du_lieu(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines
def hien_thi_dong_dau_tien_va_thu_ba(lines):
    print("Dòng đầu tiên:", lines[0])
    print("Dòng thứ 3:", lines[2])
def hien_thi_toan_bo_file(lines):
    print("Toàn bộ nội dung file:")
    for line in lines:
        print(line)
def ghi_odd_file(lines, odd_path):
    with open(odd_path, 'w') as f:
        for line in lines:
            so = list(map(int, line.strip().split()))
            dong_odd = [str(num if num % 2 != 0 else 0) for num in so]
            f.write(' '.join(dong_odd) + '\n')
def in_dong_cuoi_odd_file(odd_path):
    with open(odd_path, 'r') as f:
        lines = f.readlines()
        print("Dòng cuối cùng của ODD.txt:", lines[-1].strip())
folder = "baitap_bai6"
os.makedirs(folder, exist_ok=True)
input_path = os.path.join(folder, "data.txt")
odd_path = os.path.join(folder, "ODD.txt")
du_lieu_mau = """211 133 180 5
192 168 1 254
11 1 11 233"""
with open(input_path, 'w') as f:
    f.write(du_lieu_mau)
lines = doc_file_du_lieu(input_path)

print("\n a) Dòng đầu và dòng 3 ")
hien_thi_dong_dau_tien_va_thu_ba(lines)

print("\n b) Toàn bộ nội dung file ")
hien_thi_toan_bo_file(lines)

print("\n c) Ghi file ODD.txt ")
ghi_odd_file(lines, odd_path)

print("\n d) Dòng cuối file ODD.txt ")
in_dong_cuoi_odd_file(odd_path)
