enterd = True # ループ処理を続行するかどうかのフラグ

while enterd:
    print('キーを入力してください')
    c = input()
 
    if c == 'end':
        enterd = False
    else:
        print(c + ' が入力されました')
