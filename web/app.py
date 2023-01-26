from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Strona główna'

@app.route('/show_products')
def show_products():
    return "<h1>Lista produktów</h1>"

@app.route('/show_employees')
def show_employees():
    return "<h1>Lista pracowników</h1>"

@app.route('/about')
def about():
    return "<h1>Strona o programie</h1>"

@app.route('/examples')
def examples():
    print("Ktoś wszedł na ekran /examples....")
    return render_template("examples.html")


if __name__ == '__main__':
    app.run(debug=True,port=80)


#52. Dodaj obsługę ekranów pod adresami /show_products /show_employees /about
#Po wejściu na każdy z tych ekranów powinien pojawić się komunikat z tekstem jednoznacznie identyfikujacym na jakiej podstronie jesteściee
#53. Zadbaj o to, by wszystkie ekrany były obsługiwane przez osobne pliki html

#Flask,Django,FastApi, Pyramid
#uWSGI
#https://www.pythonanywhere.com/