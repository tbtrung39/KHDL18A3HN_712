try:
    filename=input('nhap ten tap tin can doc')
    with open(filename,'r',encoding='utf-8')as f:
        content=f.read()
        print('noi dung tap tin')
        print(content)
    with open('copy.dat','w',encoding='utf-8')as f_copy:
        f_copy.write(content)
        print('da sao chep noi dung sang file copy.dat')
except FileNotFoundError:
    print('khong tim thay tap tin')
except Exception as e:
    print('loi:',e)