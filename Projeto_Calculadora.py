continuar = 's'

while continuar == 's':
    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    operacao = input('Digite a operacao: ')
    res = None

    match operacao:
        case '+':
            res = num1 + num2

        case '-':
            res = num1 - num2

        case '*':
            res = num1 * num2

        case '/':
            if num2 == 0:
                print('Nao e possivel dividir por 0')
            else:
                res = num1 / num2

        case '**':
            res = num1 ** num2

        case '%':
            if num2 == 0:
                print('Nao e possivel calcular o resto de 0')
            else:
                res = num1 % num2

        case _:
            print('Operacao invalida! Use +, -, *, /, ** ou %.')

    if res is not None:
        print(f'O resultado dessa operacao e {res}')

    continuar = input('Gostaria de continuar? (s/n): ').lower()