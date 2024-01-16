# 使うライブラリをインポート
import sqlite3 #データベースに使用
from bs4 import BeautifulSoup # HTMLコード解析に使用
import requests # HTMLコード取得に使用
import time # サーバーに負荷をかけないようにするために使用

url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s1.php?prec_no=44&block_no=47662&year=2023&month=01&day=12&view=p1' # スクレイピングするURLを定義
d_list =[] # 空のリストを作成
r = requests.get(url) # "requests"ライブラリを使用して、指定されたURLに対してHTTP GETリクエストを送信し、レスポンスを変数"r"に格納
r.encoding = 'utf-8' # 文字化けしていたため、変数"r"を'utf-8'にエンコーディング
soup = BeautifulSoup(r.text, 'html.parser') # "r.text"で変数"r"のコードを解析し、Pythonで操作しやすい形に変換する。そして"soup"に格納。"html.parser"は解析器を指定している。

# テーブル内の各行（tr要素）を取得
for row in soup.find_all('tr', class_='mtx'): # "soup"のHTMLコードから、"class_"を指定し、trタグのみを取得。それをfor文で繰り返す。
    items = row.find_all('td') # 各行内の各tdタグを取得

    if len(items) >= 9:  # 表のセルが少なくとも9つあることを確認
        cell1 = items[0].text # セル1のデータをそのまま取得
        cell2 = items[1].text # セル2のデータをそのまま取得
        cell5 = items[4].text # セル5のデータをそのまま取得
        cell8 = items[7].text # セル8のデータをそのまま取得
        cell13 = items[12].text # セル13のデータをそのまま取得
        cell15 = items[14].text # セル15のデータをそのまま取得
        cell20 = items[20].text # セル20のデータをそのまま取得

        # 辞書を作成
        d = {
            'month': cell1, # 月のデータ
            'pressure': cell2, # 気圧のデータ
            'precipitation': cell5, # 降水量（日）のデータ
            'temperature': cell8, # 温度のデータ
            'humidity': cell13, # 湿度のデータ
            'wind_speed': cell15, # 風速のデータ
            'daylight_hours': cell20, # 日照時間（h）のデータ
        }
        d_list.append(d) # 最後に繰り返し最初に作成したd_listに追加する

# DBファイルを保存するためのファイルパス
path = '/Users/macuser/Desktop/dsp2_work/' # ローカル（自分のMac）

# DBファイル名
db_name = 'db.sqlite'

# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect(path + db_name)

# SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 既存のテーブルがある場合は削除する（エラー解消のため）
cur.execute('DROP TABLE IF EXISTS weather_data;')

# 実行したいSQLを用意する
# テーブルを作成するSQL
# CREATE TABLE テーブル名（カラム名 型，...）;
sql_create_table = 'CREATE TABLE weather_data(month INTEGER, pressure int, precipitation int, temperature int, humidity INTEGER, wind_speed int, daylight_hours int);'

# SQLを実行する
cur.execute(sql_create_table)

# d_listの情報をデータベースに追加する
for item in d_list:
    cur.execute('''
        INSERT INTO weather_data (month, pressure, precipitation, temperature, humidity, wind_speed, daylight_hours)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (item['month'], item['pressure'], item['precipitation'], item['temperature'], item['humidity'], item['wind_speed'], item['daylight_hours']))

# 必要があればコミットする（データ変更等があった場合）
# 今回は念の為コミットしておく
con.commit()

# DBへの接続を閉じる
con.close()