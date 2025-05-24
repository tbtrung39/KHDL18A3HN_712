def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def la_doi_xung(n):
    return str(n) == str(n)[::-1]
def tim_so_ngto_doi_xung(vao, ra):
    with open(vao, 'r', encoding='utf-8') as f_in:
        data = f_in.read()
        ds_so = list(map(int, data.strip().split()))
    ket_qua = [x for x in ds_so if la_nguyen_to(x) and la_doi_xung(x)]
    with open(ra, 'w', encoding='utf-8') as f_out:
        f_out.write(str(len(ket_qua)) + '\n')
        f_out.write(' '.join(map(str, ket_qua)))
tim_so_ngto_doi_xung('f_in.dat', 'f_out.dat')