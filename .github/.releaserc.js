const fs = require("fs");
const path = require("path");

const templatePath = path.join(__dirname, ".github", "release-template.md");

module.exports = {
  branches: [
    "master",
    { name: "beta", prerelease: "beta" },
    { name: "dev", prerelease: "dev" },
    { name: "alpha", prerelease: "alpha" },
  ],
  plugins: [
    [
      "@semantic-release/commit-analyzer",
      {
        preset: "conventionalcommits",
        releaseRules: [
          { type: "fix", release: "patch" },
          { type: "feat", release: "minor" },
          { type: "hotfix", release: "patch" },
          { type: "refactor", release: "patch" },
          { type: "style", release: "patch" },
          { type: "docs", release: false },
          { type: "chore", release: false },
          { type: "test", release: false },
          { type: "build", release: false },
          { type: "ci", release: false }
        ]
      }
    ],
    [
      "@semantic-release/release-notes-generator",
      {
        preset: "conventionalcommits",
        presetConfig: {
          types: [
            {
              type: "feat",
              section: "🚀 Features",
              hidden: false
            },
            {
              type: "fix",
              section: "🐛 Bug Fixes",
              hidden: false
            },
            {
              type: "hotfix",
              section: "🔥 Hot Fixes",
              hidden: false
            },
            {
              type: "refactor",
              section: "🚧 Refactors",
              hidden: false
            },
            {
              type: "style",
              section: "✨ Styles",
              hidden: false
            },
            {
              type: "docs",
              section: "📚 Documentation",
              hidden: false
            },
            {
              type: "test",
              section: "✅ Tests",
              hidden: false
            },
            {
              type: "perf",
              section: "⚡ Performance",
              hidden: false
            },
            {
              type: "ci",
              section: "🔄 CI/CD",
              hidden: false
            },
            {
              type: "build",
              section: "🏗️ Build",
              hidden: false
            },
            {
              type: "chore",
              hidden: true,
            },
          ]          
        }
      }
    ],
    "@semantic-release/changelog",
    [
      "@semantic-release/github",
      {
        releaseBodyTemplate: fs.readFileSync(templatePath, "utf8"),
        assets: [{ path: "dist/*" }],
      },
    ],
    [
      "@semantic-release/git",
      {
        assets: ["CHANGELOG.md"],
        message: "chore(release): ${nextRelease.version}\n\n${nextRelease.notes}",
      },
    ]
  ],
};