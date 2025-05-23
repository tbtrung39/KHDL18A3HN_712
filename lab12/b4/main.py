try:
    with open("lab12\bai4\f_in.txt","r") as f:
        nd=f.read()
except FileNotFoundError:
    print("khong tim thay tap tin can doc")
    exit()
try: 
    with open("f_out.dat","w") as file:
        file.write(nd)
    print("da ghi noi dung vao file 'f_out.dat'")
except IOError:
    print("loi khi mo file 'f_out.dat' o che do ghi")
    exit()
except Exception as e:
    print("da xay ra loi",e)