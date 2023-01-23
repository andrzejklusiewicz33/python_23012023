# test
# test2
# print("siema!")
# print('siema!')
#
# for x in range(10):
#     print(f'x={x}')
# print('koniec')

#formatowanie kodu ctrl+alt+L
#zakomentowywanie i odkomentowywanie ctrl+/

# print("Siema!")
# print('Siema!')
# print("Mc'Donalds")
#int x=1 #java
#x=1
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


#1. Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
#wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"


#get_all_pracownicy #fuuuuu

# first_name=input('podaj imię:\n')
# last_name=input('podaj nazwisko:\n')
# print(f"Witaj {first_name} {last_name}!")
#
# public class Main {
#     public static void main(String args[]){
#         System.out.println("WTF????");
# }
# }

#print('OMG!')

#PEP8

#import this


# x=input('podaj x:\n')
# print(x,type(x))
#print(x/10)

# x=float(  input('podaj x:\n')   ) #float,int,str
# print(x,type(x))
# print(x*1000)
# x=10
# y=3
# print( round(x/y,2) )
#
# f=float(input('podaj f:\n'))
# print(f)

#print(pow(10,4))

#2. BMI= masa/(wzrost*wzrost) . Napisz program który odbierze od użytkownika jego masę
# w kilogramach i wzrost w metrach, wyliczy i wypisze BMI.

# height=float(input('podaj wzrost w metrach:\n'))
# weight=float(input('podaj masę w kilogramach:\n'))
# bmi=round(weight/pow(height,2),2)
# print(f'bmi={bmi}')


#przerwa do 11:51

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

#3. Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to chcemy wyświetlić tę wartość
# z informacją "wartość dodatnia", jeśli zero to wyświetlamy z informacją "równe zero",
# jeśli ujemna to wyświetlamy "wartość ujemna".


# x=float(input('dej liczbę:\n'))
# if x>0:
#     print(f'{x} jest dodatnie')
# elif x==0:
#     print(f'{x} jest zerem')
# else:
#     print(f'{x} jest ujemne')



#4. Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
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


#5. Wyświetl 20 kolejnych potęg liczby 2


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

#6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
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


#przerwa obiadowa do 13:10

#7.  Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
  # - kwotę lokaty
  # - oprocentowanie w skali roku
  # - ilość miesięcy na jaką zakladamy lokatę
  # Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
  # oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
  # Kapitalizacja comiesięczna

#im=int(input('dej...'))
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


#8.Napisz program który będzie dodawał kolejne losowe wartości z zakresu
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

#9.  Napisz program który przyjmie od użyszkodnika ciąg tekstowy a następnie usunie z niego znaki ,.!? i
# wyświetli powiększony do dużych liter tekst na konsoli

