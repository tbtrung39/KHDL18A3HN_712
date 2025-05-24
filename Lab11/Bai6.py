with open('Bangso.txt') as file:
    ma_tran=[list(map(int,line.strip().split())) for line in file if line.strip()]
#Cau a
print("Dong dau:", ma_tran[0])
print("Dong 3:", ma_tran[2])
#Cau b
tong=sum(sum(dong) for dong in ma_tran)
print("Tong:", tong)
#Cau c
with open('ODD.txt','w') as file:
    for dong in ma_tran:
        file.write(''.join(str(so) if so%2!=0 else "0" for so in dong)+"\n")
#Cau d
with open('ODD.txt') as file:
    lines=file.readlines()
    print("Dong cuoi cua ODD.txt la:", lines[-1].strip())