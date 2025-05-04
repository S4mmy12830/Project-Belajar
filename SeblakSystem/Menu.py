def varian() :
    var = input("Mau varian apa, Ori atau pedas ")
    var.lower()
    if var == 'ori' :
        print("Varian Original")
    elif var == 'pedas' :
        lev = input("Mau level berapa (1-5) ")
        print(f"Varian Pedas Level ")
pesanan = []
drink = []
#Data harga toping prasmanan
sosis = 2
bakso = 2
telur = 3
sosin = 2
otk = 2
sawi = 2 
ceker = 3
tonggong = 3
basreng = 2
makaroni = 2
glosor = 2
kwetiau = 2
kerupuk = 2

#Menu minuman
jeruk = 3
kopi = 3
teh = 3
air = 2
jus = 5


def menu() :
    print(f'''
    _____________________
    |-------Menu--------|
    |sosis........... 2k|
    |bakso........... 2k|
    |telur........... 3k|
    |sosin........... 2k|
    |otk............. 2k|
    |sawi............ 3k| 
    |ceker........... 3k|
    |tonggong........ 3k|
    |basreng......... 2k|
    |makaroni........ 2k|
    |glosor.......... 2k|
    |kwetiau......... 2k|
    |kerupuk......... 2k|
    ---------------------
    
    ''')

    pesan = input("Pesan atau tidak -> ")
    pesan.lower()
    if pesan == 'pesan' :
        while True :
            krnj = input("Masukkan toping (stop) ")
            if krnj == 'sosis' :
                pesanan.append(sosis) #sosis
            elif krnj == 'bakso' :
                pesanan.append(bakso) #bakso
            elif krnj == 'telur' :
                pesanan.append(telur) #telur
            elif krnj == 'sosin' :
                pesanan.append(sosin) #sosin
            elif krnj == 'otk' :
                pesanan.append(otk) #otak2
            elif krnj == 'sawi' :
                pesanan.append(sawi) #sawi
            elif krnj == 'ceker' :
                pesanan.append(ceker) #ceker
            elif krnj == 'tonggong' :
                pesanan.append(tonggong) #tonggong
            elif krnj == 'makaroni' :
                pesanan.append(makaroni)
            elif krnj == 'glosor' :
                pesanan.append(glosor)
            elif krnj == 'kwetiau' :
                pesanan.append(kwetiau)
            elif krnj == 'basreng' :
                pesanan.append(basreng)
            elif krnj == 'kerupuk' :
                pesanan.append(kerupuk)
            elif krnj == 'stop' :
                print('\r\n', pesanan)
                total = sum(pesanan)
                print(f"\r\nTotal dari pesanan anda {total}k")
                print("Terima kasih \r\n")
                break
            else : print("Kami tidak memiliki topig yang anda mau")

            varian()
    elif pesan == 'tidak' :
        pass
    else : print("Error")

def minum() :
    print(f'''
    _____________________
    |-------Menu--------|
    |jeruk........... 3k|
    |kopi............ 3k|
    |teh............. 3k|
    |air............. 2k|
    |jus jambu....... 5k|
    ---------------------
    
    ''')

    pesan = input("Pesan atau tidak -> ")
    pesan.lower()
    if pesan == 'pesan' :
        while True :
            add = input("Masukkan minuman (stop) ")
            if add == 'jeruk' :
                drink.append(jeruk) #jeruk
            elif add == 'kopi' :
                drink.append(kopi) #kopi
            elif add == 'teh' :
                drink.append(teh) #teh
            elif add == 'air' :
                drink.append(air) #air
            elif add == 'jus jambu' :
                drink.append(jus) #jus
            elif add == 'stop' :
                print(f"\r\n{drink}\r\n")
                ttl = sum(drink)
                print(f"Total minuman anda {ttl}k")
                break
            else : print("Kami tidak memiliki yang anda mau")
    elif pesan == "tidak" :
        pass
    else : 
        print("Error")

