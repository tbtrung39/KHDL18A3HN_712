S1=input("Nhập chuỗi S1:")
S2=input("Nhập chuỗi S2:")
count_overlap=0
start=0
while True:
    start=S1.find(S2,start)
    if start == -1:
        break
    count_overlap +=1
    start += 1
count_non_overlap=0
start=0
while True:
    start=S1.find(S2,start)
    if start == -1:
        break
    count_non_overlap += 1
    start = start + len(S2)

if count_overlap == 0:
    print("Chuỗi S2 có nằm trong chuỗi S1")
else:
    print("Chuỗi S2 có nằm trong chuỗi S1")
    print("S2 xuất hiện trong S1 (có chồng lấn)",count_overlap,"lần")
    print("S2 xuất hiện trong S1 (không chồng lấn)",count_non_overlap,"lần")