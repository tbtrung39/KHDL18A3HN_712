# Bài 7
n = int(input("Nhập vào số nguyên dương n: "))
if n > 0:
  S = 0
  for i in range(1, n + 1):
    S += 1 / i
    print("Tổng nghịch đảo của", n, "số nguyên đầu tiên là:", round(S, 4))
else:
    print("Giá trị n không hợp lệ, vui lòng nhập lại!")