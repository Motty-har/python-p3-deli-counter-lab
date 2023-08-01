katz_deli = []

def line(line):
    if len(line) == 0:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        i = 1
        for per in line:
            message += f' {i}. {per}'
            i += 1
        print(message)

def take_a_number(list, string):
    list.append(string)
    print(f'Welcome, {string}. You are number {len(list)} in line.')
    pass

def now_serving(list):
    if len(list) == 0:
        print("There is nobody waiting to be served!")
    else:
            print(f'Currently serving {list[0]}.')
            list.pop(0)
    pass

