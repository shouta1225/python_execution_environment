# 魚拓フォルダからファイルごとコピーした上でhtmlファイルのtextを出力するプログラムの完成
from fileinput import filename
from glob import glob
import os
from pathlib import Path
from sys import path
from bs4 import BeautifulSoup
import glob


dirname = './会社情報/kdx.co.jp'
file_lists = []
# 相対パスのディレクトリを出力する
for current_dir, _, _ in os.walk(dirname):# 相対パス
  # 正規表現を使う
  # 会社情報→company_text
  output_dir = []
  output_dir = str(current_dir.replace("会社情報", "company_text"))

  # 出力先にフォルダがない場合に作成で重複も許可
  os.makedirs(output_dir, exist_ok=True)

  # current_dirのpath内でglobを使ってhtmlファイルを検索し、pathに代入
  path = glob.glob(current_dir + '/*.html')
  file_lists += path

for file_list in file_lists:
  
  with open(file_list) as f:#ファイル操作処理を短縮するためにwith構文を用いる
    res = f.read()# ファイルの読み込み
  soup = BeautifulSoup(res, 'html.parser')# ファイルの解析
  # ファイルを開いて出力先を指定し、textファイルを出力
  file_name = str(file_list.replace("会社情報", "company_text"))
  file = open(file_name + '.txt','w')
  file.write(soup.text)
  file.close()