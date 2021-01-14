import MySQLdb

# 接続情報
con_info = {"user":"db user", "passwd":"db password", "host":"localhost", "db":"sample", "charset":"utf8"}

# 接続する
with MySQLdb.connect(**con_info) as con:

    # カーソルを取得する
    with con.cursor() as cur:

        # クエリを実行する
        sql = "select id, body, post_code, created from posts where id > %s and post_code in %s"
        cur.execute(sql, (1, [1, 2, 3], ))

        # 実行結果をすべて取得する
        rows = cur.fetchall()
            
        # 一行ずつ表示する
        for row in rows:
            print(row)
