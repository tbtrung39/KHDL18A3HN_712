char_set = set()
print("Nhập từng ký tự (gõ 'ESC' để kết thúc):")
while True:
    ch = input("Nhập ký tự: ")
    if ch.upper() == "ESC":
        break
    if len(ch) == 1:
        char_set.add(ch)
    else:
        print("Chỉ được nhập 1 ký tự mỗi lần.")
char_set = {c for c in char_set if not c.isdigit()}
print("Tập hợp sau khi xóa ký tự số:", char_set)
