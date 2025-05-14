<%*
const fileName = tp.date.now("YYYY-MM-DD-HHmm"); 
const targetDir = "Zettelkasten/FleetingNote";
const targetPath = `${targetDir}/${fileName}`; 
await tp.file.move(targetPath); 
_%>
--- 
createdAt: <% tp.date.now("YYYY-MM-DD-HH:mm") %> 
permanentNote:
tags: 
---