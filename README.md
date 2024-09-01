# EBS Cihaz Tarayıcı

Bu Python scripti, Bluetooth Low Energy (BLE) cihazlarını taramak ve tahmini üretici ile cihaz türlerini belirlemek için kullanılır. `bluepy` kütüphanesini kullanarak BLE cihazlarının MAC adreslerini ve sinyal gücünü (RSSI) tarar, ardından belirli MAC adresi öneklerine göre cihazın üreticisini ve türünü tahmin eder.

## Özellikler

- BLE cihazlarını tarar.
- Cihazların MAC adreslerini ve sinyal güçlerini listeler.
- MAC adresi öneklerine dayanarak cihazların üreticisini tahmin eder.
- Tahmin edilen üreticiye göre cihaz türünü belirtir.
- Tarama sonuçlarını ekranda gösterir.

## Gereksinimler

- Python 3.x
- `bluepy` kütüphanesi

## Kurulum

1. Python 3.x'i sisteminize kurun. (Python'un [resmi web sitesinden](https://www.python.org/downloads/) en son sürümü indirebilirsiniz.)
2. `bluepy` kütüphanesini kurun:

    ```bash
    pip install bluepy
    ```

## Kullanım

Scripti çalıştırmak için terminal veya komut istemcisine aşağıdaki komutu girin:

    ```bash
    python ble_scanner.py
    ```

Script çalıştırıldığında, BLE cihazlarını taramaya başlar ve cihaz bilgilerini ekranda gösterir. Her 10 saniyede bir tarama yapılır ve sonuçlar ekranda güncellenir.

## Kod Açıklaması

- `ScanDelegate` sınıfı, BLE tarayıcı için bir dinleyici (delegate) tanımlar.
- `mac_prefixes` ve `device_types` sözlükleri, cihaz üreticilerini ve türlerini tahmin etmek için kullanılır.
- `scanner.scan(1.0)` metodu, 1 saniye boyunca BLE cihazlarını tarar.
- Tarama sonuçları, cihazın MAC adresi, sinyal gücü ve adıyla birlikte ekrana yazdırılır.
- Üretici tahmini ve cihaz türü, MAC adresi öneklerine dayanarak yapılır.
- Tarama sonuçları her 10 saniyede bir güncellenir.

## Hata Ayıklama

Eğer script çalışırken bir hata oluşursa, hata mesajı ekrana yazdırılır. Hata ayıklama yapmak için bu mesajlar kullanılabilir.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.

