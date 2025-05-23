def xu_ly_file(input_file, odd_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    
    n = int(lines[0])
    matrix_lines = lines[1:]
    
    print("Dòng đầu tiên của file:", lines[0])
    if len(lines) >= 3:
        print("Dòng thứ 3 của file:", lines[2])
    
    print("\nToàn bộ dữ liệu file:")
    for line in lines:
        print(line)
    
    matrix = [list(map(int, row.split())) for row in matrix_lines]
    
    odd_matrix = []
    odd_matrix.append([0]*len(matrix[0]))
    for row in matrix:
        odd_row = [x if x % 2 == 1 else 0 for x in row]
        odd_matrix.append(odd_row)
    
    with open(odd_file, 'w', encoding='utf-8') as f_out:
        for row in odd_matrix:
            f_out.write(' '.join(str(x) for x in row) + '\n')
    
    print("\nDòng cuối của file ODD.txt là:")
    print(' '.join(str(x) for x in odd_matrix[-1]))


xu_ly_file('bang_so.txt', 'ODD.txt')
