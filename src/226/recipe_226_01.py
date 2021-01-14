import sqlite3

with sqlite3.connect('example.db') as conn:
    conn.row_factory = sqlite3.Row
    # カーソルを取得
    cur = conn.cursor()

    # 1. カーソルをイテレータ (iterator) として扱う
    print("-------------------- 1 --------------------")
    cur.execute('select * from articles')
    for row in cur:
        # rowオブジェクトでデータが取得できる。タプル型の結果が取得
        print(row["id"])

    # 2. fetchallで結果リストを取得する
    print("-------------------- 2 --------------------")
    cur.execute('select * from articles')
    for row in cur.fetchall():
        print(row["id"])

    # 3. fetchoneで1件ずつ取得する
    print("-------------------- 3 --------------------")
    cur.execute('select * from articles')
    print(cur.fetchone()["id"])  # 1レコード目が取得
    print(cur.fetchone()["id"])  # 2レコード目が取得
