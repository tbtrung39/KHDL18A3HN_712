W = input("Nhập chuỗi W: ")
d = {}
for i in range(len(W)):
    for j in range(i + 1, len(W) + 1):
        k = W[i:j]
        if k in d:
            continue  
        d[k] = W.count(k)

print("Từ điển chuỗi con:", d)
