def div_num(a, b):
    try:
        val = a / b
        print(val)
    except TypeError:
        print("演算できない引数が指定されました。処理を行いません。")
    except ZeroDivisionError:
        print("ゼロで除算を行おうとしています。処理を行いません。")
    except Exception:
        print("不明な例外が発生しました。")


div_num("abcdefg", 2)
div_num(7, 0)
