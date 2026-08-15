#暗号化されたtxtを復号、また暗号化を行います

import enter
import file_proc
from time import sleep

#外部からこのプログラムを実行させる関数
def execute():
    try:
        print()
        print("<<--txtファイルの復号化-->>")
        print("passwd.txtの復号化を行います。")
        print()
        sleep(0.5)


        #キーファイルのパス指定（復号化するを選択した場合のみ）
        key_path = enter.input_path("pass.key") #指定したパスの中にファイルがあるかチェックする関数
        print()


        #暗号化されたtxtファイルのパス指定
        passwd_path = enter.input_path("passwd.txt")
        print()


        #復号化の処理
        if enter.input_bool("パスが読み込まれました。txtファイルを復号化しますか？"):
            file_proc.pass_unlock(key_path,passwd_path)    #ファイルの復号化をする関数
            print()
            print("ファイルの復号化が完了しました。ファイルを確認ください。")
        else:
            return


    #ctrl+cが押されたときの例外処理(エラーを表示させずにプログラムを中断させる)            
    except KeyboardInterrupt:
        print()
        print("<<Ctrl+Cが押されました。メニューに戻ります。>>")

if __name__ == "__main__":
    execute()