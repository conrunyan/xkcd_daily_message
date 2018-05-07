#!/bin/bash
set -e
set -x

new_comic_dir="/home/connor/projects/xkcd_term/new_comic/"
# get daily comic
xkcd_url="https://xkcd.com/info.0.json"
img_url=`curl -s "$xkcd_url" | python -c "import json, sys; print (json.load(sys.stdin)['img'])"`
img_name=echo $img_url | grep -E '\w+.png$'
echo $img_url
wget -O $img_name $img_url
# delete old comic (for testing move to hold_comic)
rm -f $new_comic_dir*
# move comic to new_comic dir
mv $1 $new_comic_dir
