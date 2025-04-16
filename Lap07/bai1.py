import msvcrt
 kytu_set=set()
 print("nhập các kí tự (Nhấn phim ESC để ket thúc): ")
 while True:
     kytu=msvcrt.getch().decode('utf-8')
     if kytu=='\x1b':
         print('kết thúc nhập')
         break
     if len(kytu) and kytu.isalpha():
         kytu_set.add(kytu)
 print("kết quả:", kytu_set)