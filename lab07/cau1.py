char_set = set()

while True:
    ch = input("Nhập một ký tự (gõ 'ESC' để kết thúc): ")
    if ch.upper() == 'ESC':
        break
    if len(ch) == 1:  
        char_set.add(ch)

char_set = {c for c in char_set if not c.isdigit()}

print("Tập hợp sau khi xóa ký tự số:", char_set)