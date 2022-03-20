import random
import time

possibilities = [
    'pedra',
    'papel',
    'tesoura'
]

while True:
    time.sleep(3)
    cpu_awnser = random.choice(possibilities)

    print('\n\n\n\n\n\n\n\n\n\n=========================================')
    print('PEDRA, PAPEL ou TESOURA')
    print('=========================================')

    print('\n\nEscolha um valor:\n\n')
    print('=========================================')
    print('[1] PEDRA\n'
          '[2] PAPEL\n'
          '[3] TESOURA\n')
    print('=========================================')

    player_awnser = input(' • ')

    if player_awnser == '1':
        if cpu_awnser == 'pedra':
            print('[PEDRA] Empatamos.')
        if cpu_awnser == 'papel':
            print('[PAPEL] Você perdeu.')
        if cpu_awnser == 'tesoura':
            print('[TESOURA] Você ganhou')

    elif player_awnser == '2':
        if cpu_awnser == 'pedra':
            print('[PEDRA] Você ganhou.')
        if cpu_awnser == 'papel':
            print('[PAPEL] Empatamos.')
        if cpu_awnser == 'tesoura':
            print('[TESOURA] Você perdeu')

    elif player_awnser == '3':
        if cpu_awnser == 'pedra':
            print('[PEDRA] Você perdeu.')
        if cpu_awnser == 'papel':
            print('[PAPEL] Você ganhou.')
        if cpu_awnser == 'tesoura':
            print('[TESOURA] Empatamos.')

    else:
        print('Resposta inválida, tente novamente.')
