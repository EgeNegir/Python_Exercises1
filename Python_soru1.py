#Girilen sayının pozitif ya da negatif olduğunu ekrana yazınız
sayi=int(input("sayi giriniz:"))
if sayi < 0 :
    print("sayi negatif")
elif sayi > 0:
    print("sayı pozitif")
else:
    print("sayi ne negatif ne de pozitif")

#Vize ve Final notu girilen öğrencinin geçip geçmediğini
#hesaplayan program (vizenin %40,finalin %60’ı hesaplanır.
#Final en az 60 olmak zorundadır,vize+final 55ten büyük olmalıdır.)
vize=int(input("vize notunu giriniz"))
final=int(input("final notunu giriniz"))
vize1=(vize*40)/100
final1=(final*60)/100
toplamnot=vize1+final1
if final >=60 and toplamnot >=55 :
    print("gectiniz")
else:
    print("kaldiniz")

#Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program?   
sayi1=int(input("sayi1 giriniz :"))
sayi2=int(input("sayi2 giriniz :"))
sayi3=int(input("sayi3 giriniz :"))
a=[]
a.append(sayi1)
a.append(sayi2)
a.append(sayi3)
en_buyuk_sayi = max(a)
print("En buyuk sayi:", en_buyuk_sayi)

#Girilen sayının 6'nın katı olduğunu bulan program?
num=int(input("sayi giriniz"))
if num % 6==0:
    print("sayi 6nin kati")
else:
    print("sayi 6nin kati degil")

#Ekrana 1:Toplama, 2:Çıkarma,..yaz. Sonra kullanıcıdan iki sayı alıp işlemi seçerek sonucu ekranda yazan program?
print("1:Toplama") 
print("2:Cikarma")
print("3:Carpma")
print("4:Bolme")
secim=int(input("Yapmak istediginiz islemin numarasini secin :"))
num1=int(input("sayi1 giriniz:"))
num2=int(input("sayi2 giriniz:"))
if secim == 1:
    print(num1+num2)
elif secim==2:
    print(num1-num2)
elif secim==3:
    print(num1*num2)
elif secim==4:
    print(num1/num2)


#Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve
#çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
k=[]
t=[]
sayii=int(input("sayi giriniz :"))
for i in range(1,sayii+1):
    if i %2==0:
        k.append(i)
for z in range(1,sayii+1):
    if z %2!=0:
        t.append(z)
print("Ciftlerin toplami:", sum(k))
print("Teklerin toplami:", sum(t))

#fonskiyon
def TekCiftToplam(deger1):
    k1=[]
    t1=[]
    for i in range(1,deger1+1):
        if i %2==0:
         k1.append(i)
    for z in range(1,deger1+1):
        if z %2!=0:
            t1.append(z)
    return sum(k1) , sum(t1)
print(TekCiftToplam(9))


#Girilen sayının tam bölenlerini bulan program?
l=[]
Deger=int(input("sayi  giriniz:"))
for i in range(1,Deger+1):
    if Deger%i==0:
        l.append(i)
print(l)

#Girilen bir sayının asal çarpanlarını bulan program?
num3 = int(input("Sayı giriniz:"))
asal_mi = True  
for i in range(2, num3):
    if num3 % i == 0:
        asal_mi = False
        break  
if asal_mi and num3 > 1:  
    print("Sayiniz asal.")
else:
    print("Sayiniz asal degil.")

#girilen sayinin kac basamakli oldugunu bulan program
sayi = int(input("sayi gir:"))
basamak_sayisi = len(str(sayi))
print("girilen sayının basamak sayısı:", basamak_sayisi)

#Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program?   
sayi1=int(input("sayi1 giriniz :"))
sayi2=int(input("sayi2 giriniz :"))
sayi3=int(input("sayi3 giriniz :"))
a=[]
a.append(sayi1)
a.append(sayi2)
a.append(sayi3)
en_buyuk_sayi = max(a)
print("En buyuk sayi:", en_buyuk_sayi)

#girilen sayinin basamaklarini ekrana yazdirin
list=[]
a=int(input("sayi giriniz:"))
yüzler=a//100
onlar=(a%100)//10
birler=(a%10)
list.append(yüzler)
list.append(onlar)
list.append(birler)
print(f"yüzler basamağı {yüzler}")
print(f"onlar basamağı {onlar}")
print(f"birler basamağı {birler}")

#N’e kadar tek sayıları yazdıran program?
N = int(input("Bir N degeri giriniz:"))

for sayi in range(1, N + 1, 2):
    print(sayi)

#20'ye kadar olan sayıları, 10'dan küçük ve 10'dan büyük şeklindelisteleyecek Python kodu nasıl olmalıdır?
kucuk_liste = []
buyuk_liste = []

for sayi in range(1, 21):
    if sayi < 10:
        kucuk_liste.append(sayi)
    else: 
        buyuk_liste.append(sayi)
print("10'dan kucuk sayilar:", kucuk_liste)
print("10'dan buyuk sayilar:", buyuk_liste)


#Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve
#çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
k=[]
t=[]
sayii=int(input("sayi giriniz :"))
for i in range(1,sayii+1):
    if i %2==0:
        k.append(i)
for z in range(1,sayii+1):
    if z %2!=0:
        t.append(z)
print("Ciftlerin toplami:", sum(k))
print("Teklerin toplami:", sum(t))

#Girilen 5 sayının ortalamasını bulan program? 
liste = []

for i in range(5):
    sayi = int(input("Sayı Giriniz:"))
    liste.append(sayi)

ortalama = sum(liste) / len(liste)
print("Girilen sayıların ortalaması:", ortalama)

#iki basamakli sayinin rakamlarinin faktoriyeli
a=int(input("sayi giriniz:"))
onlar=(a%100)//10
birler=(a%10)
carpim=1
for i in range(1,onlar+1):
    carpim*=i
print(carpim)
carpma=1
for b in range(1,birler+1):
    carpma*=b
print(carpma)

#girilen cumleyi ters ceviren program
a=[]
for i in range(1):
    x=str(input("Cumleyi Girin:"))
    a.append(x)
ters=a[0][::-1]
print(f"{a[0]}ters hali:",ters)

#Serinin ilk elemanı, toplam eleman sayısını ve artış değeri girildiğinde seri sonucunu hesaplayan program? 
a=int(input("Serinin toplam eleman sayisi:"))
b=int(input("Serinin artis degeri :"))
c=int(input("Serinin ilk elemani"))
for i in range(c,c+b*a,b):
    print(i)


#Klavyeden 3 adet kenar uzunluğu giriliyor. Girilen kenar uzunlukları göz önüne 
#alındığında üçgenin çizilip çizilemeyeceğini, çizilebilir ise türünü (ikizkenar, çeşitkenar, eşkenar), 
#alanını ve çevresini hesaplayan program?

a = float(input("1. Kenar Uzunlugu: "))
b = float(input("2. Kenar Uzunlugu: "))
c = float(input("3. Kenar Uzunlugu: "))
if a + b > c and a + c > b and b + c > a:
    print("Bu kenar uzunluklariyla bir ucgen cizilebilir.")
    
   
    if a == b == c:
        print("Bu bir eskenar ucgendir.")
    elif a == b or a == c or b == c:
        print("Bu bir ikizkenar ucgendir.")
    else:
        print("Bu bir cesitkenar ucgendir.")
    
   
    s = (a + b + c) / 2
    alan = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"ucgenin alani: {alan}")
    
    cevre = a + b + c
    print(f"ucgenin cevresi: {cevre}")

else:
    print("Bu kenar uzunluklariyla bir ucgen cizilemez.")


        ##########SORULARIN FONKSIYONLA COZUMLERI#############



#Girilen sayının pozitif ya da negatif olduğunu ekrana yazınız
#fonksiyon 
def isaret(sayi):
    if sayi >0 :
        return "pozitif"
    elif sayi < 0:
        return "negatif"
    else:
        return "sayi sifirdir"
print(isaret(-7))

#Vize ve Final notu girilen öğrencinin geçip geçmediğini
#hesaplayan program (vizenin %40,finalin %60’ı hesaplanır.
#Final en az 60 olmak zorundadır,vize+final 55ten büyük olmalıdır.)
# #fonksiyon
def GectiKaldi(vize,final):
    vize1=(vize*40)/100
    final1=(final*60)/100
    toplamnot=vize1+final1
    if final >=60 and toplamnot >=55 :
        return "gectiniz"
    else:
        return "kaldiniz"
print(GectiKaldi(60,80))

#Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program?
#fonksiyon
def MaxSayiBul(sayi1, sayi2, sayi3):
    a=[]
    a.append(sayi1)
    a.append(sayi2)
    a.append(sayi3)
    en_buyuk_sayi = max(a)
    return en_buyuk_sayi  
print(MaxSayiBul(13, 24, 7))

#Girilen sayının 6'nın katı olduğunu bulan program?
#fonksiyon
def AltiKat(num):
    if num % 6==0:
     return "sayi 6nin kati"
    else:
     return"sayi 6nin kati degil"
print(AltiKat(24))

#Ekrana 1:Toplama, 2:Çıkarma,..yaz. Sonra kullanıcıdan iki sayı alıp işlemi seçerek sonucu ekranda yazan program?
#fonksiyon
print("1:Toplama") 
print("2:Cikarma")
print("3:Carpma")
print("4:Bolme")
def islemRobotu(num,num1,num2):
    if num == 1:
        return (num1+num2)
    elif secim==2:
        return (num1-num2)
    elif secim==3:
        return (num1*num2)
    elif secim==4:
        return (num1/num2)
print(islemRobotu(1,19,1))

#1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.
#fonksiyon
def UcBesBolen():
    liste1=[]
    for i in range(1,100):
        if i % 3 == 0 and i % 5==0:
            liste1.append(i)
    return liste1
sonuc=UcBesBolen()
for eleman in sonuc:
    print(eleman)

#Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve
#çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
#fonskiyon
def TekCiftToplam(deger1):
    k1=[]
    t1=[]
    for i in range(1,deger1+1):
        if i %2==0:
         k1.append(i)
    for z in range(1,deger1+1):
        if z %2!=0:
            t1.append(z)
    return sum(k1) , sum(t1)
print(TekCiftToplam(9))

#Girilen bir sayının asal olup olmadıgını bulan program?
#fonksiyon
def asal_mi(sayi):
    if sayi < 2:
        return False 
    for i in range(2, sayi):
        if sayi % i == 0:
            return False 
    return True
print(asal_mi(17))


#Code the program that finds the entered number of days, how many years and how many months.
def monthYear(day):
    month=day//30
    year=day//365
    return [month,year]
print(monthYear(366))


#palindrome  
def pal(word):
    opposite=word[::-1]
    if word==opposite:
       return 'word is palindrome'
    else:
       return 'word is not palindrome '
print(pal('ege'))

#factorial
def factorial(n):
    multiplication=1
    for i in range(1,n+1):
        multiplication*=i
    return multiplication
print(factorial(7))

#faktoriyel
def faktoriyel(m):
    carpim=1
    for i in range(1,m+1):
        carpim*=i
    return carpim
print(faktoriyel(7))


#Remove the repeated elements in a list
import random
list = [random.randint(0, 9) for _ in range(15)]
list2 = []
print(list)

for i in list:
    if i not in list2:
        list2.append(i)
list = list2.copy()
print(list)


#4) Uzunluğu çift olan ve tam sayı değerler içeren bir
#verildiğinde 0. ve 1. elemanları, 2. ve 3. elemanları, 4. ve 5.
#elemanları,… yer değiştiren fonksiyonu yazınız?
#def YerDegis(Liste):
# KOD BURAYA YAZILACAK
#return Liste
#--------------------------------------------------
#Örnek kod: print(YerDegis([0,1,2,3,4,5,6,7,8,9]))
#Çıktı: [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]
def VizeYerDegis(Liste):
    for i in range(0,len(Liste)-1,2):
        tmp = Liste[i]
        Liste[i]=Liste[i+1]
        Liste[i+1]=tmp
    return Liste

#2) Verilen iki sayı arasında 3’e tam bölünenleri bulup listeye
#atan fonksiyonu yazınız?
# KOD BURAYA YAZILACAK
#def ListeyiOlustur(baslangic,bitis):
#return Liste
#--------------------------------------------------
#Örnek kod: print(ListeyiOlustur(15,25))
#Çıktı: [15, 18, 21, 24]
def ListeyiOlustur(baslangic,bitis):
    a=[]
    for i in range(baslangic,bitis+1):
        if i%3==0:
            a.append(i)
    return a
print(ListeyiOlustur(20,60))

  

#def BozanElamanIndeksi(Liste):
#6) Artış miktarı sabit olan aritmetik bir seri liste şeklinde verildiğinde örüntüyü bozan elemanın indeksini dönderiniz?
# KOD BURAYA YAZILACAK
#return Indeks
#----------------------------------------------------------------------------------------------------
#Örnek kod: print(BozanElamanIndeksi([1,3,5,7,9,12,13]))
#Çıktı: 6
def VizeBozanElamanIndeksi(Liste):
    fark1 = []
    fark2 = []
    for i in range(1,len(Liste)):
        fark1.append(Liste[i]-Liste[i-1])
    for i in range(1,len(fark1)):
        fark2.append(fark1[i]-fark1[i-1])        
    indeks = 1
    for i in fark2:    
        if i!=0:
            break
        indeks+=1
        
    return indeks+2


#1) Verilen m, a ve b parametrelerini kullanarak, m adet
#tam sayı içeren bir liste oluşturunuz. Sayılar [a-b]
#aralığında olmalı. NOT: randint komutu kullanılmayacak.
#def ListeOlustur(m,a,b):
#…
#return Liste
#--------------------------------------------------
#Örnek kod: print(ListeOlustur(5,3,8))
#Çıktı: [4, 4, 3, 7, 8]
import random
def ListeOlustur(m,a,b):
    Liste=[]
    for i in range(m):
        sayi=random.random()
        sayi=sayi*(b-a)+a
        Liste.append(sayi)
    return Liste
print(ListeOlustur(5,3,8))

#2) Tam sayı değerleri olan m elemanlı bir listede 1. ve m.,
#2. ve m-1., 3. ve m-2. elemanları toplayarak yeni bir liste
#üretiniz. Liste boyutu tek olduğunda ortanca elemanı yeni
#listeye direk ekleyiniz.
#def Topla(Liste):
#…
#return Liste
#--------------------------------------------------
#Örnek kod: print(Topla([4,1,2,8,3,5,9,3,1]))
#Çıktı: [5,4,11,13,3]
def Topla(liste):
    y=[]
    m=len(liste)
    for i in range(m//2):
        y.append(liste[i] + liste[m-i-1])
    if m%2==1:
        y.append(liste[m//2])
    return [y]
print(Topla([2,4,6,7,84,5,2]))


#Verilen bir cümledeki türkçe karakterleri ingilizce
#karşılıklarına dönüştüren programı yazınız? Harflerin
#hepsinin küçük olduğunu düşünelim.
#def Tr2Eng(cumle):
#…
#return ncumle
#--------------------------------------------------
#Örnek kod: print(Tr2Eng(‘hayırlı günler’))
#Çıktı: ‘hayirli gunler’
def Tr2Eng(cumle):
    ncumle = ''
    List = ['ı','ö','ü','ş','ç']
    Dict = {'ı':'i','ö':'o','ü':'u','ş':'s','ç':'c'}
    for i in cumle:
        if i in List:
            ncumle = ncumle + Dict[i]
        else:
            ncumle = ncumle + i
    return ncumle
print(Tr2Eng('hayırlı günler'))


#6) Tam sayı değerleri olan m elemanlı bir listedeki sayıları basamak değerlerine dönüştüren, sonra basamak
#değerlerinin toplamını geri döndüren programı yazınız?
#def BasamakDegeri(Liste):
#…
#return toplam
#--------------------------------------------------
#Örnek kod: print(BasamakDegeri([454, 10002, 20])) → 3 + 5 + 2 ⇒ 10
def BasamakDegeri(Liste):
    def basamak(n):
        k=0
        while n>0:
            k+=1
            n = n//10
        return k

    top = 0
    for i in Liste:
        top += basamak(i)
    
    return top


##2) Üç basamaklı rakamları birbirinden farklı sayıları
#liste halinde döndüren programı yazınız?
#def UcBasamakli():
#…
#return Liste
#--------------------------------------------------
#Örnek kod: print(UcBasamakli())
#Çıktı: 102 103 104 105 106 107 108 109 120 123 . . . . .
#980 981 982 983 984 985 986
def UcBasamakli():
    Liste=[]
    for i in range(100,1000):
        birler=i%10
        onlar=((i//10)%10)
        yüzler=((i//100))
        if birler!=onlar and birler!=yüzler and onlar!=yüzler:
            Liste.append(i)
    return Liste
print(UcBasamakli())



#3) Verilen para miktarını 100, 50, 20, 10 ve 1 TL bozuk
#paralara dönüştüren programı yazınız? Büyük değerli
#bozuklar öncelikli olmalı. Çıktı liste olmalı ve bozukların
#adetlerini sırayla içermeli.
#def ParaBozdur(para):
#…
#return Liste
#--------------------------------------------------
#Örnek kod: print(ParaBozdur(2458))
#Çıktı: [24, 1, 0, 0, 8]
def ParaBozdur(para):
    Liste = [0,0,0,0,0]
    while para>0:
        if para >= 100:             
            Liste[0]+=1
            para -= 100
        elif para >= 50:             
            Liste[1]+=1
            para -= 50
        elif para >= 20:            
            Liste[2]+=1
            para -= 20
        elif para >= 10:            
            Liste[3]+=1 
            para -= 10
        else:
            Liste[4]=para
            para = 0
    return Liste
print(ParaBozdur(2132))



#4) Verilen tam sayıya kadarki değerlerin toplamını
#döndüren özyinelemeli programı yazınız?
#Topla(n)=1+2+3+…+n
#def Topla(n):
#return sonuc
#--------------------------------------------------
#Örnek kod: print(Topla(6))
#Çıktı: 21
def Topla(n):
    if n==1:
        return 1
    else: 
        return n + Topla(n-1)
print(Topla(5))

#Girilen sayının Jumbled (komşu rakamlar arasındaki fark maksimum 1) olup olmadığını bulunuz? 
def Jumbled(n):
   birler=n%10
   onlar=((n//10)%10)
   if abs(onlar-birler)<=1:
       return 'jumbled'
   else:
       return 'nonjumbled'
print(Jumbled(27))