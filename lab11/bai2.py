def sap_xep_day_so(input_file='Inp.txt', output_file='out.dat'):
    with open(input_file, 'r') as f:
        numbers = list(map(int, f.readline().strip().split()))
    numbers.sort()
    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, numbers)))
