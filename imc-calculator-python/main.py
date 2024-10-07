# Calculadora de "Indice de Massa Corporal" em python
# Formula base: IMC = PESO / (ALTURA * ALTURA)

while True:
    try:
        peso = float(input("Qual o seu peso em kg? ").replace(',', '.'))
        if peso <= 0:
            raise ValueError("O peso deve ser maior que zero")
        altura = float(input("Qual sua altura em metros? ").replace(',', '.'))
        if altura <= 0:
            raise ValueError("A altura deve ser maior que zero")
        
        imc = peso / (altura ** 2)
        classificacao = ("abaixo do peso" if imc < 18.5 else "com peso normal" if imc < 24.9 else "com sobrepeso" if imc < 29.9 else "com obesidade")
        print(f"Seu IMC é {imc:.2f} e você está atualmente {classificacao}.")
        break
    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira valores válidos.")