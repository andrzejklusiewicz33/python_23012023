from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Strona główna'

@app.route('/examples')
def examples():
    return "<h1>przykłady</h1>dupa dupa dupa"

if __name__ == '__main__':
    app.run(debug=True,port=80)


#52. 

#Flask,Django,FastApi, Pyramid
#uWSGI
#https://www.pythonanywhere.com/