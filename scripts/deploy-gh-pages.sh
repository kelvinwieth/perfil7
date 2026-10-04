#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
ORIGIN_URL="$(git remote get-url origin)"
APP_VERSION="$(node -p "require('./package.json').version")"
echo "Building perfil7 v${APP_VERSION} for GitHub Pages..."
rm -rf out /tmp/perfil7-pages-dist
GH_PAGES=true npm run build
mkdir -p /tmp/perfil7-pages-dist
cp -a out/. /tmp/perfil7-pages-dist/
touch /tmp/perfil7-pages-dist/.nojekyll

cd /tmp/perfil7-pages-dist
git init
git checkout -b gh-pages
git add -A
git -c user.name='Cursor Agent' -c user.email='cursoragent@cursor.com' commit -m "Deploy static site to GitHub Pages"
git remote add origin "$ORIGIN_URL"
git push -f origin gh-pages

cd "$ROOT"
npm version patch --no-git-tag-version
NEXT_VERSION="$(node -p "require('./package.json').version")"

if [[ "$ORIGIN_URL" =~ github\.com[:/]([^/]+)/([^/.]+) ]]; then
  OWNER="${BASH_REMATCH[1]}"
  REPO="${BASH_REMATCH[2]%.git}"
  echo "Deployed v${APP_VERSION}: https://${OWNER}.github.io/${REPO}/"
else
  echo "Deployed v${APP_VERSION} to gh-pages on origin."
fi
echo "Next release: v${NEXT_VERSION} (package.json bumped — commit on main)"
