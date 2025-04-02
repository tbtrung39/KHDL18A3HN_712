def pass_co_hieu_luc(password):
     hlower = hupper = hdigit = hspecial = False
     special_char = "$#@"
     if not (6 <= len(password) <= 12):
         return False
     for char in password:
         if char.islower():
             hlower = True
         elif char.isupper():
             hupper = True
         elif char.isdigit():
             hdigit = True
         elif char in special_char:
             hspecial = True
     return hlower and hupper and hdigit and hspecial
 password = input("Nhap cac mat khau, cach nhau boi dau ',': ").split(",")
 pw_co_hieu_luc = [p for p in password if pass_co_hieu_luc(p)]
 print(",".join(pw_co_hieu_luc))