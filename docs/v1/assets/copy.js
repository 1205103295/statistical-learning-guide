"use strict";
document.getElementById("copy")?.addEventListener("click", async () => {
 const code=document.getElementById("code"), status=document.getElementById("status");
 try { if(!navigator.clipboard) throw new Error("unavailable");
   await navigator.clipboard.writeText(code.value); status.textContent="已复制整块代码，可以粘贴到 Jupyter 单元格。";
 } catch (_) { code.focus(); code.select(); status.textContent="代码已全部选中，请按 Ctrl+C（Mac：⌘C），或使用浏览器的复制菜单。"; }
});