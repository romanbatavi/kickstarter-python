from flask import Flask

application = Flask(__name__)

@application.route('/hello/<name>')
def hello(name):   
   return '<h2>Hello %s</h2>' % name

if __name__ == '__main__':
   application.run(debug=True)
