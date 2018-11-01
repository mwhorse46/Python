exDict = {'Jaimin':[20, 'black'], 'Ajay':[18,'blonde'], 'Jack':[22,'pink']}
print(exDict)
print(exDict['Jaimin'])
print(exDict['Jaimin'][1])

exDict['Tim'] = 14

print(exDict)

exDict['Tim'] = 15

print(exDict)

del exDict['Tim']

print(exDict)
