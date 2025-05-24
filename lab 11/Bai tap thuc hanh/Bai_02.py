def sap_xep_file(inp_file, out_file):
    try:
        with open(inp_file, 'r') as f:
            dong = f.readline().strip()
            cac_so = list(map(int, dong.split()))
            cac_so.sort()

        with open(out_file, 'w') as f_out:
            f_out.write(' '.join(map(str, cac_so)))

        print(f"Đã ghi dãy sắp xếp vào file {out_file}")

    except FileNotFoundError:
        print("Không tìm thấy file đầu vào.")
    except ValueError:
        print("File chứa dữ liệu không hợp lệ (phải là số nguyên).")

sap_xep_file('Inp.txt', 'Out.dat')
