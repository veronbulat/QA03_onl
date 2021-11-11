# Пользователь делает вклад в размере 'a' рублей сроком на 'years' лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме
# вклада, и на них в следующем году тоже будут проценты).
# функция bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя


def bank(a, years):
    i = 0
    while i < years:
        i += 1
        a = a + ((a / 100) * 10)
    print("Сумма на счете, по окончанию " + str(i) + " лет: " + str(a))


def run_bank():
    sum_ = int(input("Сколько вносим денег: "))
    years_ = int(input("На какой срок: "))
    bank(sum_, years_)


if __name__ == '__main__':   
    run_bank()
