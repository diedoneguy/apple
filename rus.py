dolce = str(input('Введите предложение: '))
word = []
def milk(dolce):
    for i in dolce.lower().split():
        if 'жы' in i:
            word.append([
            i,
            i.replace('ы','и')])
        if 'очь' in i:
            word.append([
            i,
            i.replace('ь','')
            ])
    return word
print(milk(dolce))
