import random

balance = 1000

def try_to_guess_num():         #доработать овтеты
    global balance
    try:
        number_choice = int(input('Выберите число от 1 до 36: '))
        while True:       
            stavka = int(input(f"Выберите сумму ставки от 1 до {balance}: "))
            number = random.randint(1, 36)
            print(f'Выпало число: {number}')
            if number_choice == number:
                balance += stavka*36
            else:
                balance -= stavka
            if balance > 0:
                answer = input(f'Ваш баланс: {balance} рублей. Продолжить? "Да или Нет": ').lower()
            else:
                print(f'Вы проиграли( Ваш баланс после игры: {balance} рублей')
            if answer == 'нет':
                break
            number_choice = int(input('Выберите число от 1 до 36: '))

    except ValueError:
        print("Это не число попробуйте еще раз")

def try_to_guess_sector():      #доработать овтеты
    global balance
    sector_random = {i: [i for i in range(1, 19)] for i in range(1,2)}
    sec2 = {i: [i for i in range(19, 37)] for i in range(2,3)}
    sector_random.update(sec2)
    try:
        while True:
            stavka = int(input(f"Выберите сумму ставки от 1 до {balance}: "))
            sector_guess_player = int(input('Выберите сектор: числа от 1 до 18 - 1 сектор, от 19 до 36 - 2 сектор: '))
            random_number = random.randint(1, 36)
            print(f'Выпало число: {random_number}')
            if random_number in sector_random[sector_guess_player]:
                balance += stavka
            else:
                balance -= stavka
            question = input(f'Ваш баланс: {balance} рублей. Продолжить? "Да или Нет": ').lower()
            if question == 'да':
                continue
            else:
                print(f'Игра окончена! Ваш баланс: {balance}')

    except KeyError:
        print('Такого сектора нет')

if __name__ == '__main__':
    print(__name__)