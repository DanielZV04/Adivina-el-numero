import random

def play(numsecret, intentos):
    player = 0
    while player != numsecret:
        try:
            player = int(input('dime tu numero: '))
            if numsecret > player:
                print('El numero misterioso es mayor que tu numero.')
                intentos += 1
            elif numsecret < player:
                print('El numero misterioso es menor que tu numero.')
                print(numsecret)
                intentos += 1
        except ValueError:
            print('Dime un numero no una letra.')
    return intentos

def main():
    print('Bienvenido al juego de adivinar el numero misterioso!')
    level = {
        1: (1,10),
        2: (1,1000),
        3: (1,1500)
    }
    intentos = 0
    while True:
        nivel = input('Digame el numero de dificultad (1,2,3) o S para salir: ')
        if nivel == 'S':
            print('Saliste.')
            break
        nivel = int(nivel)
        
        if nivel in level:
            numsecret = random.randint(*level[nivel])
            intentos = play(numsecret, intentos)
            print(f'Felicidades!! El numero secreto era {numsecret}. Intentos {intentos}')
            break

if __name__ == '__main__':
    main()