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
    data=[]
    e1=Employee(1,'Andrzej','Klusiewicz',12345,"programmer z zawodu i pasji")
    data.append(e1)
    e2=Employee(2,'Marian','Paździoch',8000,"Programista Front-End")
    data.append(e2)
    e3=Employee(3,'Babka','Kiepska',10000,"Babka dawaj rentę!")
    data.append(e3)
    return render_template("show_employees.html",employees=data)

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
    data=['python','java','javascript','R']
    return render_template("examples.html",fruit=Fruit(),data=data)

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

#58. Stwórz w domain.py klasę Product która będzie reprezentowała encje produktu. Przekaż z kontrolera (w app.py)
#kilka przykładowych obiektów tej klasy do widoku /show_products
#Na poziomie widoku wydrukuj te dane w postaci tabelki (ale bez pol description i stock)


#Flask,Django,FastApi, Pyramid
#uWSGI
#https://www.pythonanywhere.com/

#przerwa do 15:36