def la_nguyen_to(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def tim_uoc_so_nguyen_to(n):
    uoc_nt = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if la_nguyen_to(i):
                uoc_nt.add(i)
            j = n // i
            if la_nguyen_to(j):
                uoc_nt.add(j)
    if n > 1 and la_nguyen_to(n):
        uoc_nt.add(n)
    return sorted(uoc_nt)

def xu_ly_tep(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            n = int(line.strip())
            uoc_nt = tim_uoc_so_nguyen_to(n)
            f_out.write(' '.join(str(x) for x in uoc_nt) + '\n')

xu_ly_tep('input(4).dat','output(4).dat')
