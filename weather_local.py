import sqlite3

# DBファイルを保存するためのファイルパス
path = '/Users/macuser/Desktop/dsp2_work/' # ローカル（自分のMac）

# DBファイル名
db_name = 'weather_db.sqlite'

# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect(path + db_name)

# SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 既存のテーブルがあれば削除する
cur.execute('DROP TABLE IF EXISTS weather_local_db;')

# 実行したいSQLを用意する
# テーブルを作成するSQL
# CREATE TABLE テーブル名（カラム名 型，...）;
sql_create_table_weather_local_db = 'CREATE TABLE weather_local_db(pressure_local int, temperature_local int, humidity_local int);'

# SQLを実行する
cur.execute(sql_create_table_weather_local_db)

# SQLを用意
# データを挿入するSQL
# INSERT INTO テーブル名 VALUES (列に対応したデータをカンマ区切りで);
sql_insert_many = "INSERT INTO weather_local_db VALUES (?, ?, ?);"

# データをリストで用意する
weather_local_db_list = [
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
]

# SQLを実行
cur.executemany(sql_insert_many, weather_local_db_list)

# コミット処理（データ操作を反映させる）
con.commit()

# DBへの接続を閉じる
con.close()