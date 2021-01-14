import traceback

try:
    x = 1 / 0
except Exception as e:
    # 文字列を取得する format_exc()メソッド
    print("エラー情報\n" + traceback.format_exc())
