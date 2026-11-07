filename = input("読み込むファイル名: ")

# バリデーション: 空文字なら使い方を表示して終了
if filename == "":
    print("ファイル名を入力してください")
else:
    try:
        with open(filename, encoding="utf-8") as f:
            content = f.read()
        print("ファイルの中身は", content, "でした")
    except FileNotFoundError:
        print(filename, "が見つかりません")