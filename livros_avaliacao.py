def ler_livros(arquivo):
    livros = []
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                partes = linha.split(",")
                ano = partes[0].strip()
                titulo = partes[1].strip()
                autor = partes[2].strip()
                livros.append((ano, titulo, autor))
    return livros
def solicitar_nota():
    while True:
        try:
            nota = float(input("Digite uma nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Deve ser entre 0 e 10. @-@ ")
        except ValueError:
            print("A entrada não é válida. Digite um número. ?-? ")
def solicitar_status():
    opcoes = ["lido", "lendo", "na fila"]
    while True:
        status = input("Digite o status sendo (lido / lendo / na fila): ").strip().lower()
        if status in opcoes:
            return status
        else:
            print("Status inválido, digite novamente.")
def salvar_avaliacoes(livros, arquivo_saida):
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        for ano, titulo, autor in livros:
            print(f"\nLivro: {titulo} ({ano}) - Autor: {autor}")
            nota = solicitar_nota()
            status = solicitar_status()
            f.write(f"{ano}, {titulo}, {autor}, {nota}, {status}\n")
def main():
    livros = ler_livros("livros.txt")
    salvar_avaliacoes(livros, "livros_avaliacao.txt")
if __name__ == "__main__":
    main()
