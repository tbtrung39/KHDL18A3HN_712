def tinh_tong_so_le(file_path):
    tong = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for dong in file:
            cac_so = dong.strip().split()
            for chuoi_so in cac_so:
                if chuoi_so.isdigit():
                    so = int(chuoi_so)
                    if so % 2 == 1:
                        tong += so
    print("Tổng các số lẻ trong dãy là:", tong)

tinh_tong_so_le('dayso.dat')
