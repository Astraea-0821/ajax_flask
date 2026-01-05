from flask import Flask, render_template
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message':'Hello, RESTful API!!'}

# http://127.0.0.1:5000/api
api.add_resource(HelloWorld, '/api')


# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template('index.html')


# http://127.0.0.1:5000/page1
@app.route('/page1')
def page1():
    return render_template('page1.html')



if __name__ == '__main__':
    app.run(debug=True)


