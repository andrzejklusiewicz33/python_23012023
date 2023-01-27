from flask import Flask, render_template, request
from domain import *
import employees_dao as edao
import products_dao as pdao

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/show_products')
def show_products():
    return render_template("show_products.html",products=pdao.get_all())

@app.route('/products.json')
def products_json():
    return [e.serialize() for e in pdao.get_all()]

@app.route('/show_product_details')
def show_product_details():
    id=request.args.get('id')
    return render_template("show_product_details.html",product=pdao.get_one(id))


@app.route('/show_employees')
def show_employees():
    return render_template("show_employees.html", employees=edao.get_all())

@app.route('/employees.json')
def employees_json():
    return [e.serialize() for e in edao.get_all()]

@app.route('/show_employee_details')
def show_employee_detais():
    id=request.args.get('id')
    return render_template("show_employee_details.html",employee=edao.get_one(id))

@app.route('/add_employee')
def add_employee():
    return render_template("add_employee.html")

@app.route('/about')
def about():
    return render_template("about.html", author=Author())


@app.route('/about.json')
def about_json():
    return Author().serialize()


@app.route("/fruit.json")
def fruit_json():
    fruit = Fruit()
    return fruit.serialize()


@app.route('/examples')
def examples():
    data = ['python', 'java', 'javascript', 'R']
    import os
    print("zalogowany="+os.getlogin( ))
    return render_template("examples.html", fruit=Fruit(), data=data)


# @app.route('/examples')
# def examples():
#     print("Ktoś wszedł na ekran /examples....")
#     f="banana"
#     c="yellow"
#     return render_template("examples.html",fruit=f,color=c)


if __name__ == '__main__':
    app.run(debug=True, port=80)

# 52. Dodaj obsługę ekranów pod adresami /show_products /show_employees /about
# Po wejściu na każdy z tych ekranów powinien pojawić się komunikat z tekstem jednoznacznie identyfikujacym na jakiej podstronie jesteściee
# 53. Zadbaj o to, by wszystkie ekrany były obsługiwane przez osobne pliki html
# 54. Do wszystkich ekranów dodaj działającce menu
# 55. Do widoku ekranu /about przekaż informację o swoim imieniu, nazwisku i emailu. Wyświetl te dane na ekranie w formie tabelki.
# 56. W osobnym module domain stwórz klasę Author z polami first_name,last_name, email (i ustawionymi w polach wartościami)
# Następnie spowoduj by kontroler ekranu /about przekazywał do widoku obiekt tej klasy. Na poziomie widoku
# zaktualizuj kod w taki sposób by wyświetlane były dane z przekazanego obiektu
# 57. Dodaj usługę sieciową która zwróci zserializowaną postać obiektu klasy Author

# 58. Stwórz w domain.py klasę Product która będzie reprezentowała encje produktu. Przekaż z kontrolera (w app.py)
# kilka przykładowych obiektów tej klasy do widoku /show_products
# Na poziomie widoku wydrukuj te dane w postaci tabelki (ale bez pol description i stock)
# 59. Oddeleguj generowanie listy produktów do funkcji get_all() w osobnym module products_dao
# 60. Do aplikacji dodaj usługę sieciową zwracającą listę wszystkich produktów jako json. DOdaj też do menu link do tej usługi
# 61. Zadbaj o to by dane na ekranie listy produktów pochodziły z bazy

# 62. Zadbaj o to by dane służące do łączenia się z bazą (host,uzytkownik, haslo etc.) znajdowaly się w pliku settings.py

# Flask,Django,FastApi, Pyramid
# uWSGI
# https://www.pythonanywhere.com/

# przerwa do 15:36
#przerwa do 10:11

#nowa linia

#przerwa do 11:31

#63. Na liście produktów dodaj do każdego produktu w kolumnie "Akcje" link do ekranu szczegółów produktu
#Po kliknięciu na ten link powinien się pojawić ekran z menu i odpowiednim nagłówkiem, a w konsoli
#powinna się pojawić informacja o id produktu którego szczegóły chcemy podglądać

#64. Na ekranie szczegółów produktu wyświetl jakieś fejkowe
#dane przekazane z kontrolera (obiekt klasy Product)

#65. Spraw by dane na ekranie szczegółów produktu pochodziły z bazy...

#przerwa obiadowa do 13:12

#66. Zadbaj o to by na ekranie szczegółów produktu jeśli stan magazynowy wynosi zero to
#niech ten stan magazynowy będzie wyświetlany na czerwono pogrubiony,
#a jeśli więcej niż 0 to na zielono pogrubiony


#TinyMCE

#67. Na ekranie listy produktów dodaj link do ekranu dodawania produktu.
#Spowoduj by po kliknięciu na ten link wyświetlił się formularz który będzie
#służył do wprowadzania danych o produkcie.