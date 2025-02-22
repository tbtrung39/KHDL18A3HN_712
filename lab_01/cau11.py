n=int(input("nhập vào số lần tung xúc xắc: "))
xs_khong=(215/216**n)
xs_co=1-xs_khong
print("xác suất tung",n,"lần 3 xúc xắt có ít nhất 1 lần cả ba ra 6 là: ",round(xs_co,2))
