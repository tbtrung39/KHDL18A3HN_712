# cach 1
input_str = input("Nhap chuoi ky tu: ")
non_alnum_count = 0
for char in input_str:
    if not char.isalnum():  
        non_alnum_count += 1
print(f"So ky tu khong phai chu cai hoac so : {non_alnum_count}")
# cách 2
input_str = input("Nhap chuoi ky tu: ")
non_alnum_count = sum(1 for char in input_str if not char.isalnum())
print(f"So ky tu khong phai chu cai hoac so: {non_alnum_count}")
