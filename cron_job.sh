set -e

# Call get_comic.sh
bash /home/connor/projects/xkcd_term/get_comic.sh
# Get new_comic name
comic=`ls /home/connor/projects/xkcd_term/new_comic/*.png`
# Send email to me with xkcd comic as attachment
python /home/connor/projects/xkcd_term/email_comic.py "$comic"