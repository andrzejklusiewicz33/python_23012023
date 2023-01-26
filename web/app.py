from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show_products')
def show_products():
    return render_template("show_products.html")

@app.route('/show_employees')
def show_employees():
    return render_template("show_employees.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/examples')
def examples():
    print("Ktoś wszedł na ekran /examples....")
    return render_template("examples.html")


if __name__ == '__main__':
    app.run(debug=True,port=80)


#52. Dodaj obsługę ekranów pod adresami /show_products /show_employees /about
#Po wejściu na każdy z tych ekranów powinien pojawić się komunikat z tekstem jednoznacznie identyfikujacym na jakiej podstronie jesteściee
#53. Zadbaj o to, by wszystkie ekrany były obsługiwane przez osobne pliki html
#54. Do wszystkich ekranów dodaj działającce menu

#Flask,Django,FastApi, Pyramid
#uWSGI
#https://www.pythonanywhere.com/

#przerwa do 15:36