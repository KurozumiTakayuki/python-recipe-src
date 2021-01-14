import psycopg2

# 接続情報
con_info = {"user":"db user", "password":"db password", "host":"localhost", "dbname":"sample"}

# 接続する 
with psycopg2.connect(**con_info) as con:

    # カーソルを取得する
    with con.cursor() as cur:

        # クエリを実行する
        sql = "select id, body, post_code, created from posts where id > %s and post_code in %s"
        cur.execute(sql, (1, (1, 2, 3), ))

        # 実行結果をすべて取得する
        rows = cur.fetchall()
            
        # 一行ずつ表示する
        for row in rows:
            print(row)
