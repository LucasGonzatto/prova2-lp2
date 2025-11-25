def ler_avaliacoes(arquivo):
    livros = []
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            partes = [p.strip() for p in linha.split(",")]
            if len(partes) == 5:
                ano, titulo, autor, nota, status = partes
                try:
                    nota = float(nota)
                    livros.append((ano, titulo, autor, nota, status.lower()))
                except ValueError:
                    pass
    return livros
def filtrar_livros(livros):
    return [l for l in livros if l[4] in ("lido", "lendo")]
def selecionar_top5melhores(livros):
    livros_ordenados = sorted(livros, key=lambda x: x[3], reverse=True)
    return livros_ordenados[:5]
def salvar_recomendacoes(livros, arquivo_saida):
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        for ano, titulo, autor, nota, status in livros:
            f.write(f"{ano}, {titulo}, {autor}, {nota}, {status}\n")
def main():
    livros = ler_avaliacoes("livros_avaliacao.txt")
    filtrados = filtrar_livros(livros)
    recomendados = selecionar_top5melhores(filtrados)
    salvar_recomendacoes(recomendados, "livros_recomendados.txt")
if __name__ == "__main__":
    main()
