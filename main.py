import os
from collections import Counter
os.system("cls")
inutil = ["a", "e", "ou", "em", "com", "assim", "de", "da", "do", "dos", "das"]

while True:
    esc = input("""
    0 - Sair
    1 - Adicionar novo comentário
    2 - Gerar mapa de palavras
    """)

    try:
        match int(esc):
            case 0:
                break

            case 1:
                with open("sujo.txt", "a+", encoding="utf-8") as arq:
                    coment = input("Digite seu comentário: ")
                    arq.write("\n" + coment)

            case 2:
                #Filtrando lista
                sujo = open("sujo.txt", "r", encoding="utf-8")
                limpo = open("limpo.txt", "w+", encoding="utf-8")

                comentLimpo = []
                for linha in sujo.readlines():
                    palavras = linha.split()
                    palavras_filtradas = [palavra for palavra in palavras if palavra.lower() not in inutil]
                    comentLimpo.append(" ".join(palavras_filtradas))

                for linha in comentLimpo:
                    limpo.write(linha + "\n")

                limpo.seek(0)
                print(limpo.read())

                limpo.close()
                sujo.close()

                #Mapa de palavras
                with open("limpo.txt", "r", encoding="utf-8") as limpo:
                    listaPal = (limpo.read()).split()
                    cont = Counter(listaPal)
                    comum = cont.most_common(5)
                    for p,f in comum:
                        print(f"Palavra: {p} | Quantidade: {f}")

            case _:
                print("Opção inválida.")
    except ValueError:
        print("Opção inválida")

