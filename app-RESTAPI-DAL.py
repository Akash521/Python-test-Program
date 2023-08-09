from flask import Flask, render_template, request, redirect
from dal import PostDAL

app = Flask(__name__)
post_dal = PostDAL()

@app.route('/')
def home():
    posts = post_dal.get_all_posts()
    return render_template('home.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = {'title': title, 'content': content}
        post_dal.create_post(post)
        return redirect('/')
    return render_template('create_post.html')

@app.route('/post/<post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    post = post_dal.get_post_by_id(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post_data = {'title': title, 'content': content}
        post_dal.update_post(post_id, post_data)
        return redirect('/')
    return render_template('update_post.html', post=post)

@app.route('/post/<post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post_dal.delete_post(post_id)
    return redirect('/')