#!/bin/bash

cat ./templates/top.html ./content/index.html ./templates/bottom.html > ./docs/index.html
cat ./templates/top.html ./content/contact.html ./templates/bottom.html > ./docs/contact.html
cat ./templates/top.html ./content/toolset.html ./templates/bottom.html > ./docs/toolset.html

echo done
