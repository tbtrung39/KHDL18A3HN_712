try:
    path=input("Nhap duong dan den file can doc: ")
    with open("lab12\bai3\nd.txt","r") as f:
        nd=f.read()
    with open("copy.dat","w") as copy_f:
        copy_f.write(nd)
    print("da sao chep noi dung sang file 'copy.dat'")
except FileExistsError:
    print("khong tim thay file. ket thuc chuong trinh")