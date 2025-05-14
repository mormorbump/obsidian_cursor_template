## Obsidian × Cursorテンプレート

基本的にこの記事をベースに実装しています: 
https://note.com/shotovim/n/n5833578984bf

#### Zettelkastenについて

[x.com/ShinWorkout0207/status/1920637351174549656?ref\_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1920637351174549656%7Ctwgr%5E7f626af2b1d458d85fc35d418d57ad37a5e00069%7Ctwcon%5Es1\_&ref\_url=https%3A%2F%2Fnote.com%2Fiam\_shin%2Fn%2Fnb29cea186412](https://x.com/ShinWorkout0207/status/1920637351174549656?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1920637351174549656%7Ctwgr%5E7f626af2b1d458d85fc35d418d57ad37a5e00069%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fnote.com%2Fiam_shin%2Fn%2Fnb29cea186412)

### 初期設定の必要がないコミュニティプラグイン
- AutoLinkTitle
	- コピペするだけでタイトルをつけてくれます。
- Calender
	- カレンダーが見れます。Memo(Thino)と紐づきます。
- DataView
	- Notionみたいなテンプレートを作成できます。IndexNote参照
- ExcaliBrain
	- 文章やテキストをビジュアルマップとして表示するために使用します。
- Excalidraw
	- obsidian上で手書きの図が作成できます。
- recent-files-obsidian
	- 最新のファイルを参照できます。
- tag-wrangler
	- 同名のタグを一括検索、一括編集などができます。
- templater-obsidian
	- markdownのテンプレートを作成することができます。Template参照
- obsidian-memos(Thino)
	- XライクのUIでメモを作成することができます。Memo(Thino)以下に格納

### 初期設定が必要なコミュニティプラグイン

- [obsidian-git](https://github.com/Vinzent03/obsidian-git)
	- モバイルのObsidianアプリと課金せずに同期したいなら必要です。
	- 必須ではありませんが、やっておくと色々と便利です。
	- プロジェクトにある`.git` を削除してから、自分のgithubのリポジトリと繋げ直してもらう必要があります。
- [obsidian-kindle-plugin](https://github.com/hadynz/obsidian-kindle-plugin)
	- Kindleでハイライトした部分をObsidianに同期できます。
	- 自分のamazonのアカウントでログインし直してもらう必要があります。
- [s3-image-uploader](https://github.com/jvsteiner/s3-image-uploader)
	- 必須ではありません。
	- モバイルのObsidianアプリで課金せずに画像読み込みしたいなら必要です。
	- AWSのアカウントを作成し、S3とIAMユーザ、ポリシーを作成する必要があります。
- [LINE Notes Sync](https://note.com/shotovim/n/n55c363144d86)
	-  LINEからObsidianにメモを送信することができます。
- [Obsidian\_to\_Anki](https://github.com/ObsidianToAnki/Obsidian_to_Anki)
	- Anki側の設定でもアドオンの追加が必要です。
	- Ankiのメリットはこちら [Obsidianと連携する暗記アプリ、本当にAnkiでいいのか検証してみた｜けぽ](https://note.com/kepoorz/n/n6f8f72da106d)

### gitignoreのルール
参考: 
[\[Obsidian\] 結局行き着いた .gitignore｜しょっさん](https://note.com/sho7650/n/nbbc6976103ff)


### Tasksの用途

以下を実装すればmarkdownに日付、時間、タスク名を書くと同期されます。

[Obsidian と Google カレンダーを連携してシームレスなタスク管理を実現する｜松濤Vimmer](https://note.com/shotovim/n/n22400bc4ddb7)

GCPのアカウントを作成し、Google Calender APIの有効化、OAuthの有効化などを行う必要があるため、結構やることが多いです。

### Cursor(AIエディタ)の役割

- 用意された複数の記事を1つのファイルにまとめる
- 出力されたファイルをアップデートする
- ファイル同士を紐づける
- Kindleなどの書籍引用部分を補足する(理解度テストを作ったり)
- 記事のタグづけを一貫性を持って行う
- Ankiデッキを自動で作成
- Slidev用のスライドを自動で作成

### モバイル版Obsidianの対応
各端末で設定する必要があります: 
[スマホのObsidianをGitで同期(2024.11)](https://zenn.dev/ishikawa096/articles/158246fc5a5d62)