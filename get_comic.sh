#!/bin/bash
set -e
set -x

comic_name=$1
new_comic_dir="/home/connor/projects/xkcd_term/new_comic/"
# get daily comic
xkcd_url="https://xkcd.com/info.0.json"

wget -O $1 $xkcd_url
# delete old comic (for testing move to hold_comic)
rm -f $new_comic_dir*
# move comic json to new_comic dir
mv $1 $new_comic_dir
