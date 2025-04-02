#Bai9
ds_so = [2, 4, 6, 8, 10]
for so in ds_so:
    assert so % 2 == 0, f"Số {so} không phải là số chẵn!"
print("Tất cả các số trong danh sách đều là số chẵn.")