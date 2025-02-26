print("Nhập vào một số từ 1 đến 7 để xác định thứ trong tuần:")
while True:
    print("Nhập thứ (1-7):", end=" ")
    thu = int(input())
    if 1 <= thu <= 7:
        break
    print("Giá trị không hợp lệ, vui lòng nhập lại!")
ten_thu = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("Thứ", thu, "là", ten_thu[thu - 1])
