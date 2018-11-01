exec("print('this works like eval')")
list_str = "[5,2,1,5]"
list_str = exec(list_str)
print(list_str)

exec("list_str2 = [5,6,4,5]")
print(list_str2)

exec("def test(): print('yo!')")
test()

exec("""
def test2():
    print('Yo this works too')

""")
test2()
