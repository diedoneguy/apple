sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
# def reder(sequence_2):
#     if len(sequence_2) == len(set(sequence_2)):
#         return 'Последовательность уникальна'
#     elif len(sequence_2) != len(set(sequence_2)):
#         return 'Последовательность нифига уникальна'
# print(reder(sequence_2))

if len(sequence_2) == len(set(sequence_2)):
    print('Последовательность уникальна')
elif len(sequence_2) != len(set(sequence_2)):
    print('Последовательность нифига не уникальна')