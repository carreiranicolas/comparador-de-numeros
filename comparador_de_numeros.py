while True:
    try:
        numero_1 = float(input("Digite um número: "))
        numero_2 = float(input("Digite outro número: "))

        if numero_1 > numero_2:
            print(f'{numero_1} é maior que {numero_2}')
        elif numero_1 < numero_2:
            print(f'{numero_1} é menor que {numero_2}')
        else:
            print("Os números são iguais.")
        break
    
    except:
         print("Por favor, digite apenas números")