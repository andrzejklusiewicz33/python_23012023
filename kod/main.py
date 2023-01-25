# test
# test2
# print("siema!")
# print('siema!')
#
# for x in range(10):
#     print(f'x={x}')
# print('koniec')

# formatowanie kodu ctrl+alt+L
# zakomentowywanie i odkomentowywanie ctrl+/

# print("Siema!")
# print('Siema!')
# print("Mc'Donalds")
# int x=1 #java
# x=1
# x=10
# y=20
# z=x*y
# print(z)
# print(x,y,z)
# owoc="banan"
# kolor="żółty"
# cos='nietoperz'
# print(owoc)
# print("owoc="+owoc)
# print("owoc={} kolor={}".format(owoc,kolor,cos))
# owoc='banan'
# print("owoc="+owoc)
# print('owoc={}'.format(owoc))
# print(f'owoc={owoc}')

# owoc='banan'
# pi=3.14
# x=10
# print(owoc,type(owoc))
# print(pi,type(pi))
# print(x,type(x))
#
# pi=3.14
# print('pi='+pi)

#
# pi='3.14'
# print('pi='+pi)
# print(pi*10)
# print("hajs"*1000)
#
# x=10
# print('x='+str(x))
# print('x={} x={}'.format(x,x))
# print(f'x={x}')
#
# owoc=input('podaj swój ulubiony owoc:')
# print(f'Twój ulubiony owoc to {owoc}')


# owoc=input('podaj swój ulubiony owoc:\n')
# print(f'Twój ulubiony owoc to {owoc}')


# 1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
# wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"


# get_all_pracownicy #fuuuuu

# first_name=input('podaj imię:\n')
# last_name=input('podaj nazwisko:\n')
# print(f"Witaj {first_name} {last_name}!")
#
# public class Main {
#     public static void main(String args[]){
#         System.out.println("WTF????");
# }
# }

# print('OMG!')

# PEP8

# import this


# x=input('podaj x:\n')
# print(x,type(x))
# print(x/10)

# x=float(  input('podaj x:\n')   ) #float,int,str
# print(x,type(x))
# print(x*1000)
# x=10
# y=3
# print( round(x/y,2) )
#
# f=float(input('podaj f:\n'))
# print(f)

# print(pow(10,4))

# 2. BMI= masa/(wzrost*wzrost) . Napisz program który odbierze od użytkownika jego masę
# w kilogramach i wzrost w metrach, wyliczy i wypisze BMI.

# height=float(input('podaj wzrost w metrach:\n'))
# weight=float(input('podaj masę w kilogramach:\n'))
# bmi=round(weight/pow(height,2),2)
# print(f'bmi={bmi}')


# przerwa do 11:51

# x=1
# if 1==1:
#     pass

# x=0
# if x>5:
#     print('warunek prawdziwy')
#     print('x jest większe od 5')
# print('koniec')

# x=10
# if x>5:
#     print('warunek prawdziwy')
# else:
#     print('warunek nie prawdziwy')
#
# x=3
# if x==1:
#     print('jeden')
# elif x==2:
#     print('dwa')
# elif x==3:
#     print('trzy')
# elif x==4:
#     print('cztery')
# else:
#     print('poza zakresem')

# 3. Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to chcemy wyświetlić tę wartość
# z informacją "wartość dodatnia", jeśli zero to wyświetlamy z informacją "równe zero",
# jeśli ujemna to wyświetlamy "wartość ujemna".


# x=float(input('dej liczbę:\n'))
# if x>0:
#     print(f'{x} jest dodatnie')
# elif x==0:
#     print(f'{x} jest zerem')
# else:
#     print(f'{x} jest ujemne')


# 4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#  wyświetlił nam również odpowiedni opis wg skali z Wikipedii.


#
#
# height=float(input('podaj wzrost w metrach:\n'))
# weight=float(input('podaj masę w kilogramach:\n'))
# bmi=round(weight/pow(height,2),2)
# print(f'bmi={bmi}')
#
# if bmi<=18.5:
#     print('za chudy')
# elif bmi<25:
#     print('wartosc prawidlowa')

#
# height=float(input('podaj wzrost w metrach:\n'))
# weight=float(input('podaj masę w kilogramach:\n'))
# bmi=round(weight/pow(height,2),2)
# print(f'bmi={bmi}')
#
# if bmi<16:
#     print('wygłodzenie')
# elif bmi<17:
#     print('wychudzenie')
# elif bmi<18.5:
#     print('niedowaga')
# elif bmi<25:
#     print('masa ok')
# elif bmi<30:
#     print('nadwaga')
# elif bmi<35:
#     print('I stopień przypakowania')
# elif bmi<40:
#     print('II stopień przypakowania')
# else:
#     print('III stopień przypakowania')
#
# while 1==1:
#     pass
#
# while True:
#     pass

# for x in range(10):
#     print(f'siema po raz {x}!')
#
# for x in range(1,11):
#     print(f'siema po raz {x}!')

#
# for x in range(1,11):
#     print(x/10)

#
# for x in range(1,11):
#     print(x*10)
#     print('--------')
# print('koniec x=',x)


# 5. Wyświetl 20 kolejnych potęg liczby 2


# for koza in range(1,21):
#     print(koza, pow(2,koza))
#
# x=int(input('podaj krotność:\n'))
# if x>0:
#     for i in range(1,x+1):
#         print(i)
#
# for x in range(-10,11):
#     if x<0:
#         print(f'{x} jest ujemne')
#     elif x==0:
#         print(f'{x} jest zerem')
#     else:
#         print(f'{x} jest dodatnie')

# 6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
#  parzysta czy nieparzysta
#
# print(11%2)
#
# if 11%2==0:
#     print('parzysta...')
# else:
#     print('nieparzysta...')

# for x in range(1,101):
#     if x%2==0:
#         print(f'{x} jest parzysta')
#     else:
#         print(f'{x} jest nieparzysta')


# przerwa obiadowa do 13:10

# 7.  Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
# - kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakladamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
# oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
# Kapitalizacja comiesięczna

# im=int(input('dej...'))
#
# money=100000
# interest=0.08
# len=24
# for m in range(1,len+1):
#     money=round(money+(money*interest/12),2)
#     print(m,money)

#
# money=100000
# interest=-0.2
# len=60
# for m in range(1,len+1):
#     money=round(money+(money*interest/12),2)
#     print(m,money)


#
# money=100000
# interest=0.08
# len=24
# for m in range(1,len+1):
#     money=round(money+(money*interest/12),2)
#     print(m,money)


# import random
# print(random.randint(1,100))
# print(random.random())
# x=random.randint(1,100)
# print(x)

# x=1
# while x<=100:
#     print(x)
#     x=x*2


# 8.Napisz program który będzie dodawał kolejne losowe wartości z zakresu
# od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci wiekszej od wartosci podanej przez uzytkownika

# import random
# max=int(input('podaj maksymalną wartość:\n'))
# sum=0
# while sum<max:
#     sum=sum+random.randint(1,10)
#     print(sum)
#
# import random
# max=int(input('podaj maksymalną wartość:\n'))
# sum=0
# while sum<max:
#     print(sum)
#     sum = sum + random.randint(1, 10)


# import random
# max=int(input('podaj maksymalną wartość:\n'))
# sum=0
# while sum<max:
#     print(sum)
#     #sum = sum + random.randint(1, 10)
#     sum += random.randint(1, 10)
#

# x=x+1
# x+=1
# x=x/2
# x/=2
#
# for wiersz in cursor:
#     print(wiersz)

# tekst="siała baba mak i dostała 10 lat bo nie płaciła VAT"
# print(tekst.upper())
# print(tekst.lower())
# print(tekst.title())
# print(tekst.replace('a','X'))
# print(tekst.replace('a','X').replace('A','X'))
# print(tekst.lower().replace('a','X'))
# print(tekst.upper().replace('A','X'))
# print(tekst)
# tekst=tekst.upper()
# print(tekst)
# print( len(tekst) )
# lista=[1,2,3,4,5]
# print(len(lista))
# print(tekst.len()) #fuuuuu

#
# tekst="siała baba mak i dostała 10 lat bo nie płaciła VAT"
# print(tekst.count('a'))
# print(tekst.lower().count('a'))

# if 'bab' in tekst:
#     print('jest')
# else:
#     print('nie ma')
#
# if 'BAB'.lower() in tekst.lower():
#     print('jest')
# else:
#     print('nie ma')
#

# tekst="siała baba mak i dostała 10 lat bo nie płaciła VAT"
# tekst="           abc      dupa\n"
# print(tekst)
# print('-----')
# print(tekst.strip())
# print(tekst.strip().replace(' ',''))

# tekst="siała baba mak i dostała 10 lat bo nie płaciła VAT"
# for l in tekst:
#     print(l)
#
# tekst='pinionszki'
# print(tekst*100)
#
# if "Java">"Python":
#     print('chyba Cię gnie...')
# else:
#     print('no rejczel..')
#

# tekst="siała baba mak i dostała 10 lat bo nie płaciła VAT"
# print(tekst[0:15])
# print(tekst[0:15:2])
# print(tekst[0:15].upper().replace('A','X'))

# 9.  Napisz program który przyjmie od użyszkodnika ciąg tekstowy a następnie usunie z niego znaki ,.!? i
# wyświetli powiększony do dużych liter tekst na konsoli

# text=input('Dej mnie teksta:\n')
# print(text.replace(',','').replace('.','').replace('!','').replace('?','').upper())

# text=input('Dej mnie teksta:\n')
# niechciane=[',','.','?','!']
# for n in niechciane:
#     text=text.replace(n,'')
# print(text.upper())

# przerwa do 14:30

# for linia in open('linie.txt'):
#     print(linia)

# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(linia)

#
# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(len(linia),linia)


# for linia in open('tadzio.txt',encoding='utf-8'):
#     print(len(linia.strip()),linia.strip())


# 10. Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego nazwę poda użytkownik
#
# for line in open('tadzio.txt',encoding='utf-8'):
#     if len(line.strip())>0:
#         print(len(line.strip()),line.strip())
#
# all=open('tadzio.txt',encoding='utf-8').read()
# print(all.replace('a','X'))

#
# all=open('tadzio.txt',encoding='utf-8').read(100)
# print(all.replace('a','X'))

# 11. Napisz program który zliczy ilość wystąpień małej lub dużej wersji ciagu tekstowego podanego
# przez użytkownika w pliku którego nazwę również poda użytkownik.
#
# phrase=input('podaj poszukiwaną frazę:\n')
# file_name=input('podaj nazwę pliku:\n ')
# print(  open(file_name,encoding='utf-8').read().lower().count(phrase.lower())  )

#
# phrase=input('podaj poszukiwaną frazę:\n')
# file_name=input('podaj nazwę pliku:\n ')
# all= open(file_name,encoding='utf-8').read()
# print( all.lower().count(phrase.lower())  )


# 12. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
# poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
#  linie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka
#   po  odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
#  i w jakim pliku szuka. Wyszukiwarka powinna być nieczula na wielkosc liter.
#
# if "BABA".lower() in "siała baba mak".lower():
#     print('jest')
# else:
#     print('niet!')
#
# nl=0
# for linia in open(....):
#     nl+=1
#
# all=open('tadzio.txt',encoding='utf-8').read()
# for linia in all:
#     print(linia)
#
# tekst="abcd"
# for t in tekst:
#     print(t)

# file_name=input('podaj nazwę pliku:\n')
# phrase=input('podaj szukaną frazę:\n')
# x=0
# for line in open('tadzio.txt',encoding='utf-8'):
#     x+=1
#     if phrase.lower() in line.lower():
#         print(x,line.strip())

#
# lines_count = len(open('tadzio.txt', encoding='utf-8').readlines())
# print(f'liczba linii w pliku 1 = {lines_count}')
# lines_count2 = len(open('tadzio2.txt', encoding='utf-8').readlines())
# print(f'liczba linii w pliku 1 = {lines_count2}')
# if lines_count == lines_count2 and lines_count > 0:
#     print('liczba linii taka sama. Pracujemy....')
#     file1 = open('tadzio.txt', encoding='utf-8')
#     file2 = open('tadzio2.txt', encoding='utf-8')
#     for x in range(1, lines_count + 1):
#         line1=file1.readline()
#         line2=file2.readline()
#         if line1!=line2:
#             print(line1.strip(),' | ',line2.strip())
# else:
#     print('różna liczba linii. Nie pracujemy')
#
#


# my_list=[]
# print(type(my_list))
# my_tuple=()
# print(type(my_tuple))
#
# my_list=[]
# my_list=list()
# my_list=[1,2,'nietoperz',3,4,5,'koza']
# my_list.append(33333)
# for e in my_list:
#     print(e)

# import random
# my_list=[]
# for x in range(10):
#     my_list.append(random.randint(1,100))
# print(my_list)
# for e in my_list:
#     print(e)

# 13. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.
#
# my_list=[]
# for p in range(1,11):
#     my_list.append(pow(2,p))
# print(my_list)
# for ml in my_list:
#     print(ml)
#
# for f in [pow(2,e) for e in range(1,11)]: print(f)
#
# my_list = [1, 5, 22, 2, 33, 190, -89]
# print(max(my_list))
# print(min(my_list))
# print(sum(my_list))
# print(sum(my_list) / len(my_list))

# 14. Stwórz listę zawierającą 100 losowych liczb z zakresu dowolnego
# i wyświetl różnicę pomiędzy największą a najmniejszą wartością w tej liście...

# import random
# my_list=[]
# for x in range(100):
#     my_list.append(random.randint(1,100))
# print(max(my_list)-min(my_list),max(my_list),min(my_list))
#
# import random
# my_list=[random.randint(1,100) for x in range(100)]
# print(max(my_list)-min(my_list),max(my_list),min(my_list))
#
# import random
# print(random.random()*1000)

# my_list=[1,2,3]
# print(my_list)
# print(*my_list)
#
# def function(*args):
#     pass
#
# function(1,2,3,4)
# function(*my_list)

# list1=[1,2,3,4]
# list2=[5,6,7,8]
# result=[list1,list2]
# print(result)
# result=[*list1,*list2]
# print(result)


# list1=[1,2,3,4]
# list2=[5,6,7,8]
# result=[]
# result.append(list1)
# result.append(list2)
# print(result)

# list1=[1,2,3,4]
# list2=[5,6,7,8]
# result=[]
# result.extend(list1)
# result.extend(list2)
# print(result)

#
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list1.extend(list2)
# print(list1)


# list1=[1,2,3,4]
# list2=list1
# list1.clear()
# print(list1)
# print(list2)

#
# list1=[1,2,3,4]
# list2=list1.copy()
# list1.clear()
# print(list1)
# print(list2)


# 15. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista)

# import random
#
# list1 = []
# list2 = []
# for x in range(10):
#     list1.append(random.randint(1, 10))
#     list2.append(random.randint(1, 10))
#
# result=[*list1,*list2]
# print(result)
# list1.extend(list2)
# print(list1)
#
# lista=[]
# for x in range(1,11):
#     podlista=[x,x*100]
#     lista.append(podlista)
# print(lista)


# lista=[]
# for x in range(1,11):
#     lista.append([x,x*100])
# print(lista)
# for e in lista:
#     print(e)

# 16. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
# print(pow(2,10))
#
# list=[]
# for x in range(1,11):
#     sublist=[x,pow(2,x)]
#     list.append(sublist)
#
# print(list)
# for e in list:
#     print(e)


#
# list=[]
# for x in range(1,11):
#     list.append([x,pow(2,x)])
#
# print(list)
# for e in list:
#     print(e)
#
# lista=[]
# for x in range(1,11):
#     lista.append(x)
#
# print(lista)
#
# lista=[x for x in range(1,11)]
# print(lista)
#
# print([x for x in range(1,11)])


# lista=[x*1000 for x in range(1,11)]
# print(lista)

#
# lista=[]
# for x in range(1,101):
#     if x%2==0:
#         lista.append(x)
#
# print(lista)

# lista=[x for x in range(1,101) if x%2==0 ]
# print(lista)

# print([x for x in range(1,101) if x%2==0 ])
#
# print([x*100 for x in range(1,101) if x%2==0 ])

# import random
# lista=[]
# for x in range(1,11):
#     lista.append(random.randint(1,10))
# print(lista)
#
# import random
# lista=[random.randint(1,10) for e in range(1,11)]
# print(lista)
#
# import random
# print([random.randint(1,10) for e in range(1,11)])

# import random
# lista1=[]
# for x in range(1,11):
#     lista1.append(random.randint(1,10))
# print(lista1)
#
# lista2=[]
# for e in lista1:
#     if e%2==0:
#         lista2.append(e)
# print(lista2)

# import random
# lista1=[random.randint(1,10) for x in range(10)]
# lista2=[e for e in lista1 if e%2==0]
#
# print(lista1)
# print(lista2)
#
# import random
# lista2=[e for e in [random.randint(1,10) for x in range(10)] if e%2==0]
#
# print(lista2)
#
# lista=[random.randint(1,10) for x in range(10) if x%2==0]
# print(lista)

# select * from products where cena<100 and

# 17. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2

# lista=[]
# for x in range(1,11):
#     p=pow(2,x)
#     lista.append(p)
# print(lista)
#
#
# lista=[]
# for x in range(1,11):
#     lista.append(pow(2,x))
# print(lista)
#
# lista=[pow(2,x) for x in range(1,11)]
# print(lista)
#
# print([pow(2,x) for x in range(1,11)])

# 18. Korzystając z list składanych wygeneruj listę 10 elementow której każdy element również będzie listą.
# Pierwszy element tej podlisty to numer potegi, a drugi to wartosc tej potegi dla liczby 2
#
# result=[ [e,pow(2,e)] for e in range(1,11)]
# print(result)
# for r in result:
#     print(r)
#
# print([ [e,pow(2,e)] for e in range(1,11)])

# przerwa do 10:15

# linia='1;Andrzej;Klusiewicz'
# lista=linia.split(';')
# print(lista)
# print(lista[2])
# print(lista[2].replace('u','X'))


# linia='1;Andrzej;Klusiewicz\n'
# lista=linia.strip().split(';')
# print(lista)
# print(lista[2])
# print(lista[2].replace('u','X'))
#
# for linia in open('dane.csv',encoding='utf-8'):
#     print(linia.strip())


# 19. Napisz program który z pliku dane.csv wyświetli powiekszone imiona i nazwiska oraz wzrost i masę

# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     print(lista[1].upper(),lista[2].upper(),lista[3],lista[4])
#
# result=[]
# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     result.append(lista)
#
# for r in result:
#     print(r)

#
# result=[]
# for linia in open('dane.csv',encoding='utf-8'):
#     result.append(linia.strip().split(';'))
#
# for r in result:
#     print(r)

# 20. Korzystajac z list skladanych zaladuj do listy zawartosc pliku dane.csv w taki sposób
# by linie oczyścic z bialych znaków i rozbić na listy. Każdy z elementów listy sam
# powinien byc listą. Następnie przeiteruj po wyniku i wyświetl wszystkie elementy listy   linia po linii.

#
# result=[]
# for linia in open('dane.csv',encoding='utf-8'):
#     result.append(linia.strip().split(';'))
#
# for r in result:
#     print(r)
#

#
# result=[linia for linia in open('dane.csv',encoding="utf-8").readlines()]
# for r in result:
#     print(r)


#
# for r in [linia for linia in open('dane.csv',encoding="utf-8")]:
#     print(r)

# result=[linia.strip().split(';') for linia in open('dane.csv',encoding="utf-8")]
# for r in result:
#     print(r)

# for r in [linia.strip().split(';') for linia in open('dane.csv',encoding="utf-8")]:
#     print(r[3],type(r[3]))
#
# for r in [linia.strip().split(';') for linia in open('dane.csv',encoding="utf-8")]:
#     print(float(r[3])/2)
#
# x=1.4
# if type(x)==int:
#     print('to jest liczba całkowita')
# elif type(x)==float:
#     print('to jest liczba zmiennoprzecinkowa')
#

# x='koza'
# try:
#     print(float(x))
# except ValueError:
#     print('to nie jest liczba, nie da się tego rzutować')

# 21. Dla każdego wpisu w pliku dane.csv wyświetl na konsoli dane o
#   id, imieniu,nazwisku, wzroscie,masie oraz obliczonym bmi zawodnika


#
# for r in [linia.strip().split(';') for linia in open('dane.csv',encoding="utf-8")]:
#     bmi=r[4]/pow(r[3],2) #nie zadziala bo brak rzutowania na liczbę (wartości są tekstem)
#     print(*r,bmi)
#
# for r in [linia.strip().split(';') for linia in open('dane.csv',encoding="utf-8")]:
#     bmi=float(r[4])/pow(float(r[3]),2)
#     print(*r,bmi)
#
# for r in [linia.strip().split(';') for linia in open('dane.csv',encoding="utf-8")]:
#     bmi=round(float(r[4])/pow(float(r[3]),2),2)
#     print(*r,bmi)

#
# for r in [linia.strip().split(';') for linia in open('dane.csv',encoding="utf-8")]:
#     print(*r,round(float(r[4])/pow(float(r[3]),2),2))

# for r in [linia.strip().split(';') for linia in open('dane.csv',encoding="utf-8")]:
#     r.append(round(float(r[4])/pow(float(r[3]),2),2))
#     print(*r)
#
# lista=[1,6,32,2,3,55,4]
# print(lista)
# lista.sort()
# print(lista)

#
# lista=[1,6,32,2,3,55,4]
# print(lista)
# lista.sort()
# lista.reverse()
# print(lista)

#
# lista=[1,6,32,2,3,55,4]
# print(lista)
# lista.sort(reverse=True)
# print(lista)


# lista=[1,6,32,2,3,55,4]
# print(sorted(lista))
# print(lista)

# lista=[1,6,32,2,3,55,4]
# print(sorted(lista,reverse=True))
# print(lista)
#
# lista=[1,6,32,2,3,55,4]
# posortowane=sorted(lista)
# print(lista)
# print(posortowane)


# lista=[1,6,32,2,3,55,4]
# posortowane=sorted(lista,reverse=True)
# print(lista)
# print(posortowane)


# lista=[1,6,32,2,3,55,4]
# posortowane=sorted(lista)
# odwrocone_posortowane=list(reversed(posortowane))
# print(lista)
# print(posortowane)
# print(odwrocone_posortowane)
#
# lista=['C','A','B']
# print(sorted(lista))
# lista.sort()
# print(lista)

#
# lista=['C','A','B','1']
# print(sorted(lista))
# lista.sort()
# print(lista)

# 22.Wygeneruj listę 10 elementów o losowej wartości liczbowej,
# posortuj listę (malejąco) i wyświetl jej zawartość linia po linii

# import random
# result=[random.randint(1,100) for e in range(10)]
# print(result)
# print(sorted(result,reverse=True))
# result.sort(reverse=True)
# print(result)
#
# import random
# result=[random.randint(1,100) for e in range(10)]
# result.sort()
# result.reverse() #większa złożonośc obliczeniowa w stosunku do .sort(reseversed=True)
# print(result)

# przerwa do 11:27
#
# lista=[
#     [2,'C'],
#     [1,'D'],
#     [3,'B'],
#     [4,'A']
# ]
# lista.sort()
# print(lista)

# from operator import itemgetter
# lista=[
#     [2,'C'],
#     [1,'D'],
#     [3,'B'],
#     [4,'A']
# ]
# lista.sort(key=itemgetter(1))
# print(lista)

#
# lista=[
#     [2,'C'],
#     [1,'D'],
#     [3,'B'],
#     [4,'A']
# ]
# lista.sort(key=lambda e:e[1])
# print(lista)


# class Person:
#     first_name=None
#     last_name=None
#     def __init__(self,fn,ln):
#         self.first_name=fn
#         self.last_name=ln
#     def __str__(self):
#         return str(self.__dict__)
#
# p1=Person('Andrzej','Klusiewicz')
# p2=Person('Natalia','Gmurczyk')
# p3=Person('Monika','Bożko')
# list=[p1,p2,p3]
# list.sort(key=lambda p:p.last_name)
# for e in list:
#     print(e)

# 23. Wczytaj do listy kolejne wiersze z pliku dane.csv.
# Dane posortuj po nazwiskach i wyswietl linia po linii na konsoli.

# data=[line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]
# for d in data:
#     print(d)
#
# data=[line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]
# data.sort(key=lambda e:e[2])
# for d in data:
#     print(d)


# from operator import itemgetter
# data=[line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]
# data.sort(key=itemgetter(2))
# for d in data:
#     print(d)

# 24. Wyświetl na konsoli linia po linii dane z pliku dane.csv ale posortowane  malejąco wg. bmi
#
# data=[line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]
# for d in data:
#     bmi=round(float(d[4])/pow(float(d[3]),2),2)
#     d.append(bmi)
#     print(d)


# data=[line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]
# for d in data:
#     d.append(round(float(d[4])/pow(float(d[3]),2),2))
# data.sort(key=lambda e:e[5],reverse=True)
# for d in data:
#     print(d)

#
# import os
# os.mkdir("d:\\whatever")

# import os
# for e in os.walk('d:\\'):
#     print(e)
#
# import os
# for e in os.walk('d:\\'):
#     print(e[0])

#
# import os
# for e in os.walk('d:\\'):
#     print(e)

#
# import os
# for e in os.walk('d:\\'):
#     print(f"########  KATALOG {e[0]}:")
#     for k in e[1]:
#         print(f'podkatalog {k}')
#     for p in e[2]:
#         print(f'plik {p}')

# string="siała baba mak"
# if "baba" in string:
#     print('jest w stringu')
# else:
#     print('nie ma w stringu')
#
# lista=string.split()
# print(lista)
# if "bab" in lista:
#     print('jest w liście')
# else:
#     print('nie ma w liście')
#
# for e in lista:
#     if 'bab' in e:
#         print(f'jest w {e}')
#     else:
#         print(f'nie ma w {e}')

# 25. Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i katalog startowy.
# Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi zawierajace w nazwie szukaną
# frazę - wraz ze ścieżkami. Wyszukiwarka ma być nieczuła na wielkość liter
#
# szukane="OrAcLe"
# import os
# for e in os.walk('e:\\'):
#     katalogi=e[1]
#     for k in katalogi:
#         if szukane.lower() in k.lower():
#             print(e[0],k)


# szukane="OrAcLe"
# import os
# for e in os.walk('e:\\'):
#     for k in e[1]:
#         if szukane.lower() in k.lower():
#             print(os.path.join(e[0],k))
#     for p in e[2]:
#         if szukane.lower() in p.lower():
#             print(os.path.join(e[0],p))

# import os
# szukane=input('podaj szukaną frazę:\n')
# katalog_startowy=input('podaj katalog startowy:\n')
# for e in os.walk(katalog_startowy):
#     for k in e[1]:
#         if szukane.lower() in k.lower():
#             print(os.path.join(e[0],k))
#     for p in e[2]:
#         if szukane.lower() in p.lower():
#             print(os.path.join(e[0],p))

# przerwa obiadowa do 13:10

# lista=[1,2,3]
# krotka=(1,2,3)
# print(lista[1])
# print(krotka[1])
# lista.append(4)
# krotka.append(4) #nie ma

# krotka=(5,4,1,6,2)
# #krotka.sort() #nie ma
# print(sorted(krotka))
# posortowane=sorted(krotka)
# print(posortowane)

# krotka=(5,4,1,6,2)
# lista=list(krotka)
# print(lista,type(lista))
# krotka2=tuple(lista)
# print(krotka2,type(krotka2))
#
# krotka=(5,4,1,6,2)
# lista=list(krotka)
# lista.sort()
# krotka=tuple(lista)
# print(krotka)

# 26. Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10,
# druga 10 losowych liczb zakresu 11-20. Stwórz trzecią krotkę która ma zawierać dane z obu krotek.
# Trzecią krotkę wypisz na konsoli

# import random
# k1=tuple([random.randint(1,10) for e in range(10)])
# k2=tuple([random.randint(11,20) for e in range(10)])
# print(k1,type(k1))
# print(k2,type(k2))
# k3=(*k1,*k2)
# print(k3,type(k3))

# 27. Napisz kod ktora wyświetli w postaci listy krotek zawartość pliku dane.csv

# result=[line.strip().split(';') for line in open('dane.csv',encoding='utf-8')]
# for r in result:
#     print(r)


#
# result=[tuple(line.strip().split(';')) for line in open('dane.csv',encoding='utf-8')]
# for r in result:
#     print(r)


# for r in [tuple(line.strip().split(';')) for line in open('dane.csv',encoding='utf-8')]: print(r)

# z={1,1,1,1,1,1,1,5,5,5,5,5,5,5,5,2,2,2,2,2,2,3,3,3,3,3,3,3,3}
# print(z)
#
# z1={1,2,3,4}
# z2={3,4,5,6}
# print(z1.intersection(z2))
# print(z1.union(z2))
# print(z1.difference(z2))
# print(z2.difference(z1))

# lista=[1,2,1,1,1,2,2,2,2,2,3,4,1,1,2,2,3,3,4]
# z=set(lista)
# print(z)
# lista=list(z)
# print(lista)

# z=set()
# z.add(1)
# z.add(1)
# z.add(1)
# z.add(2)
# print(z)
#
# lista=list(set([1,2,1,1,1,2,2,2,2,2,3,4,1,1,2,2,3,3,4]))
# print(lista)

# 28. Wygeneruj dwa zestawy, dodaj do nich po 20
# (w przypadku duplikatów lista może być mniejsza niż 20 elementów)
# losowych liczb z zakresu 1-40. Wyswietl ich sumę, różnicę i część wspólną

# import random
# z1=set([random.randint(1,40) for e in range(20)])
# z2=set([random.randint(1,40) for e in range(20)])
# print(z1,f'len(z1)={len(z1)}')
# print(z2,f'len(z1)={len(z2)}')

# import random
# z1 = set()
# z2 = set()
# for _ in range(20):
#     z1.add(random.randint(1, 40))
#     z2.add(random.randint(1, 40))
# print(z1,f'len(z1)={len(z1)}')
# print(z2,f'len(z1)={len(z2)}')

# import random
# z1=set([random.randint(1,40) for e in range(20)])
# z2=set([random.randint(1,40) for e in range(20)])
# print(z1,f'len(z1)={len(z1)}')
# print(z2,f'len(z1)={len(z2)}')
# print("suma=",z1.union(z2))
# print("część wspólna=",z1.intersection(z2))
# print("z1-z2=",z1.difference(z2))
# print("z2-z1=",z2.difference(z1))


#29. Zduplikuj jeden z wierszy w pliku dane.csv.
# Napisz kod który zwróci do postaci listy krotek zawartość tego pliku z danymi bez powtórek.

#unhashable type list -- brakuje rzutowania elementów listy na krotki

#
# result=list(set([tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]))
# print(result)
# for r in result:
#     print(r,type(r))

#przerwa do 14:23

#
# sl=dict()
# sl['string']='value 1'
# sl['numeric']=1234
# sl['list']=[1,2,3,4]
#
# #print(sl['numeric'])
#
# for k in sl:
#     print(k,sl[k])
#
# for k in sl.keys():
#     print(k,sl[k])
#
# for v in sl.values():
#     print(v)


#30. Stwórz plik ustawienia.conf i umieść w nim poniższe dane
# encoding;utf-8
# timezone;-2
# color;black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila
# klucze a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości


# for e in  [linia.strip().split('=') for linia in open('ustawienia.conf',encoding='utf-8')]:
#     print(e)
#
# sl=dict()
# for e in  [linia.strip().split('=') for linia in open('ustawienia.conf',encoding='utf-8')]:
#     sl[e[0]]=e[1]

#
# sl=dict()
# for e in  [linia.strip().split('=') for linia in open('ustawienia.conf',encoding='utf-8')]:
#     sl[ e[0] ]=e[1]
# #    sl[klucz]=wartosc
# print(sl)
#
# for k in sl:
#     print(k,sl[k])

# print(sl['encoding'])


#31.Wczytaj do słownika dane z pliku dane.csv tak by kluczem było imię sklejone
# z nazwiskiem rozdzielone spacja (powiekszone do duzych liter),
# a wartością cały wiersz jako krotka lub lista.
# Przeiteruj po slowniku i wyswietl jego zawartość.

#print(sl['ANDRZEJ KLUSIEWICZ'])

# def get_data():
#     return [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
#
# for d in get_data():
#     print(d)
#
# sl=dict()
# data=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for d in data:
#     key=d[1].upper()+" "+d[2].upper()
#     sl[key]=d
#
# for k in sl:
#     print(k,sl[k])

#
# sl=dict()
# for d in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]: sl[d[1].upper()+" "+d[2].upper()]=d
# for k in sl: print(k,sl[k])
#
# result=[ [e,pow(2,e)] for e in range(1,11)]
# print(result)
#
# for r in result:
#     print(r)
# print('----------------')
# print(result[3])
# poz=result[3]
# print(poz[1])
# print(result[3][1])

#pandas, scikitlearn

#import matplotlib.pyplot

#32. Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
# [  (slowo,ilosc_wystapien),(slowo,ilosc_wystapien)   ]. Nazwa pliku ma zostać przekazana przez zmienną.
#    Wynik powinien byc posortowany malejąco wg ilosci wystapien
#    a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do osobnej listy.
#       Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników etc.
#    MAMY LISTĘ SŁÓW Z POWTÓRZENIAMI BEZ ZNAKÓW SPECJALNYCH I O JEDNOLITEJ WIELKOSCI LITER
#    b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
#       w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
#       dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1 dla tego klucza
#    c) Przepakuj dane ze słownika do listy i posortuj.
#

#A
#odebranie od użytkownika nazwy pliku do otwarcia
#wciągnięcie całej zawartości pliku do zmiennej tekstowej
#pomniejszenie/powiększenie calosci tekstu z pliku
#definicja listy z niechcianymi znakami
#dla każdego z niechcianych znaków podmiana tego znaku w tekscie z pliku na pusty ciag
#za pomocą funkcji split() - otrzymujemy listę słów
#B
#definicja słownika
#przejście pętlą po liście słów
#sprawdzenie czy dane słowo występuje jako klucz w słowniku
#jeśli występuje to zwiększamy wartość dla tego klucza o 1
#jeśli nie występuje to ustanawiamy nowy klucz taki jak to słowo z wartością 1
#Iteracja w pętli po zawartości słownika
#wypisanie pary klucz-wartość
#C
#Stworzenie pustej listy -czyli naszej docelowej listy krotek
#Iteracja w pętli po wszystkich kluczach słownika
#Dla każdego klucza dodanie do listy docelowej krotki która będzie zawierała klucz (czyli słowo) i wartość dla tego klucza (ilość wystąpień)
#Sortowanie malejące naszej listy docelowej wg. liczby wystąpień (druga kolumna krotki)
#Iteracja po liście docelowej i wyświetlanie jej elementów
# sl=dict()
# sl['key1']='value 1'
# if 'key2' in sl:
#     print('jest')
# else:
#     print('nie ma')

# import time
# start=time.time()
# file_name='tadzio.txt'#input('podaj nazwę pliku do analizy:\n')
# all=open(file_name,encoding="utf-8").read().lower()
# not_wanted=['»', '«', ':', '/', '-', '—', '.', ';', '(', '…', '!', ')', ',', '?', '*']
# for nw in not_wanted:
#     all=all.replace(nw,'')
# words=all.split()
# dt=dict()
# for w in words:
#     if w in dt:
#         dt[w]+=1
#     else:
#         dt[w]=1
# result=[]
# for k in dt:
#     result.append( (k,dt[k])  )
# result.sort(key=lambda x:x[1],reverse=True)
# for e in result:
#     print(e)
# end=time.time()
# print(f"Czas trwania={end-start}s")

#lista.sort(key=itemgetter(1), reverse=True)

#print(len(words),pow(len(words),2))
#Wiosna
#wiosna

# import re
# tekst="siała !!!???...,,,"
# print(list(set(re.findall("\W",tekst))))

# import re
# print(list(set( re.findall("\W",open('tadzio.txt',encoding='utf-8').read())  )))
#https://blog.jsystems.pl/show_post/Wyra%C5%BCenia_regularne/
#Tadeusz 354
#Litwa 255
#Helena 155

#Tadeusz
#Tadeusz.
#Tadeusz,
#Tadeusz!

# string="baba baba baba"
# print(string.count('baba'))

#przerwa do 11:38

#33.Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.

# for x in range(-10,11):
#     print(x,1/x)

#
# try:
#     print(1/0)
#     print('coś dalej')
# except:
#     print('muka!')
# print('koniec....')


# try:
#     open('nieistnieje.txt')
#     print(1/0)
#     print('coś dalej')
# except FileNotFoundError:
#     print('nie ma takiego pliku')
# except ZeroDivisionError:
#     print('dzielenie przez zero')
# except Exception as e:
#     print(f'muka! exception={e} type(exception)={type(e)}')
# print('koniec....')

#
# try:
#     open('nieistnieje.txt')
#     print(1/0)
#     print('coś dalej')
# except:
#     pass #fuuuuuu
# print('koniec....')
#
# for ....:
#     try:
#         ....
#     except:
#         ....

#34. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10
# w taki sposob by w przypadku wyjatku nie przerywac dzialania petli a po prostu wyswietlic
# na konsoli informację o błędzie i przejsc do dalszego przetwarzania

#
# for x in range(-10,11):
#     try:
#         print(x,1/x)
#     except ZeroDivisionError:
#         print(f'błąd dzielenia przez zero przy x={x}')

#file=open('errors.log',encoding='utf-8',mode="w")
# file=open('errors.log',encoding='utf-8',mode="w")
# for x in range(1,11):
#     file.write(f"element numer {x}\n")
# file.close()
#
# with open('errors.log',encoding='utf-8',mode="w") as file:
#     for x in range(1,11):
#         file.write(f"element numer {x}\n")


#35. Przetwórz wszystkie wiersze z dane.csv
# wyswietlajac na konsoli dane z wiersza wzbogacone o bmi.
# Nie podmieniaj przecinków etc w tekscie.
# W przypadku pojawienia się wyjątku na obliczaniu bmi (w zasadzie rzutowaniu na float)
# dla   któregoś wiersza chcemy go zapisać (cały wiersz)
# w osobnym pliku bledy.csv wzbogacony o informację o rodzaju błędu
#4;Andrzej;1,89;90;IOERROR


# for d in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     try:
#         bmi=round(float(d[4])/pow(float(d[3]),2),2)
#         print(*d,bmi)
#     except ValueError as e :
#         with open('errors.log',encoding="utf-8",mode="w") as file:
#             file.write(";".join(d)+f"ValueError - {e}\n")
            #file.write(f"{d[0]};{d[1]};{d[2]};{d[3]};{d[4]};ValueError - {e}\n")


#DRY

#przerwa obiadowa do 13:00
#
# def komendant():
#     print('jeb z granatnika ;)')
#
# komendant()

# def dodaj(a,b):
#     print(a+b)
#
# dodaj(10,30)

# def odejmij(a,b):
#     return a-b

# def odejmij(a,b):
#     wynik=a-b
#     return wynik
#
#
# wynik=odejmij(40,10)
# print(wynik)
#
# print(odejmij(30,12))

# def odejmij(a,b):
#     wynik=a-b
#     return wynik
#     print('nie nastąpi nigdy....')
#
# wynik=odejmij(40,10)
# print(wynik)
#
# print(odejmij(30,12))

#
# def typ(x):
#     if x>0:
#         return "dodatnia"
#     elif x==0:
#         return "zero"
#     else:
#         return "ujemna"
#
#
# print(typ(1))
# print(typ(0))
# print(typ(-1))

#36. Stwórz funkcję która przyjmie wzrost i masę a zwróci zaokraglone do 2 miejsc po przecinku BMI.
# W przypadku pojawienia się wyjątku, wyświetl na konsoli jaki wystąpił problem a z funkcji zwróć -1.

# def bmi(w,m):
#     try:
#         return round(m/pow(w,2),2)
#     except ZeroDivisionError:
#         print('podałeś zerowy wzrost')
#         return -1
#
# print(bmi(1.76,72))
# print(bmi(0,72))
#
# def witacz(imie,nazwisko):
#     print(f'Witaj {imie} {nazwisko}!')
#
# witacz('Andrzej','Klusiewicz')
# witacz('Andrzej')

#
# def witacz(imie,nazwisko="nie podano"):
#     print(f'Witaj {imie} {nazwisko}!')
#
# witacz('Andrzej','Klusiewicz')
# witacz('Andrzej')
# witacz(imie='Andrzej')

#w Pythonie nie ma przeciążania
# def witacz(a):
#     pass
#
# def witacz(a,b):
#     pass
#
# witacz('xxxx')

# def witacz(nazwisko="nie podano",imie): #fuuuuu
#     print(f'Witaj {imie} {nazwisko}!')
#
# witacz('Andrzej','Klusiewicz')
# witacz('Andrzej')
#

#37. Napisz funkcję która zwróci pod postacią listy krotek zawartość pliku
#   którego nazwę przekażemy przez pierwszy argument funkcji. Plik ma być otwarty z kodowaniem
#   podanym jako drugi argument funkcji. Jeśli kodowanie nie zostanie podane ma przyjac utf-8

# data=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for d in data:
#     print(d)

# def get_data(file_name,enc="utf-8",divisor=";"):
#     return [e.strip().split(divisor) for e in open(file_name,encoding=enc)]

# data=get_data('dane.csv')
# for d in data:
#     print(d)

# data=get_data('dane.csv',divisor=';',enc='utf-8')
# for d in data:
#     print(d)

# for d in get_data('dane.csv',divisor=';',enc='utf-8'):
#     print(d)


#38. Napisz funkcję która bedzie w stanie przyjąć taką listę jaka jest zwracana
 # przez funkcję z poprzedniego ćwiczenia. Funkcja ta ma przeiterować po otrzymanej
 # liście i wyświetlić każdy element na konsoli. Odbierz dane z funkcji z ćwiczenia
 # poprzedniego i przekaz do nowo powstalej funkcji.

# def get_data(file_name,enc="utf-8",divisor=";"):
#     return [e.strip().split(divisor) for e in open(file_name,encoding=enc)]
#
# def print_data(data):
#     for d in data:
#         print(d)
#
# my_data=get_data('dane.csv')
# print_data(my_data)
#
# print_data(  get_data('dane.csv')  )

# import my_module
# my_module.lol()
# my_module.omg()
#
# import my_module as mm
# mm.lol()
# mm.omg()

# def omg():
#     print('lokalna funkcja')
#
# from my_module import omg
# omg()


# from my_module import omg,lol
# omg()
#
# from my_module import *
# omg()

# import invoice_dao as idao
# import lead_dao as ldao
# print(idao.get_all())
# print(ldao.get_all())

# from lead_dao import *
# print(get_all())

#
# import invoice_dao
# import lead_dao
# print(invoice_dao.get_all())
# print(lead_dao.get_all())

#39. Funkcje z dwóch ostatnich ćwiczeń (poniżej) przenieś do osobnego modułu.
#Następnie zaimportuj je i dane odczytane z funkcji get_data przekaz do funkcji print_data

# def get_data(file_name,enc="utf-8",divisor=";"):
#     return [e.strip().split(divisor) for e in open(file_name,encoding=enc)]
#
# def print_data(data):
#     for d in data:
#         print(d)
#
# import csv_tools as ct
# ct.print_data( ct.get_data('dane.csv') )


#przerwa do 14:26

#
# import dao.invoice_dao
# print(dao.invoice_dao.get_all())

#
# import dao.invoice_dao as idao
# print(idao.get_all())

#from dao.invoice_dao import  *
#print(get_all())
# import dao.invoice_dao
# import invoice_dao

#import this

#import dao.invoice_dao

#40.Stwórz pakiet zawierający moduł który bedzie zawierał funkcję przyjmującą wzrost i masę a zwracającą bmi.
# Zaimportuj i wywołaj tę funkcję w taki sposób by przy jej wywołaniu nie trzeba było  podawać nazwy pakietu ani modułu.

# from tools.body import get_bmi
# print(get_bmi(1.76,72))

#TKINTER
#EASYGUI

# import requests
# response=requests.get('https://jsystems.pl/static/blog/python/dane.json')
# print(response.status_code)
# if response.status_code==200:
#     print('ok')
#     data=response.json()
#     print(data)
#     print(data['nazwisko'])
#     print(data['adres'])
#     adres=data['adres']
#     print(adres['miasto'])
#     print(data['adres']['miasto'])
#     print(data['jezyki'])
#     for j in data['jezyki']:
#         print(j)

#41. z usługi sieciowej http://jsystems.pl/Universe/samaTabelka.do pobierz informację o szkoleniach.
# na konsoli wyswietl tytuly, miasta i daty wszystkich szkolen które w tytule mają malymi badz duzymi   literami "Docker"