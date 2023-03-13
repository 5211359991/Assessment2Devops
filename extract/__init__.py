def get_input(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip().split(','))

    return data