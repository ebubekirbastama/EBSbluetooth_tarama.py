from bluepy.btle import Scanner, DefaultDelegate
import time

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

scanner = Scanner().withDelegate(ScanDelegate())

mac_prefixes = {
    "Apple": ["4C:6E", "AC:23", "AC:22"],
    "Samsung": ["D8:DD", "D8:DE", "D8:DF"],
    "Google": ["A4:C1:38"],
    "Dell": ["00:14:22"],
    "HP": ["00:1E:8C"],
    "Lenovo": ["00:0C:29"],
    "Huawei": ["F0:9F:00", "F0:9F:01", "F0:9F:02"]
}

device_types = {
    "Apple": "Telefon/iPad",
    "Samsung": "Telefon/Tablet",
    "Google": "Telefon",
    "Dell": "Laptop",
    "HP": "Laptop",
    "Lenovo": "Laptop",
    "Huawei": "Telefon/Laptop"
}

while True:
    print("Tarama başlıyor...")
    try:
        devices = scanner.scan(10.0)  # 10 saniye tarama yap
        
        if devices:
            for dev in devices:
                mac = dev.addr
                cihaz_adi = dev.getValueText(9) if dev.getValueText(9) else "Yok"
                
                print(f"MAC Adresi: {mac:<20} Sinyal Gücü (RSSI): {dev.rssi:<5} dBm  Cihaz Adı: {cihaz_adi}")
                
                # Üreticiyi tahmin etme
                uretici = next((uretici for uretici, prefixes in mac_prefixes.items() if any(mac.upper().startswith(prefix) for prefix in prefixes)), "Bilinmeyen")
                
                # Cihaz türünü tahmin etme
                tahmini_tur = device_types.get(uretici, "Bilinmeyen")
                
                # Telefon veya PC olup olmadığını tahmin etme
                if any(keyword in cihaz_adi.lower() for keyword in ["phone", "mobile", "tablet", "iphone", "pixel"]):
                    tahmini_tur = "Telefon"
                elif any(keyword in cihaz_adi.lower() for keyword in ["laptop", "desktop", "pc", "dell", "hp", "lenovo"]):
                    tahmini_tur = "PC"
                
                print(f"  Tahmini Üretici: {uretici}")
                print(f"  Tahmini Cihaz Türü: {tahmini_tur}")
                
                for (adstype, desc, value) in dev.getScanData():
                    print(f"  {desc:<20}: {value}")
                
                print("---")
        else:
            print("Bluetooth Low Energy cihazı bulunamadı.")
    
    except Exception as e:
        print(f"Hata oluştu: {e}")
    
    time.sleep(10)
