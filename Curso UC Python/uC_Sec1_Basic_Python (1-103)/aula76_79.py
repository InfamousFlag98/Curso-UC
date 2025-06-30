"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
secreta = 'australopithecus'
tentativas = 0
letras_acertadas = ''
while True:
    letra = input('Digite uma letra: ')
    tentativas += 1
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    if letra in secreta:
        letras_acertadas += letra
        print(f'Você acertou a letra: {letra}')
    else:
        print('*')
    
    # Exibir letras acertadas
    for letra_secreta in secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta, end=' ')
        else:
            print('_', end=' ')
    
    print()  # Nova linha após exibir as letras
    
    # Verificar se todas as letras foram acertadas
    if all(letra in letras_acertadas for letra in secreta):
        print(f'Parabéns! Você adivinhou a palavra secreta "{secreta}" em {tentativas} tentativas.')
        break