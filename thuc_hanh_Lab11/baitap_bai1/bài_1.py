import os
def tong_cac_so_hang_le(filename):
    tong = 0
    with open(filename, 'r') as f:
        for line in f:
            numbers = map(int, line.strip().split())
            tong += sum(n for n in numbers if n % 2 == 1)
    print("Tổng các số hàng lẻ trong dãy:", tong)
file_path = os.path.join("baitap_bai1", "dayso.dat")
tong_cac_so_hang_le(file_path)


