def sao_chep_tap_tin(ten_tep):
    try:
        with open(ten_tep,'r',encoding='utf-8') as tep_goc:
            n_d=tep_goc.read()
        with open("copy.dat",'w',encoding='utf-8') as tep_moi:
            tep_moi.write(n_d)
        print("da sao chep noi dung sang file 'copy.dat' thanh cong")
    except FileNotFoundError:
        print(f"loi: khong tim thay tep tin co ten'{ten_tep}'.")
    except Exception as e:
        print(f"da xay ra loi:{e}")
    ten_file=input("nhap ten tep can doc: ")
    sao_chep_tap_tin(ten_file)
