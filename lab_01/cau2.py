tongtg=int(input("nhập tổng thời gian theo giây: "))
d=tongtg//86400 
h=(tongtg%86400)//3600 
m=((tongtg%86400)%3600)//60 
s=(((tongtg%86400)%3600)%60)
print(d,"ngày",h,"giờ",m,"phút",s,"giây")