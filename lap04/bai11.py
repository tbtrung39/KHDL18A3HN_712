menu = {
    1: "Cafe",
    2: "Cam vắt",
    3: "Nước ép cà rốt",
    4: "Nước lọc",
    5: "Nước dừa"
}
print("===== MENU ĐỒ UỐNG =====")
for key, value in menu.items():
    print(f"{key}. {value}")
while True:
    try:
        choice = int(input("Nhập số tương ứng với đồ uống bạn muốn gọi (1-5): "))
        if choice in menu:
            print(f"Bạn đã chọn: {menu[choice]}")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 5.")
    except ValueError:
        print("Vui lòng nhập một số hợp lệ!")