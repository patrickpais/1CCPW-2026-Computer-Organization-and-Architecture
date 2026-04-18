#Atividade 1
def atividade_1():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    op_and = n1 & n2
    op_or = n1 | n2

    print(f'Os números são: {n1} e {n2}')
    print(f'O resultado da operação AND: {op_and} -> {op_and:08b}')
    print(f'O resultado da operação OR: {op_or} -> {op_or:08b}')
    print(f'O primeiro número em binário: {n1} -> {n1:08b}')
    print(f'O segundo número em binário: {n2} -> {n2:08b}')

atividade_1()

print("Vamos a atividade 2")

#Atividade 2
def atividade_2():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    print("\nEscolha uma opção:")
    print("1 - Operação AND")
    print("2 - Operação OR")

    opcao = input("Opção: ")

    if opcao == '1':
        resultado = num1 & num2
    elif opcao == '2':
        resultado = num1 | num2
    else:
        print("Opção inválida")
        return
    
    print(f"\nO resultado é: {resultado} e em binário {resultado:08b}")
atividade_2()