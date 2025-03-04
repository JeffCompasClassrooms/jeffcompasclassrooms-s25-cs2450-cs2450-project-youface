import time
import tinydb

def add_post(db, user, text):
    posts = db.table('posts')
    posts.insert({'user': user['username'], 'text': text, 'time': time.time(), 'id' : user['username'] + str(time.time())})

def get_posts(db, user):
    posts = db.table('posts')
    Post = tinydb.Query()
    return posts.search(Post.user==user['username'])

def delete_post(db, id):
    posts = db.table('posts')
    post = tinydb.Query()
    posts.remove(post.id == id)