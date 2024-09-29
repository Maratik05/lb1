def take_large_banknotes(banknotes):
    banknotes10 = []
    for i in banknotes:
        if i > 10:
            banknotes10.append(i)

    return banknotes10
    take_large_banknotes([1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50])