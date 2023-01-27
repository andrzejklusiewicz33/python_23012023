from flask import Flask, render_template, request,redirect
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

@app.route('/add_product')
def add_product():
    return render_template("add_product.html")

@app.route('/add_product',methods=['POST'])
def add_product_post():
    name=request.form['name']
    price=request.form['price']
    description=request.form['description']
    stock=request.form['stock']
    product=Product(None,name,price,description,stock)
    pdao.save(product)
    return redirect("/show_products")

@app.route('/delete_product')
def delete_product():
    id=request.args.get('id')
    product=pdao.get_one(id)
    return render_template("delete_product.html",product=product)

@app.route('/delete_product',methods=['POST'])
def delete_product_post():
    id=request.args.get('id')
    print(f'kasowanie produktu o id={id}')
    return redirect('/show_products')

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

@app.route('/add_employee',methods=['POST'])
def add_employee_post():
    data=request.form
    employee=Employee(None,data['first_name'],data['last_name'],data['salary'],data['description'])
    edao.save(employee)
    return redirect("/show_employees")

@app.route('/delete_employee')
def delete_employee():
    id=request.args.get('id')
    employee=edao.get_one(id)
    return render_template("delete_employee.html",employee=employee)


@app.route('/delete_employee',methods=['POST'])
def delete_employee_post():
    id=request.args.get('id')
    edao.delete(id)
    return redirect('/show_employees')


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

#68. Dodaj obsługę zdarzenia POST na formularzu dodawania produktu.
#Obsługa tego zdarzenia ma sprowadzać się do odebrania danych z formularza, wypisania
#ich na konsoli i przekierowania  na listę produktów

#PRZERWA DO 14:40

#69. Zadbaj o to, by po zatwierdzeniu formularza dodawania produktu tworzony był
#obiekt klasy Product. Stwórz w products_dao funkcję save i przekaż do niej
#stworzony obiekt. Funkcja save ma nam wypisać na konsoli zawartość obiektu który
#będzie przez nią w przyszłości utrwalany

#70. Zadbaj o to by funkcja save w products_dao faktycznie zapisywala dane do bazy...

#71. Dodaj do listy produktow linki prowadzace do ekranu kasowania produktu.
#Ekran kasowania produktu powinien pytac czy chcesz skasowac ten produkt
#z podaniem nazwy produktu ktory będzie kasowany.


#72. Dodaj obsługę post dla kasowania produktu. Obsługa ma polegać na wypisaniu na konsoli id produktu
#ktorego będziemy kasować i przekierowaniu na liste produktów.

#reportlab

#https://getbootstrap.com/

#73. Zadbaj o to by ekran kasowania produktu faktycznie kasował produkt z bazy...