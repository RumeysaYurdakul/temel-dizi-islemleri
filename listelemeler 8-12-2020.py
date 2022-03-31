#temel dizi işlemleri
#8.12.2020
import random
#boş dizi tanımlaması
d1=[]
d2=[]
d3=[]
d4=[]
#dizinin içinin doldurulması
#1.yöntem:kullanıcıya sorarak
s=''
while s!='*':
     s=input("bir bilgiyi(bitirmek için *girin):")
     if s!'*':
          d1.append(s)
print("girilen bilhiler(d1)")
print(d1)

#2. yöntem:rastgele sayılar ile
for i in range(10):
     r=random.randint(0,100)
     d2.append(r)

print("rastgele sayı dizisi(d2)")
print(d2)


#3. yöntem:seri oluşturma
#örnek:sayıların kareleri
for i in range(10):
     d3.append(i*i)
print("sayıların karleri(d3)")
print(d3)
#4.yöntem:örnek:f(x)=x^2+3x-5 x:1-->10
for x in range(10):
     d4.append(x*x+3*x-5)
print("f(x)-x^2+3x-5 (d4)")
print(d4)

#bundan sonraki işlemler
#d2 rastgele sayı dizisi üzerinde
#gerçeklenecektir.


#listedeki sayıların toplamı
toplam=0
for i in range (len(d2)):
     toplam=toplam+
