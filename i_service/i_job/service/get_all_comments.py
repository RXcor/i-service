import logging
import random
import time
from datetime import datetime

from InstagramAPI import InstagramAPI

logger = logging.getLogger(__name__)

def get_all_comments(client, media_id):


    # stop conditions, the script will end when first of them will be true
    until_date = '2018-03-31'
    count = 100

    has_more_comments = True
    min_id = ''
    comments = []

    while has_more_comments:
        _ = client.getMediaComments(media_id, min_id=min_id)
        # Загружаем в порядке от старых к новым
        for c in reversed(client.LastJson['comments']):
            comments.append(c)

        #has_more_comments = client.LastJson.get('has_more_comments', False)
        has_more_comments = client.LastJson.get('has_more_headload_comments', False)

        # Критерии остановки
        if count and len(comments) >= count:
            comments = comments[:count]
            # stop loop
            has_more_comments = False
            logger.debug("stopped by count")
        if until_date:
            older_comment = comments[-1]
            dt = datetime.utcfromtimestamp(older_comment.get('created_at_utc', 0))
            # only check all records if the last is older than stop condition
            if dt.isoformat() <= until_date:
                # keep comments after until_date
                comments = [
                    c
                    for c in comments
                    if datetime.utcfromtimestamp(c.get('created_at_utc', 0)) > until_date
                ]
                # stop loop
                has_more_comments = False
                logger.debug("stopped by until_date")
        # next page
        if has_more_comments:
            min_id = client.LastJson.get('next_min_id', '')
            time.sleep(random.uniform(1, 5))

    logger.debug(f"comments len: {len(comments)}")
    return comments
