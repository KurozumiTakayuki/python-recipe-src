import os

app_env = os.environ.get("APP_ENV")
if app_env == 'DEV':
    print("開発環境で実行します")
elif app_env == 'PROD':
    print("本番環境で実行します")
else:
    print("適切な環境変数が設定されていません。")
