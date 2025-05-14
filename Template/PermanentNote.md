<%*
const fileName = tp.date.now("YYYY-MM-DD-HH");
const targetDir = "Zettelkasten/PermanentNote"; 
const targetPath = `${targetDir}/${fileName}`;
await tp.file.move(targetPath);
_%>
--- 
createdAt: <% tp.date.now("YYYY-MM-DD-HH") %>
literatureNote: 
fleetingNote: 
tags: 
---