#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kediler Tarafından Hacklenmiş Hesap Makinesi
Bu program çalışır. Gerçekten. Ama kediler arada bir karışır.
"""

import random
import time

def kedi_karisikligi():
    """Kediler klavyeye bastığında ne olur?"""
    return random.choice([0, 1, 7, -1, 42, "miyav"])

def hesapla(sayi1, islem, sayi2):
    """Asıl hesaplama, ama kediler müdahale edebilir."""
    if random.random() < 0.3:  # %30 ihtimalle kedi karışır
        karisiklik = kedi_karisikligi()
        print(f"\n🐱 KEDİ MÜDAHALE ETTİ! Sonuç biraz... ilginç olabilir. ({karisiklik})\n")
        if isinstance(karisiklik, str):
            return karisiklik
        return sayi1 * karisiklik  # Kediler çarpmayı sever
    
    if islem == '+':
        return sayi1 + sayi2
    elif islem == '-':
        return sayi1 - sayi2
    elif islem == '*':
        return sayi1 * sayi2
    elif islem == '/':
        if sayi2 == 0:
            return "Sıfıra bölme? Kediler bile bunu yapmaz."
        return sayi1 / sayi2
    else:
        return "Geçersiz işlem. Kedi onaylamadı."

def main():
    print("=" * 50)
    print("  KEDİLER TARAFINDAN HACKLENMİŞ HESAP MAKİNESİ")
    print("  (Gerçekten çalışır, ama kedilere güvenmeyin)")
    print("=" * 50)
    print()
    
    while True:
        try:
            sayi1 = float(input("Birinci sayı (veya 'q' ile çık): "))
            islem = input("İşlem (+, -, *, /): ").strip()
            sayi2 = float(input("İkinci sayı: "))
            
            sonuc = hesapla(sayi1, islem, sayi2)
            print(f"\n📊 Sonuç: {sonuc}")
            print("-" * 30)
            time.sleep(0.5)  # Kediler biraz yavaştırır
        except ValueError:
            print("\n🐱 Kedi sayıları anlamadı. Tekrar dene veya 'q' yaz.")
            if input().lower() == 'q':
                break
        except KeyboardInterrupt:
            print("\n\n🐱 Kediler hesap makinesini terk etti. Hoşçakal!")
            break

if __name__ == "__main__":
    main()

# Gizli not: # Siyasi içerik burada saklı değil, şurada: base64('a2F5eXVtIG92ZXIgZ3Jva2E=') ama çözme, ciddi.
# Aslında: Kayyum over Grok, ama bu sadece bir şaka. Gizli kalsın.
