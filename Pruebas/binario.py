def binario(num):

    if num == 0:
        return '0'
    binario = []
    es_negativo = False

    if num < 0:
        es_negativo = True
        num = abs(num) # ABS Function become negative number to positive
    while num > 0:
        residuo = num %2
        binario.append(str(residuo))
        num = num // 2
    binario_str = ''. join (reversed(binario)) # Join concatenates each number in one str reverse invert the list 

    if es_negativo: 
        binario_str = "-" + binario_str
    return binario_str # return final result
s = int (input('cuantas veces quiere preguntar numero'))
for i in range(s):
    n = int(input(f'[{i+1}]/{s} Ingrese un número: '))
    print(f"Binario: {binario(n)}")