import sqlite3

# DBファイルを保存するためのファイルパス
path = '/Users/macuser/Desktop/dsp2_work/' # ローカル（自分のMac）

# DBファイル名
db_name = 'db.sqlite'

# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect(path + db_name)

# SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 既存のテーブルがあれば削除する
cur.execute('DROP TABLE IF EXISTS local_data;')

# 実行したいSQLを用意する
# テーブルを作成するSQL
# CREATE TABLE テーブル名（カラム名 型，...）;
sql_create_table_local_data = 'CREATE TABLE local_data(month INTEGER, number_of_steps INTEGER, water_price INTEGER, gas_price INTEGER, sleeping_time INTEGER);'

# SQLを実行する
cur.execute(sql_create_table_local_data)

# SQLを用意
# データを挿入するSQL
# INSERT INTO テーブル名 VALUES (列に対応したデータをカンマ区切りで);
sql_insert_many = "INSERT INTO local_data VALUES (?, ?, ?, ?, ?);"

# データをリストで用意する
local_data_list = [
    (1, 3715, 4243, 7957, 380),
    (2, 2463, 4141, 6089, 392),
    (3, 9700, 3016, 4149, 304),
    (4, 6501, 2085, 2335, 322),
    (5, 5639, 2563, 6367, 349),
    (6, 8537, 3119, 6164, 365),
    (7, 5539, 1837, 6947, 343),
    (8, 8734, 2274, 4376, 324),
    (9, 11962, 2200, 2556, 345),
    (10, 13416, 2697, 2715, 323),
    (11, 7952, 3168, 3449, 324),
    (12, 6647, 3823, 7437, 394),
]

# SQLを実行
cur.executemany(sql_insert_many, local_data_list)

# コミット処理（データ操作を反映させる）
con.commit()

# DBへの接続を閉じる
con.close()