try:
    source=input('nhap ten tap tin nguon:')
    dest=input('nhap ten tap tin dich:')
    with open(source,'r',encoding='utf-8')as f:
        content=f.read()
    with open(dest,'w',encoding='utf-8')as f2:
        f2.write(content)
    print('da ghi noi dung tu source sang dest thanh cong')
except FileNotFoundError:
    print('khong tim thay tap tin nguon')
except Exception as e:
    print('da xay ra loi',e)