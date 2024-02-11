katz_deli = []

def line(katz):
    if not katz:
        print("The line is currently empty.")
    else:
        string_list = []
        for index, person in enumerate(katz):
            string_list.append(f"{index + 1}. {person}")
        print(f'The line is currently: {" ".join(string_list)}')


def take_a_number(katz, name):
    katz.append(name)
    print(f'Welcome, {name}. You are number {len(katz)} in line.')

def now_serving(katz):
    if not katz:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz[0]}.')
        katz.pop(0)
