import time
import tinydb

'''
This is a post. A post contains the username of the user that posted it, a post-id, text, a picture url, 
a video url, reactions, and comments.
'''

#Adds a post to the database.
#Takes in a user to get the username of the user who made the post.
#Takes in text.
#Takes in picture_url (if any).
#Takes in a video_url (if any)
def add_post(db, user, post_id, text, picture_url, video_url):
    posts = db.table('posts')
    posts.insert({'user': user['username'], 'post-id': post_id,
    'text': text, 'picture-url': picture_url, 'video-url': video_url, 'reactions': [], 
    'comments': [], 'time': time.time()})

def get_posts(db, user):
    posts = db.table('posts')
    Post = tinydb.Query()
    return posts.search(Post.user==user['username'])
