def input_data():
    file_in = 'input.txt'
    with open(file_in, 'r') as f:
        n = int(f.readline().strip())
        k = int(f.readline().strip())
        array = list(int(_) for _ in f.readline().strip().split())
    return n, k, array

