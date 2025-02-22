xa,ya=map(float,input("nhap toa do dinh A cua tam giac: ").split())
xb,yb=map(float,input("nhap toa do dinh B cua tam giac: ").split())
xc,yc=map(float,input("nhap toa do dinh C cua tam giac: ").split())
xg=(xa+xb+xc)/3
yg=(ya+yb+yc)/3
print(f"trong tam cua tam giac ABC la: G({xg:.2f},{yg:.2f})")
