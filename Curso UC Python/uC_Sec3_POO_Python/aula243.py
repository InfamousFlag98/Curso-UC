from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('ABRINDO ARQUIVO')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print(f'Ocorreu erro: {e}')
    finally:
        print('FECHANDO ARQUIVO')
        arquivo.close()

with my_open('aula243.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)