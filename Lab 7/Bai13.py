#Bai13
w = input("Nhập chuỗi: ")
dictionary = {}
for i in range(len(w)):
    for j in range(i + 1, len(w) + 1):
        chuoi_con = w[i:j]
        if chuoi_con in dictionary:
            dictionary[chuoi_con] += 1
        else:
            dictionary[chuoi_con] = 1
print("Chuỗi con và số lần xuất hiện trong W là:")
for k, v in dictionary.items():
    print(k,":",v)