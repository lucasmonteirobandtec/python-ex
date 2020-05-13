time = ('Athletico', 'Atlético-CO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 'Flamengo')

print('Os primeiros 5 colocados são: ')
for t in time[:5]:
    print(t)

print('Os 4 ultimos colocados são: ')
for t in time[:5:-1]:
    print(t)

print(sorted(time))

print(time.count('Chapecoense'))
