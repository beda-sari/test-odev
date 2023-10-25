sayi = int(input("sayi giriniz:"))
ters = str(sayi)[::-1]
ters = int(ters)
print("sayinin tersi:",ters)
if ters == sayi:
    print(sayi, "sayisi palindromdur.")
else:
     print(sayi, "sayisi palindrom degildir.")

