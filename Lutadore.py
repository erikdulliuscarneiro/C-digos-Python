# Escreva um programa que leia o nome de um lutador e
# seu peso. Em seguida, informe a categoria a que pertence o lutador, conforme o quadro abaixo
# (note que o quadro foi criado para efeito deste exercício e não condiz com qualquer categoria
# de luta). A saída do programa deve exibir na tela uma frase com o padrão:
Nome = input("Digite seu nome:")
Peso = float(input("Digite seu Peso em Kg: "))
if Peso < 65:
    print("O lutador", Nome, "pesando", Peso, "Se encaixa na Categoria Pena")
elif Peso >=65 and Peso<72:
    print("O lutador", Nome, "pesando", Peso, "Se encaixa na Categoria leve")
elif Peso >=72 and Peso<79:
    print("O lutador", Nome, "pesando", Peso, "Se encaixa na Categoria Ligeiro")
elif Peso >=79 and Peso<86:
    print("O lutador", Nome, "pesando", Peso, "Se encaixa na Categoria Meio-Medio")
elif Peso >=86 and Peso<93:
    print("O lutador", Nome, "pesando", Peso, "Se encaixa na Categoria Medio")
elif Peso >=93 and Peso<100:
    print("O lutador", Nome, "pesando", Peso, "Se encaixa na Categoria Meio-Pesado")
else:
    print("O lutador", Nome, "pesando", Peso, "Se encaixa na Categoria Pesado")