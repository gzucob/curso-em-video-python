exp = str(input('Digite uma expressão: '))
aval = list()
for simb in exp:
    if simb == '(':
        aval.append('(')
    elif simb == ')':
        if len(aval) > 0:
            aval.pop()
        else:
            aval.append(')')
            break
if len(aval) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão é inválida!')

