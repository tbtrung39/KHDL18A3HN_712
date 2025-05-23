def sao_chep_file():
    try:
        ten_tap_tin_nguon = input("Nhập tên tập tin nguồn cần đọc: ")
        file_nguon = open(ten_tap_tin_nguon, 'r', encoding='utf-8')  
        
        ten_tap_tin_dich = input("Nhập tên tập tin mới để ghi vào: ")
        file_dich = open(ten_tap_tin_dich, 'w', encoding='utf-8')    
        
        noi_dung = file_nguon.read()
        file_dich.write(noi_dung)

        print(f"Sao chép thành công vào tập tin: {ten_tap_tin_dich}")
    
    except FileNotFoundError:
        print("Lỗi:")
    except IOError as e:
        print("Lỗi:", e)
    except Exception as e:
        print("Lỗi:", e)
    finally:
        try:
            file_nguon.close()
        except:
            pass
        try:
            file_dich.close()
        except:
            pass

sao_chep_file()
