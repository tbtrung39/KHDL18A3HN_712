def xu_ly_hanh_khach(input_file='PASSENGERS.IN', weight_file='WEIGHT.OUT', cancel_file='CANCELED.OUT'):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    so_khach = int(lines[0].strip())
    danh_sach_hanh_khach = [list(map(float, line.strip().split())) for line in lines[1:]]

    canceled = []
    weights = []

    for i, hanh_ly in enumerate(danh_sach_hanh_khach):
        tong_kg = sum(hanh_ly)
        weights.append(tong_kg)
        qua_can = tong_kg > 23
        qua_so_kien = len(hanh_ly) > 5

        if qua_can or qua_so_kien:
            canceled.append(i + 1)

    # Ghi file trọng lượng
    with open(weight_file, 'w') as wf:
        for w in weights:
            wf.write(f"{w:.2f}\n")

    # Ghi file hủy
    with open(cancel_file, 'w') as cf:
        for so_thu_tu in canceled:
            cf.write(f"{so_thu_tu}\n")

    # In thông báo
    print("==> Các hành khách bị hủy chuyến:")
    for idx in canceled:
        hanh_ly = danh_sach_hanh_khach[idx - 1]
        print(f" - Hành khách số {idx}: {len(hanh_ly)} kiện, tổng {sum(hanh_ly):.2f} kg")
