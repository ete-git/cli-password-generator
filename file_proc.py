#ファイル処理に関する関数

from cryptography.fernet import Fernet

#txtファイルの書き込み
#受け取った引数(パスワード)をtxtファイルに書き込む
def pass_write(password):
    file = open("passwd.txt","w")
    file.write(f"{password}")
    file.close()



#ファイルの暗号化（パス指定なし）
def pass_lock():
    #pass.key(キーファイル)の作成
    key = Fernet.generate_key()
    file = open("pass.key","wb")
    file.write(key)  

    #キーファイルをkeyに読み込む
    file = open("pass.key","rb")
    key = file.read()

    #txtファイルをpasswdに読み込む
    file = open("passwd.txt", "rb")
    passwd = file.read()
    
    #passwd.txtに入ってる内容を暗号化
    fernet = Fernet(key)
    encrypt_pass = fernet.encrypt(passwd)

    #暗号化されたファイルの出力
    file = open("passwd.txt","wb")
    file.write(encrypt_pass)

    file.close()



#decrypt.pyで使用する関数,パス指定ありでファイルを復号化します。
def pass_unlock(key_path,passwd_path):
    #キーファイルをkeyに読み込む
    file = open(key_path, "rb")
    key = file.read()

    #暗号化されたtxtファイルをpasswdに読み込む
    file = open(passwd_path, "rb")
    passwd = file.read()

    #復号したパスワードの文字をdecrypt_passに格納
    fernet = Fernet(key)
    decrypt_pass = fernet.decrypt(passwd)

    #バイト文字列から通常の文字列型に変換
    decrypt_pass = decrypt_pass.decode("utf-8")

    #復号化されたファイルの出力
    file = open("passwd.txt","w")
    file.write(decrypt_pass)

    file.close()



#decrypt.pyで使用する関数,パス指定ありでファイルを暗号化します。
def pass_lock_alt(passwd_path):    
    #pass.key(キーファイル)の作成
    key = Fernet.generate_key()
    file = open("pass.key","wb")
    file.write(key)  

    #キーファイルをkeyに読み込む
    file = open("pass.key","rb")
    key = file.read()

    #txtファイルをpasswdに読み込む
    file = open(passwd_path, "rb")
    passwd = file.read()
    
    #passwd.txtに入ってる内容を暗号化
    fernet = Fernet(key)
    encrypt_pass = fernet.encrypt(passwd)

    #暗号化されたファイルの出力
    file = open(passwd_path,"wb")
    file.write(encrypt_pass)

    file.close()
