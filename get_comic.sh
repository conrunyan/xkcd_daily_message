set -e

comic_name=$1
# get daily comic
xkcd_url="https://xkcd.com/info.0.json"
wget $xkcd_url > $1
# delete old comic (for testing move to hold_comic)
rm 
# move comic to new_comic dir
