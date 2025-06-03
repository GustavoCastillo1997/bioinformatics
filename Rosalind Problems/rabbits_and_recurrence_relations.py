months = 32
litter_in_pairs = 5
recurrence_sequence = [1, 1]

for month in range(1, months-1):
    new_month = (recurrence_sequence[month-1] * litter_in_pairs) + recurrence_sequence[month]
    recurrence_sequence.append(new_month)

print(recurrence_sequence)

print(f'Total de pares de coelhos no {months}º mês: {recurrence_sequence[months-1]}')
