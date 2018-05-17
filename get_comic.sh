#!/bin/bash
set -e

new_comic_dir="/home/connor/projects/xkcd_term/new_comic/"
# get daily comic
xkcd_url="https://xkcd.com/info.0.json"
img_url=`curl -sq "$xkcd_url" | python -c "import json, sys; print (json.load(sys.stdin)['img'])"` # >> /home/connor/projects/xkcd_term/logs/curl_log`
img_name=`echo $img_url | grep -Eo "\w+.png\$"`
wget -O $img_name $img_url
# delete old comic (for testing move to hold_comic)
rm -f $new_comic_dir*
# move comic to new_comic dir
mv -f $img_name $new_comic_dir
echo "${new_comic_dir}${img_name}"
