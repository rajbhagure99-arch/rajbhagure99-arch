# Cyber Lab Profile — Setup

1. Confirm the GitHub username is exactly `rajbhagure99-arch`.
2. This repository must be named **`rajbhagure99-arch`** for GitHub to show it as your profile README.
3. Review `README.md`; replace all `[PROJECT_NAME]`, `[TECH_STACK]`, and `PLACEHOLDER` text with accurate information.
4. Keep or replace `banner.svg` and `divider.svg` in the repository root. Their README paths are `./banner.svg` and `./divider.svg`.
5. In GitHub, open **Settings → Actions → General → Workflow permissions** and ensure workflows can write repository contents if the snake workflow needs it.
6. Commit the files to the `main` branch. Open **Actions → Generate contribution snake → Run workflow** to test it.
7. After the workflow creates the `output` branch, reload the README. Third-party stats may take time or be rate-limited.

## Upload with Git

From inside the project directory:

```bash
git init
git branch -M main
git add README.md LICENSE banner.svg divider.svg .github/workflows/snake.yml
git commit -m "Build Cyber Lab profile README"
git remote add origin https://github.com/rajbhagure99-arch/rajbhagure99-arch.git
git push -u origin main
```

If the repository already has a remote or files, inspect them first. Do not run `git init` or replace remotes blindly in an existing repository.

## Important
- GitHub README pages do not honor custom CSS background colors or arbitrary styles.
- Stats and snake images depend on external services and can occasionally be unavailable.
- The project cards are clearly marked placeholders; do not imply unfinished projects are completed.
- Never put passwords, API keys, tokens, private IPs, or sensitive client/lab details in a public repository.
