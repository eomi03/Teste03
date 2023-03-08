import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'advinhe um numero entre 1 and {x}:'))
        if guess < random_number:
            print(f'desculpe,advinhe novamente.Muito baixo.')
        elif guess > random_number:
            print(f'desculpe, advinhe novamente.Muito alto')
    
    print(f'UAU, parabéns. Você advinhou o numero {random_number} correto')


guess(10)        


