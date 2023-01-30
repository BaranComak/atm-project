AliHesap = {
    'ad': 'Ali Sayan',
    'hesapno': '121232132',
    'bakiye': 3000,
    'ekhesap': 2000
}

AhmetHesap = {
    "ad": "Ahmet Deli",
    "hesapNo": "121232132",
    "bakiye": 4000,
    "ekHesap": 3000
}


def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz.")
        bakiyesorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekhesap"]
        
        if (toplam >= miktar):
            ekhesapkullanim = input("ek hesap kullanılsın mı (e/h)")

            if ekhesapkullanim == "e":
                ekhesapkullanim = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekhesap"] -= ekhesapkullanim
                print("paranızı alabilirsiniz.")
                bakiyesorgula(hesap)

            else:
                 print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")

        else:
            print("üzgünüz bakiye yetersiz.")         
            bakiyesorgula(hesap)

def bakiyesorgula(hesap):
    print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz de ise {hesap['ekhesap']} TL bulunmaktadır.")

paraCek(AliHesap,3000)

print("*******************")

paraCek(AliHesap,2000)