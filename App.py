from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
    return 'Hello World'

@app.route('/add_contact')
def add_contact():
    return 'add contact'

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
