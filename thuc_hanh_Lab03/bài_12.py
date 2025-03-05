container = input("Nhập số container: ")
bang_ma_hoa = {}
bang_ma_hoa['A'] = 10
bang_ma_hoa['B'] = 12
bang_ma_hoa['C'] = 13
bang_ma_hoa['D'] = 14
bang_ma_hoa['E'] = 15
bang_ma_hoa['F'] = 16
bang_ma_hoa['G'] = 17
bang_ma_hoa['H'] = 18
bang_ma_hoa['I'] = 19
bang_ma_hoa['J'] = 20
bang_ma_hoa['K'] = 21
bang_ma_hoa['L'] = 22
bang_ma_hoa['M'] = 23
bang_ma_hoa['N'] = 24
bang_ma_hoa['O'] = 25
bang_ma_hoa['P'] = 26
bang_ma_hoa['Q'] = 27
bang_ma_hoa['R'] = 28
bang_ma_hoa['S'] = 29
bang_ma_hoa['T'] = 30
bang_ma_hoa['U'] = 31
bang_ma_hoa['V'] = 32
bang_ma_hoa['W'] = 33
bang_ma_hoa['X'] = 34
bang_ma_hoa['Y'] = 35
bang_ma_hoa['Z'] = 36

S = 0
for i in range(4):
    S += bang_ma_hoa[container[i]] * (2 ** i)
for i in range(4, 10):
    S += int(container[i]) * (2 ** i)
so_kiem_tra = S % 11
print("Số kiểm tra của container là:", so_kiem_tra)