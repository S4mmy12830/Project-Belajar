import Menu
import os

#pembukaan 
os.system('cls')
print(f"\r\n{'Seblak System'.center(30,'-')}\r\n")
print(f"Halo selamat datang di Seblak System")
org = input("Boleh tau namanya siapa ")

while True:
    print(f"Dengan {org} mau pesan apa? Ketik menu untuk melihat.")
    com = input("-> ")
    com.lower()
    if com == 'menu':
        food = input(f"Dengan {org} mau Makanan atau minuman : ")
        food.lower()
        if food == 'makanan' :
            os.system('cls') 
            Menu.menu()
            
        elif food == 'minuman' :
            os.system('cls') 
            Menu.minum()
        else : print("Kami tidak menyediakan yang anda mau")

        yn = input("\r\nSudah selesai y/n : ")
        if yn == 'y' :
            print("Terima kasih")
            break
        elif yn == 'n' :
            pass
        else : 
            print("Error")
            break
            