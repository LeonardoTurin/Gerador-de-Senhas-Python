import random
import string


def gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais):
    caracteres = ""

    if usar_maiusculas:
        caracteres += string.ascii_uppercase  # Letras maiúsculas
    if usar_minusculas:
        caracteres += string.ascii_lowercase  # Letras minúsculas
    if usar_numeros:
        caracteres += string.digits  # Números
    if usar_especiais:
        caracteres += string.punctuation  # Caracteres especiais

    if not caracteres:
        print("Erro: Nenhum tipo de caractere selecionado!")
        return None

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


def main():
    print("Bem-vindo ao Gerador de Senhas!")

    comprimento = int(input("Digite o comprimento da senha: "))
    usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
    usar_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    senha = gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais)

    if senha:
        print(f"Sua senha gerada é: {senha}")


if __name__ == "__main__":
    main()