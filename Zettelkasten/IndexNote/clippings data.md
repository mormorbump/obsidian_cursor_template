---
cssclasses:
  - zettelkasten
---
```dataviewjs
dv.table(
  ["画像", "ノート", "作成日"],
  dv.pages("#clipping")
    .sort(b => b.file.cday, 'desc')
    .map(b => {
      const imageUrl = b.image
        ? b.image
        : "https://placehold.jp/cfcfcf/ffffff/1200x630.png?text=No%20Image";
      return [
        `<img src="${imageUrl}" width="300">`, // 適宜サイズ調整
        b.file.link,
        b.file.cday
      ];
    })
);
```
