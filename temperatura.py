def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Conversor de Temperatura")
    print("1: Celsius para Fahrenheit")
    print("2: Fahrenheit para Celsius")

    opcao = int(input("Escolha uma opção (1 ou 2): "))

    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é equivalente a {fahrenheit:.2f}°F")
    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F é equivalente a {celsius:.2f}°C")
    else:
        print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
