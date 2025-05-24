def doc_file(ten_file):
    with open(ten_file,'r') as file:
        data=file.read().split()
        return set(map(int,data))
def tim_so_chung():
    ds_m=doc_file('m_num.txt')
    ds_n=doc_file('n_num.txt')
    so_chung=sorted(ds_m and ds_n)
    with open('so_chung.txt','w') as file:
        file.write(''.join(map(str,so_chung)))
    with open('so_chung.txt','r') as file:
        print("Cac so chung la:", file.read())
tim_so_chung()