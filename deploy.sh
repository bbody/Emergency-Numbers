#!/bin/sh
GH_TOKEN=$1

git config --global user.email "support@travis-ci.org"
git config --global user.name "Travis CI"

git add countries.json
git commit --message "Recompile Country List"

git remote remove origin
git remote add origin https://bbody:${GH_TOKEN}@github.com/bbody/Emergency-Numbers.git > /dev/null 2>&1
git push --quiet --set-upstream origin master 