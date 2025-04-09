char_set = set()
while True:
    ch = input("Nhập 1 ký tự (hoặc gõ ESC để kết thúc): ")
    if ch == 'ESC':
        break
    if len(ch) > 0:
        char_set.add(ch[0])  
char_set = {c for c in char_set if not c.isdigit()}
print("Tập hợp sau khi xóa ký tự số:", char_set)
