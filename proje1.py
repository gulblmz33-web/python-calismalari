import os
import time

# Dosya ismi tanımlama
DATA_FILE = "personel_veritabani.txt"

def menü_göster():
    print("\n" + "="*30)
    print(" PERSONEL YÖNETİM SİSTEMİ")
    print("="*30)
    print("1. Personel Listesini Gör")
    print("2. Yeni Personel Ekle")
    print("3. Personel Ara")
    print("4. Veritabanını Temizle")
    print("q. Çıkış")
    print("="*30)

def personel_ekle():
    print("\n--- Yeni Personel Kaydı ---")
    ad = input("İsim Soyisim: ")
    departman = input("Departman: ")
    maas = input("Maaş: ")
    
    if ad and departman and maas:
        with open(DATA_FILE, "a", encoding="utf-8") as file:
            file.write(f"{ad} | {departman} | {maas} TL\n")
        print(f"\n[+] {ad} sisteme başarıyla eklendi.")
    else:
        print("\n[!] Hata: Tüm alanları doldurmalısınız!")

def listele():
    print("\n--- Kayıtlı Personel Listesi ---")
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        print("Sistemde henüz kayıtlı personel bulunamadı.")
    else:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for sira, satir in enumerate(file, 1):
                print(f"{sira}. {satir.strip()}")

def personel_ara():
    aranan = input("\nAranacak ismi giriniz: ").lower()
    bulundu = False
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for satir in file:
                if aranan in satir.lower():
                    print(f"\n[Sonuç]: {satir.strip()}")
                    bulundu = True
        if not bulundu:
            print("\n[-] Aranan isimle eşleşen bir kayıt bulunamadı.")
    else:
        print("\n[!] Veritabanı dosyası henüz oluşturulmamış.")

def temizle():
    onay = input("\n[!] Tüm veriler silinecek. Emin misiniz? (e/h): ")
    if onay.lower() == 'e':
        open(DATA_FILE, 'w').close()
        print("\n[!] Tüm kayıtlar başarıyla silindi.")

# Ana Döngü
def main():
    while True:
        menü_göster()
        secim = input("İşlem seçiniz: ")

        if secim == '1':
            listele()
        elif secim == '2':
            personel_ekle()
        elif secim == '3':
            personel_ara()
        elif secim == '4':
            temizle()
        elif secim.lower() == 'q':
            print("Sistemden çıkılıyor... İyi çalışmalar.")
            time.sleep(1)
            break
        else:
            print("\n[?] Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()



