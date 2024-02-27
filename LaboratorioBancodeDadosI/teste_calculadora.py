import calculadora
def main():
    a = 2
    b = 3

    soma = calculadora.somar(a,b)
    subtracao = calculadora.subtrair(a,b)
    multiplicar = calculadora.multiplicar(a, b)
    divisao = calculadora.dividir(a, b)
    
    print(f'{a} + {b}= {soma}')
    print(f'{a} - {b}= {subtracao}')
    print(f'{a} * {b}= {multiplicar}')
    print(f'{a} / {b}= {divisao}')
main()
