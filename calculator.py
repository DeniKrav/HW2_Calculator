def main(x, op, y):
    if op == '+':
        print(addition(int(x),int(y)))
    if op == '*':
        print(multiplication(int(x),int(y)))
    if op == '-':
        print(subtraction(int(x),int(y)))
    if op == '/':
        if y != 0:
            print(division(int(x),int(y)))
        else:
            print('На ноль делить нельзя! Введите другое выражение')

main(*input().split())