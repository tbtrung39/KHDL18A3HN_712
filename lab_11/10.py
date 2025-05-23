import csv

def tinh_TL(tb, rl):
    return (tb + rl) / 2

def main():
    sv = []
    n = int(input("Số SV: "))
    for _ in range(n):
        ma = input("Mã SV: ")
        ten = input("Tên: ")
        tb = float(input("Điểm TB: "))
        rl = float(input("Điểm RL: "))
        tl = tinh_TL(tb, rl)
        sv.append([ma, ten, tb, rl, tl])

    sv.sort(key=lambda x: x[3])  # RL tăng dần

    with open("ds_sinhvien.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Mã", "Tên", "TB", "RL", "TL"])
        writer.writerows(sv)

    sv_max = max(sv, key=lambda x: x[4])
    print("SV có TL cao nhất:", sv_max)

if __name__ == "__main__":
    main()
