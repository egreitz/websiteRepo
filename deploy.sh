#!/bin/bash

# 1. Make sure you are in the repo root
cd "$(dirname "$0")"

# 2. Push Git changes (optional)
git add .
git commit -m "Deploy to Neocities" || echo "No changes to commit"
git push origin main

# 3. Push to Neocities, respecting .neocitiesignore
neocities push ./ --ignore-file .neocitiesignore --verbose

echo "Deployment complete! Only new or changed files were uploaded."
