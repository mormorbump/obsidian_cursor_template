## Obsidian × Cursorテンプレート

基本的にこの記事をベースに実装しています。
https://note.com/shotovim/n/n5833578984bf

### 初期設定の必要がないコミュニティプラグイン
- AutoLinkTitle
	- コピペするだけでタイトルをつけてくれます。
- Calender
	- カレンダーが見れます。Memo(Thino)と紐づきます。
- DataView
	- Notionみたいなテンプレートを作成できます。IndexNote参照
- ExcaliBrain
- Excalidraw
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

### gitignoreのルール
参考
[\[Obsidian\] 結局行き着いた .gitignore｜しょっさん](https://note.com/sho7650/n/nbbc6976103ff)


### Tasksの用途

### Cursor(AIエディタ)の役割

- 用意された複数の記事を1つのファイルにまとめる
- 出力されたファイルをアップデートする
- ファイル同士を紐づける
- Kindleなどの書籍引用部分を補足する(理解度テストを作ったり)
- 記事のタグづけを一貫性を持って行う
- Ankiデッキを自動で作成
- Slidev用のスライドを自動で作成