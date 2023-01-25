def get_data(file_name,enc="utf-8",divisor=";"):
    return [e.strip().split(divisor) for e in open(file_name,encoding=enc)]

def print_data(data):
    for d in data:
        print(d)