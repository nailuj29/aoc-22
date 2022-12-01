def read(day, test=False):
    with open(f'day{day}{"_test" if test else ""}.dat', 'r') as file:
        return file.read()