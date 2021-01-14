def div_num(a, b):
    try:
        val = a / b
        print(val)
    except Exception as e:
        print("例外が発生しました。呼び出し元で処理してください。")
        raise e


div_num(7, 0)
