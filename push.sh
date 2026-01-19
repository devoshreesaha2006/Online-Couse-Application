#!/bin/bash
cd "/c/Users/Lifa.Mbangata/Downloads/Python App/onlinecourse"
git init
git config user.email "lifa.mbangata@example.com"
git config user.name "Lifa Mbangata"
git add .
git commit -m "Initial commit: Complete Online Course Application with exam features"
git remote add origin https://github.com/Lifa-Mbangata/Online-Couse-Application.git
git branch -M main
git push -u origin main
echo "Repository pushed to GitHub successfully!"
