# Tạo danh sách các số từ 0 đến 200 chia hết cho cả 5 và 7
so_hop_le = [x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0]
n = len(so_hop_le)
index = (n * 123456789) % n  
so_ngau_nhien = so_hop_le[index]
print("Số ngẫu nhiên chia hết cho 5 và 7 trong khoảng 0-200:", so_ngau_nhien)