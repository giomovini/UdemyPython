#usada para exibir coisas na tela
print(12, 34, 1011, sep="-", end='##')
print(56, 78, sep='=', end='%\n')

# \r\n (CRLF) -> quebra de linha, MACOS só é necessario \n(LF)
print(1, 2, 3, sep='-', end='\n')

"""TESTE 1"""
# alternativa A
print('A Explicito', 'é', 'melhor-que-implicito.', sep='-')
print('A Simples', 'é', 'melhor-que-complexo', sep='-')

# alternativa B
print('B Explicito', 'é', 'melhor-que-implicito.', end='-')
print('B Simples', 'é', 'melhor-que-complexo', end='-')

# alternativa C
print('C Explicito', 'é', 'melhor-que-implicito.')
print('C Simples', 'é', 'melhor-que-complexo')

