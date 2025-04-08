# bai 1
tap_ktu = set()

print("Hãy nhập ký tự từ bàn phím và nhấn phím ESC để kết thúc nhập dữ liệu:")
while True:
    k_tu = input("Hãy nhập ký tự: ")
    if k_tu == "ESC":
        break

    if len(k_tu) != 1:
        print(" hãy nhập 1 ký tự")
        continue
    tap_ktu.add(k_tu)
tap_ktu = {k for k in tap_ktu if not k.isdigit()}
print("Tập hợp sau khi xóa các ký tự số là:")
print(tap_ktu)
