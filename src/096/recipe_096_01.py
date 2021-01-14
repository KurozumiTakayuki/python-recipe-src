def div_num(a, b):
    try:
        val = a / b
        print("割り算結果:{}".format(val))
    except:
        print("例外が発生しました。")
    else:
        print("処理が正常に終了しました。")
    finally:
        print("処理が終了しました。")


print('----- 正常処理の場合 -----')
div_num(4, 2)
print('----- 例外発生の場合 -----')
div_num(10, 0)
