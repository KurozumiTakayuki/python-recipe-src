def main():
    """ 
    ダブルクォート3つでdocstringとなります。
    ここに関数の説明を記述します。
    """
 
    # 通常のコメントは#を使います。
    # 通常の文と同様にインデントを合わせる必要があります。
    print("hello world!")
    
    # if文ではインデントします
    x = 100
    if x > 100:
        print("xは100より大きいです。")

    # ループでもインデントします
    num_list = [0, 1, 3]
    for num in num_list:
        # ブロック内部ではコメントもインデントします
        print(num)

        # 入れ子の場合はその分インデントを追加します
        if num > 1:
            print("numは1より大きいです。")

    # passは、何もしない文です
    pass

    # インデント内部に処理がない場合はpassを記述します
    if x < 100:
        pass

if __name__ == "__main__":
    main() # main関数の呼び出し
