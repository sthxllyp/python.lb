def draw_numbers(rows):
    for i in range(1, rows + 1):
        row = (str(rows) + ' ') * i
        print(row)
draw_numbers(5)