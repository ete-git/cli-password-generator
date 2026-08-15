#inputに関する関数
import os

#最大と最小の範囲を決めて数字を入力させる関数
#引数min,maxはそれぞれ最小と最大の数値、この範囲内で入力させる。
def input_num_lim(text,min,max):
    while True:
        num = input(f"{text}({min}~{max})：")
        if num.isdigit():   #numが整数であるかチェック            
            if min <= int(num) <= max:  #minとmaxの範囲内であるかチェック
                return num  #範囲内であればその数字を返す
            else:
                print(f"無効な値：{min}~{max}の範囲内で入力してください。") #範囲内でなければループ
                print()
        else:
            print(f"無効な入力：整数で入力してください。") #数値でなければループ
            print()



#yかnの入力で真偽を返す関数
#インプットでyが入力されたらTrue,nならFalseを返す
def input_bool(text):   #引数textには質問文が入る
    while True:
        judge = input(f"{text}[y/n]：")
        #.lower()は小文字に変換させる → 大文字で入力しても動作させる
        if judge.lower() == "y" :
            return True
        elif judge.lower() == "n":
            return False
        else:
            print("無効な入力：yかnを入力してください")



#パスを入力させ,そのファイル名が存在するか調べる関数
#引数のfile_nameは探したいファイル名
def input_path(file_name):
    while True:
        file_path = input(f"{file_name}のパスを入力又はファイルをドラッグ＆ドロップしてください：")
        # 前後の空白や引用符を取り除く
        if file_path is None:
            print()
            print("無効なパス：入力が空です。")
            print()
            continue
        file_path = file_path.strip().strip('"').strip("'")

        # 実際にファイルが存在するか確認する
        if not os.path.isfile(file_path):
            print()
            print("無効なパス：ファイルが存在しないかパスが間違っています。")
            print()
            continue

        # 指定されたファイル名がベース名に含まれているか確認
        if file_name not in os.path.basename(file_path):
            print()
            print(f"無効なパス：指定したファイル名 '{file_name}' がパスに含まれていません。")
            print()
            continue

        print("読み込み完了")
        return file_path    # ファイルのパスを返す
        

        