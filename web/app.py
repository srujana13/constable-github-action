try:
    from flask import Flask, render_template, url_for, request, redirect, make_response
    import random
    import json
    import os
    from time import time
    from random import random
    from flask import Flask, render_template, make_response
    from flask_dance.contrib.github import make_github_blueprint, github
    from getGithubData import Github
    from constable import Constable
    from badge import Badge
except Exception as e:
    print("Some Modules are Missing {}".format(e))

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ['secret_key']

github_blueprint = make_github_blueprint(client_id=os.environ['client_id'],
                                         client_secret=os.environ['client_secret'])

app.register_blueprint(github_blueprint, url_prefix='/github_login')

@app.route('/')
def github_login():

    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_data = account_info.json()
            user = account_data['login']
            return render_template('index.html', title='Welcome', user=user)
    return '<h1>Request failed!</h1>'

@app.route('/get_score')
def get_score():
    repo_name = request.args.get('repo')
    account_info = github.get('/user')
    account_data = account_info.json()
    owner = account_data['login']
    github_gql = Github(github.access_token)
    constable = Constable(repo_name, owner, github_gql)
    score = constable.get_score()
    print(score)
    grade = constable.get_grade(score['total_score'])
    branch = 'master'
    key = '{}/{}/{}'.format(owner, repo_name, branch)
    badge = Badge(key).get_shield_url(grade=grade)
    return {"score": score, "grade": grade, "badge": badge}

@app.route('/check_repo')
def check_valid_repo():
    repo_name = request.args.get('repo')
    if github.authorized:
        github_gql = Github(github.access_token)
        valid = github_gql.check_valid_repo(repo_name)
    else:
        valid = False
    return {"valid": valid}