import pdb

#args kullanımı
def args_kullanımı(x_args, *args):
    print("Normal argüman kullanımı:", x_args)
    for arg in args:
        print("*args kullanımı:", arg)

args_kullanımı("elma", "armut","muz","domates","tarçın")

#kwargs kullanımı
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="yasoob")


#debugging kullanımı
def make_bread():
    pdb.set_trace()
    return "Vaktim yok"

print(make_bread())

numbers = [1,2,3,4,5,6,7]
def total_number(numbers):
    total = 0
    for num in numbers:
        total+= num

    return total
pdb.set_trace()


total = total_number(numbers)
print(total)
"""
PDB komut isteminden aşağıdaki komutları kullanarak debugging yapabilirsiniz:

l (list): Mevcut satırın kodunu listeler.
n (next): Bir sonraki satıra gider.
p (print): Bir değişkenin değerini yazdırır.
break (breakpoint): Bir satırda hata ayıklama noktası ayarlar.
c (continue): Hata ayıklamadan çıkar ve kodun çalışmasını sürdürür.
Diğer araçlar
"""
###GENERATORS####
sayilar = [1,2,3]

#sayilar değişkenini iterator hale getirmek için alttaki iki yöntemi kullanabiliriz
i_sayilar = sayilar.__iter__()
i_sayilar = iter(sayilar)

#dir kullanılabilecek metodları göstermektedir, __ ile maşlayan metodlara magic metod deniyor
print(dir(i_sayilar))

#next metodu iteratordaki elemanları tek tek ilerletir
print(i_sayilar.__next__())
print(next(i_sayilar))

while True:
    try:
        sayi = next(i_sayilar)
        print(sayi)
    except StopIteration:
        break


#stringler iterable ama iterator değil iter'e dönüştürürsek eğer sorun çıkmaz 52-53. satır
degisken = 'asdfsadsdf'
i_degisken = iter(degisken)
next(i_degisken)
#integer olmuyor anladığım kadarıyla
sa = 1333
i_sa =iter(sa)


#MAP, FİLTER, REDUCE

#map
liste = [1,2,3,4,5,6,7,8]
yeni_liste = list(map(lambda x:x**2,liste))

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

#filter

l = list(range(-5, 5))
print(l)
sifirdanbuyuk_l = list(filter(lambda x: x > 0, l))
print(sifirdanbuyuk_l)

#reduce
from functools import reduce
l = [1, 2, 3, 4, 5, 6]
sonuc = reduce((lambda x, y: x * y), l)
print(sonuc)

######SET######

#set yani kümeleme tekrar eden verilere izin vermez,  big datada büyük verilerde işe yarayabilir.
#kümeler ile kesişimler farklar çıkarılabilir(intersection,difference)

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))


#TERNARY
x,y = 5,10
#genel kullanım
if x<y:
    print('x y den küçük')
else:
    print('x y den büyüktür')

#<doğru olma durumu> if <koşul> else <yanlış olma durumu>

print('x y den küçük') if x<y else  print('x y den büyüktür')

#DECARATORS
#genel olarak fonksiyon içinde fonksiyon yapısını anlatıyor örnek olarak şu verilmiş:
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
#metin döndünen fonks
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#ilk fonksa argüman olarak fonksiyon vermiş ve atamış anlamadığım return etmeden fonksiyonları nasıl kullandığı
a_function_requiring_decoration()

#fonksiyonumuzun başına @ koyarakta ilgili fonksiyona argüman olarak verebiliyoruz eğer öyle bir argüman alıyor ise
#wraps tanımı gpt'de var galiba fonksiyonun metadata özelliklerini korumak için kullanılıyor decarator kullandığımızda kaybolabiliyormuş

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """A simple function that greets the given name."""
    print(f"Hello, {name}!")
say_hello('kadir')

# Decorated function still maintains its original metadata
#eğer wraps kullanmazsak bunlar çalışmazdı
print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)   # Output: A simple function that greets the given name.

#GLOBAL & RETURN
#global bir değişken döndürmek istediğimizde kullanırız bir fonksiyonda birden çok global değişken döndürebiliriz

#MUTATİON
#Listelerin type'ının değişkenliğiyle alakalı bir konu

#SLOTS METODU
