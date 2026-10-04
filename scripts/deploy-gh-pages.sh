#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
ORIGIN_URL="$(git remote get-url origin)"
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

if [[ "$ORIGIN_URL" =~ github\.com[:/]([^/]+)/([^/.]+) ]]; then
  OWNER="${BASH_REMATCH[1]}"
  REPO="${BASH_REMATCH[2]%.git}"
  echo "Deployed: https://${OWNER}.github.io/${REPO}/"
else
  echo "Deployed to gh-pages on origin."
fi
