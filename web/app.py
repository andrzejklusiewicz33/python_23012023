from flask import Flask,render_template
from domain import *

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
    return render_template("about.html",author=Author())

@app.route('/about.json')
def about_json():
    return Author().serialize()

@app.route("/fruit.json")
def fruit_json():
    fruit=Fruit()
    return fruit.serialize()

@app.route('/examples')
def examples():
    return render_template("examples.html",fruit=Fruit())

# @app.route('/examples')
# def examples():
#     print("Ktoś wszedł na ekran /examples....")
#     f="banana"
#     c="yellow"
#     return render_template("examples.html",fruit=f,color=c)


if __name__ == '__main__':
    app.run(debug=True,port=80)


#52. Dodaj obsługę ekranów pod adresami /show_products /show_employees /about
#Po wejściu na każdy z tych ekranów powinien pojawić się komunikat z tekstem jednoznacznie identyfikujacym na jakiej podstronie jesteściee
#53. Zadbaj o to, by wszystkie ekrany były obsługiwane przez osobne pliki html
#54. Do wszystkich ekranów dodaj działającce menu
#55. Do widoku ekranu /about przekaż informację o swoim imieniu, nazwisku i emailu. Wyświetl te dane na ekranie w formie tabelki.
#56. W osobnym module domain stwórz klasę Author z polami first_name,last_name, email (i ustawionymi w polach wartościami)
#Następnie spowoduj by kontroler ekranu /about przekazywał do widoku obiekt tej klasy. Na poziomie widoku
#zaktualizuj kod w taki sposób by wyświetlane były dane z przekazanego obiektu
#57. Dodaj usługę sieciową która zwróci zserializowaną postać obiektu klasy Author

#Flask,Django,FastApi, Pyramid
#uWSGI
#https://www.pythonanywhere.com/

#przerwa do 15:36