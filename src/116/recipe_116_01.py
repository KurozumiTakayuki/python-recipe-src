import configparser

# configファイルの読み込み
config = configparser.ConfigParser()
config.read('config.ini')

# 値を文字列で取得する
config['SAMPLE1']['str_key']

# configの型に応じた値を取得する
str_value = config.get('SAMPLE1', 'str_key')
int_value = config.getint('SAMPLE1', 'int_key')
float_value = config.getfloat('SAMPLE2', 'float_key')
bool_value = config.getboolean('SAMPLE2', 'bool_key')

# 値を表示する
print(str_value)
print(int_value)
print(float_value)
print(bool_value)
