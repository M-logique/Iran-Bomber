<%# FILE: .github/release-notes.ejs %>
<%#
  ARCHITECT'S NOTE: This is an EJS template. It uses JavaScript-like syntax
  within <% ... %> tags to dynamically generate Markdown.
  It iterates through a list of assets (your compiled binaries) to build the table.
%>
<div align="center">
  <img src="https://img.shields.io/github/downloads/M-logique/Iran-Bomber/<%= nextRelease.gitTag %>/total?style=for-the-badge&logo=github" alt="Release Downloads">
  <img src="https://img.shields.io/github/v/release/M-logique/Iran-Bomber?style=for-the-badge&logo=github" alt="Latest Release Version">
</div>

---

<%= nextRelease.notes %>

---

### 📥 Downloads

Here are the compiled binaries for various platforms. We recommend verifying the download integrity using the provided SHA-256 checksums.

| Operating System | Architecture | Download Link | SHA-256 Checksum |
| ---------------- | ------------ | ------------- | ---------------- |
<% assets.forEach(asset => { %>
| <%= asset.os %> | <%= asset.arch %> | [<%= asset.name %>](<%= asset.url %>) | `<%= asset.checksum %>` |
<% }); %>

---

### 📖 Full Changelog
See the full changelog here: [CHANGELOG.md](https://github.com/M-logique/Iran-Bomber/blob/<%= nextRelease.gitTag %>/CHANGELOG.md)

---

### 🛠️ Contribute
Found a bug or have a feature request? Feel free to [open an issue](https://github.com/M-logique/Iran-Bomber/issues) or [create a pull request](https://github.com/M-logique/Iran-Bomber/pulls).