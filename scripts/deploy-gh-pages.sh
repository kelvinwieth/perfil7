#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf out /tmp/perfil7-pages-dist
GH_PAGES=true npm run build
mkdir -p /tmp/perfil7-pages-dist
cp -a out/. /tmp/perfil7-pages-dist/
touch /tmp/perfil7-pages-dist/.nojekyll

# Push dist as gh-pages using a throwaway git dir
cd /tmp/perfil7-pages-dist
git init
git checkout -b gh-pages
git add -A
git -c user.name='Cursor Agent' -c user.email='cursoragent@cursor.com' commit -m "Deploy static site to GitHub Pages"
git remote add origin https://github.com/kelvinwieth/perfil7.git
git push -f origin gh-pages
echo "Deployed: https://kelvinwieth.github.io/perfil7/"
