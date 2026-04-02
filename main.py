from rag import responder
from voice_input import ouvir
from tts import falar

def main():
    while True:
        print("\n1 - Digitar pergunta")
        print("2 - Falar pergunta")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break

        elif opcao == "1":
            pergunta = input("\nDigite sua pergunta: ")

        elif opcao == "2":
            pergunta = ouvir()
            print("\nPergunta reconhecida: ", pergunta)

        else:
            print("Opção inválida. Tente novamente.")
            continue

        resposta = responder(pergunta)
        print("\nResposta:\n", resposta)

        falar(resposta)

if __name__ == "__main__":
    main()