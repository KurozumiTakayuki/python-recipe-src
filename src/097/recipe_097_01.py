def div_num(a, b):
    try:
        val = a / b
        print(val)
    except Exception as e:
        print(e)


div_num("abcdefg", 2)
div_num(7, 0)
