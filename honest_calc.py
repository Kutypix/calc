memory = 0.0

def is_one_digit(num):
    return True if num > -10 and num < 10 and num.is_integer() else False

def check(x_, y_, op_):
    msg = ''
    msg += " ... lazy" if is_one_digit(x_) and is_one_digit(y_) else ''
    msg += " ... very lazy" if (x_ == 1 or y_ == 2) and op_ == '*' else ''
    msg += " ... very, very lazy" if (x_ == 0 or y_ == 0) and (op_ in '*+=') else ''
    print("You are" + msg if msg != '' else '')

saving = ["Are you sure? It is only one digit! (y / n)\n",
          "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
          "Last chance! Do you really want to embarrass yourself? (y / n)\n"]
while True:
    print("Enter an equation")
    x, oper, y = input().split()
    try:
        x = memory if x == 'M' else float(x)
        y = memory if y == 'M' else float(y)
        if oper in "+-*/":
            check(x, y, oper)
            if oper == '+':
                result = (float(x + y))
            elif oper == '-':
                result = (float(x - y))
            elif oper == '*':
                result = (float(x * y))
            elif oper == '/':
                result = (float(x / y))
            print(result)
            answer = ' '
            while answer not in 'yn':
                answer = input("Do you want to store the result? (y / n):\n")
                if answer == 'y':
                    id = 0
                    if is_one_digit(result):
                        while id < 3:
                            answer = input(saving[id])
                            if answer == 'y':
                                id += 1
                                if id == 3:
                                    memory = result
                            elif answer == 'n':
                                break
                    else:
                        memory = result
            answer = ' '
            while answer not in 'yn':
                answer = input("Do you want to continue calculations? (y / n):\n")
            if answer == 'n':
                break
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")

"""
msg_ = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move..."]
opers_ = ["+", "-", "*", "/"]

def _input_():
    while True:
        print(msg_[0])
        calc = input().split()
        try:
            x = float(calc[0]) if '.' in calc[0] else int(calc[0])
            y = float(calc[-1]) if '.' in calc[-1] else int(calc[-1])
            oper = calc[1]
        except ValueError:
            print(msg_[1])
        else:
            if oper not in opers_:
                print(msg_[2])
            else:
                break
    return x, oper, y
#print(type(x), type(oper), type(y))

x, oper, y = _input_()

def _opers_(x, oper, y):
    if oper == '+':
        result = float(x + y)
    elif oper == '-':
        result = float(x - y)
    elif oper == '*':
        result = float(x * y)
    elif oper == '/':
        try:
            result = float(x / y)
        except ZeroDivisionError:
            print(msg_[3])
            x, oper, y = _input_()
            result = _opers_(x, oper, y)
    return result

result = _opers_(x, oper, y)
print(result)
"""