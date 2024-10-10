numero = 7
tentativas = 3
Qnt_tentativas = 0

while Qnt_tentativas < tentativas:
    advinhar = int(input(f'Tentativa {Qnt_tentativas + 1}/{tentativas}: Adivinhe o numero certo'))

    if advinhar == numero:
        print('Parabéns! voçe acertou!')
        break
    else:
        print('Tente Novamente.')

    Qnt_tentativas += 1
else:
    print(f'Voce teve {Qnt_tentativas} tentativas, o numeor era {numero}.')