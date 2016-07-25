##### ex-6 & 7
# This example demonstrates the use of sessions to track individual
# web users and store information about them.

from flask import Flask, request, render_template, redirect, session

import pg

db = pg.DB(dbname='restaurant_db2')

query = db.query('select * from reviewer')
print query

app = Flask('MyApp')

@app.route('/')
def home():
    # A session is just like a Python dictionary, in every way
    # you can check in a key exists in the dictionary
    if 'name' in session:
        # session['name'] is how you get the value for a key
        # alternatively, you can use session.get('name') or
        # session.get('name', DEFAULT_VALUE)
        return render_template('session-hello.html', name=session['name'])
        return redirect('/user-reviews')
    else:
        return render_template('session-get-name.html')

@app.route('/submit_name', methods=['POST'])
def submit_name():
    # This is how you set a value of a session variable
    session['name'] = request.form['name']
    return redirect('/')

# @app.route('/user_reviews', methods=['POST'])
# def user_reviews():
#     query = db.query(
#         "select reviewer.id from reviewer where name = '%s'" % session['name'])
#     print query
#     return redirect('/user-reviews')

@app.route('/clear_name')
def clear_name():
    # this is how you clear a session variable
    del session['name']
    return redirect('/')

# You have to set up the secret key, or sessions will not work, this is just like with Express.
app.secret_key = 'CSF686CCF85C6FRTCHQDBJDXHBHC1G478C86GCFTDCR'

if __name__ == '__main__':
    app.run(debug=True)
