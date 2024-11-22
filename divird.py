import sys
import os

def dividir_texto_em_mensagens(texto, limite=1000):
    """
    Divide o texto em mensagens com no máximo 'limite' caracteres,
    respeitando os parágrafos para manter a coerência.
    """
    parágrafos = texto.split('\n\n')  # Considera parágrafo como separado por duas quebras de linha
    mensagens = []
    mensagem_atual = ''

    for parágrafo in parágrafos:
        # Adiciona duas quebras de linha para manter a separação de parágrafos
        parágrafo = parágrafo.strip()
        if not parágrafo:
            continue  # Ignora parágrafos vazios

        # Verifica se adicionando o próximo parágrafo excede o limite
        if len(mensagem_atual) + len(parágrafo) + 2 > limite:
            if mensagem_atual:
                mensagens.append(mensagem_atual.strip())
                mensagem_atual = ''
        
        # Se o parágrafo sozinho for maior que o limite, precisa ser dividido
        if len(parágrafo) > limite:
            if mensagem_atual:
                mensagens.append(mensagem_atual.strip())
                mensagem_atual = ''
            # Divide o parágrafo em pedaços menores
            inicio = 0
            while inicio < len(parágrafo):
                fim = inicio + limite
                pedaço = parágrafo[inicio:fim]
                mensagens.append(pedaço)
                inicio = fim
        else:
            # Adiciona o parágrafo à mensagem atual
            mensagem_atual += parágrafo + '\n\n'

    # Adiciona a última mensagem acumulada
    if mensagem_atual.strip():
        mensagens.append(mensagem_atual.strip())

    return mensagens

def processar_arquivo(caminho_arquivo):
    """
    Processa o arquivo de texto e divide seu conteúdo em mensagens.
    """
    if not os.path.isfile(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não existe.")
        sys.exit(1)

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        sys.exit(1)

    mensagens = dividir_texto_em_mensagens(conteudo)
    return mensagens

def main():
    if len(sys.argv) != 2:
        print("Uso: python dividir_instagram.py <caminho_para_arquivo.txt>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]
    mensagens = processar_arquivo(caminho_arquivo)

    print(f"Total de mensagens geradas: {len(mensagens)}\n")
    for idx, mensagem in enumerate(mensagens, 1):
        print(f"--- Mensagem {idx} ---")
        print(mensagem)
        print("\n")

if __name__ == "__main__":
    main()

