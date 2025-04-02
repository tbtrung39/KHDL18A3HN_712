import random
danh_sach_chia_het = [so for so in range(201) if so % 5 == 0 and so % 7 == 0]
print("Các số chia hết cho 5 và 7 trong khoảng từ 0 đến 200:", danh_sach_chia_het)
so_ngau_nhien = random.choice(danh_sach_chia_het)
print("Số ngẫu nhiên được chọn:", so_ngau_nhien)
