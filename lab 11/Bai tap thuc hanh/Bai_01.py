def tinh_tong_le(filename='dayso.dat'):
    with open(filename, 'r') as f:
        numbers = []
        for line in f:
            numbers += map(int, line.strip().split())
    tong_le = sum(x for x in numbers if x % 2 == 1)
    print("Tổng các số lẻ là:", tong_le)