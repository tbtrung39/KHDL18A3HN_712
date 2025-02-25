kW = int(input('Nhập số KW điện tiêu thụ: '))
if kW <= 100:
    tien_dien = kW * 2000
elif kW <= 200:
    tien_dien = 100 * 2000 + (kW - 100) * 2500
elif kW <= 300:
    tien_dien = 100 * 2000 + 100 * 2500 + (kW - 200) * 3000
else:
    tien_dien = 100 * 2000 + 100 * 2500 + 100 * 3000 + (kW - 300) * 5000
print(f'Tiền điện phải trả: {tien_dien:,.0f} đồng')