try:
    f_in=open(input("nhap ten file can doc: "),'r',encoding='utf-8')
    f_out=open(input("nhap ten file de ghi: "),'w',encoding='utf-8')
    f_out.write(f_in.read())
    print("da sao chep thanh cong")
except FileNotFoundError:
    print("loi khong the tim thay ten nguon")
except IOError:
    print("loi: khong the doc ghi file")
finally: 
    try: f_in.close()
    except: pass
    try: f_out.close()
    except: pass
