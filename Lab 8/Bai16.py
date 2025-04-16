#Bai16
def list_so_chan():
    so_chan = []
    for i in range(1, 101):
        if i % 2 == 0:
            so_chan.append(i)
    print("Danh sach cac so chan tu 1 den 100 la:", so_chan)
list_so_chan()