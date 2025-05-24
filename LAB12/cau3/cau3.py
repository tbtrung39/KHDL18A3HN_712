try:
    n=input("Tên file:")
    with open(n,'r',encoding='utf-8') as f,open('copy.dat','w',encoding='utf-8') as g:
        g.write(f.read())
    print("Xong")
except FileNotFoundError:print("Ko tồn tại")
except Exception as e:print("Lỗi:",e)