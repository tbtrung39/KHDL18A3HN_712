print("Nhập vào một tháng (1-12):", end=" ")
month = int(input())
while month < 1 or month > 12:
    print("Tháng không hợp lệ! Vui lòng nhập lại (1-12):", end=" ")
    month = int(input())
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
print("Tháng", month, "là", months[month - 1])
