def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()


print_n_times(3, 'Hello', 'Fun python', 'programming')

def print_n_times(value, n=2):
    for i in range(n):
        print(value)
    
print_n_times('안녕하세요', 5)

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times('Hello', 'Fun python', 'programming', 2)
print_n_times('Hello', 'Fun python', 'programming', n=2)