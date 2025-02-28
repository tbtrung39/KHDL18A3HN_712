#Viết chương trình tìm số hoàn hảo nhỏ hơn nn
n=int(input("Nhập giá trị n"))
Tong=1
for i in range(2,n):
    uoc_chung=1
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            uoc_chung  += j + i//j
    if uoc_chung == i:
        print(i)