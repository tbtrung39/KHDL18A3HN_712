#Bai1
print("Nhập các ký tự (nhập 'ESC' để kết thúc): ")
tap_ky_tu = set()
while True:
    ky_tu = input("Nhập ký tự: ")
    if ky_tu == "ESC" or ky_tu == "esc": 
        break
    if len(ky_tu) == 1: 
        tap_ky_tu.add(ky_tu)
    else:
        print("Vui lòng chỉ nhập một ký tự!")
tap_ky_tu_moi = set()
for kt in tap_ky_tu:
    if not kt.isnumeric():
        tap_ky_tu_moi.add(kt)
tap_ky_tu = tap_ky_tu_moi
print("Tập hợp sau khi xoá các phần tử là ký tự số:", tap_ky_tu)