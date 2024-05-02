import random
import time
from liby import shoutdown


#player
name = "budi"
money = 100
poin = 0

#Bot 1
name1 = "Hali"
money1 = 100
poin1 = 0




def game():
    # mengimpor dari luar func
    global name,money,poin,name1,money1,poin1
        #Proyeksi 
    kartu = "|_|"*3
    kartu_true = random.randint(1,2)
    kartu_joker = "|$|"
    kartu_copy = kartu

    #batas jawab
    batas = 3
    taruhan_max = 100
    
    while money >= 0 and money1 >= 0 :


        #menampilkan
        print("KITA AKAN BERMAIN TEBAK TEBAKAN")

        #masukan jumlah taruhan
        while True:
            try:
                taruhan_input = int(input("Berani taruhan berapa: "))
                if taruhan_input <= taruhan_max:
                    break
                else:
                    print("Chip tidak cukup")
            except ValueError :
                print("Masukan inputan berupa angka")
        print(f"giliran pemain {name}")
        shoutdown()

        print("\nDI BAWAH INI ADA KARTU JOKER ")
        print(F"{kartu_copy}\nYG MANA KARTU JOKER \n1.KIRI\n2.TENGAH\n3.KANAN")



        #giliaran player memilih
        while True:
            try:
                pilihan_player = int(input("Pilih yang mana: "))
                if pilihan_player<= batas:
                    break
                else:
                    print("Pilihannya harus 1-3 doang")
            except ValueError:
                print("Inputan harus berupa angka")

        print(f"Player {name} Sudah memilih")
        shoutdown()



        #validasi kemenangan player
        if pilihan_player == kartu_true:
            print(f"Kamu menang {name}")
            money += taruhan_input
            money1 -= taruhan_input
            poin += 10
        else :
            print(f"{name} Kalah")
            money -= taruhan_input
            money1 += taruhan_input

        #giliran bot memilih
        print(f"Giliran {name1}")
        shoutdown()

        while True:
            try:
                pilihan_bot = random.randint(1,6)*random.randint(1,6)
                time.sleep(0.5)
                if pilihan_bot == batas:
                    break
                else:
                    print(f"Giliran {name1}")
            except ValueError:
                print("Error")


        

        print(f"Bot {name1} Sudah memilih")
        shoutdown()


        #validasi bot
        if pilihan_bot == kartu_true:
            print(f"Kamu menang {name1}")
            money -= taruhan_input
            money1 += taruhan_input
            poin1 += 10
        else:
            print(f"{name1} Kalah")
            money += taruhan_input
            money1 -= taruhan_input


        hasil = f"\n\nnama = {name}\nsisa saldo = {money}\nPoin kemenagan {poin}\n\nnama = {name1}\nsisa saldo = {money1}\nPoin kemenangan {poin1}\n"
        print(hasil)

        if money <= 0 or money1 <= 0 :
            print("Game Over")
            hasil = f"\n\nnama = {name}\nsisa saldo = {money}\nPoin kemenagan {poin}\n\nnama = {name1}\nsisa saldo = {money1}\nPoin kemenangan {poin1}\n"
            print(hasil)
            money += 100
            money1 +=100


def main ():
        global poin,poin1,money,money1
        print("apakah kamu ingin bermain [y/n]: ")

        while True :
            try:
                bermain = str(input(": "))
                break
            except ValueError:
                print("Masukan berupa huruf")
        if bermain == "y":
            print("Selamat bermain")
            print("Game akan dimulai dalam waktu")
            shoutdown()
            game()
        elif bermain == "n":
            print("Sampai jumpa")
            shoutdown()
            exit()

if __name__ == "__main__":
    main()