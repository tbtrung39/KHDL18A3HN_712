def doc_du_lieu():
    with open(r'cau9\PASSENGERS.IN', 'r') as f:
        n = int(f.readline().strip()) 
        data = []
        for _ in range(n):
            line = f.readline().strip()
            if line == '':
                data.append([])
            else:
                do_xach_tay = list(map(float, line.split()))
                data.append(do_xach_tay)
    return n, data


def ghi_weight(weights):
    with open(r'cau9\WEIGHT.OUT', 'w') as f:
        for w in weights:
            f.write(f"{w:.2f}\n")


def ghi_canceled(canceled_list):
    with open(r'cau9\CANCELED.OUT', 'w') as f:
        for stt in canceled_list:
            f.write(str(stt) + '\n')


def main():
    n, hanh_khach = doc_du_lieu()
    weights = []
    canceled = []

    for i, do_xach_tay in enumerate(hanh_khach, start=1):
        tong_trong_luong = sum(do_xach_tay)
        weights.append(tong_trong_luong)

        so_luong_do = len(do_xach_tay)

        if tong_trong_luong > 23:
            canceled.append(i)
        elif so_luong_do > 5:
            canceled.append(i)

    ghi_weight(weights)
    ghi_canceled(canceled)
    if canceled:
        print("Danh sach hanh khach bi huy chuyen:")
        for stt in canceled:
            
            tong_trong_luong = weights[stt - 1]
            so_luong_do = len(hanh_khach[stt - 1])
            ly_do = []
            if tong_trong_luong > 23:
                ly_do.append("tong trong luong vuot 23 kg")
            if so_luong_do > 5:
                ly_do.append("so luong do xach tay vuot 5")
            print(f"  Hanh khach so {stt}: {', '.join(ly_do)}")
    else:
        print("Khong co hanh khach nao bi huy chuyen.")


if __name__ == "__main__":
    main()