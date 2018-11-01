def my_solution():
        numbers = [input('Enter a value: ') for i in range(10)]
        odds = [y for y in numbers if y % 2 != 0]
        if odds:
            return max(odds)
        else:
            return 'All declared variables have even values.'
my_solution()
