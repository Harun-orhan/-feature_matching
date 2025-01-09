# Kedi Yüzü Tespiti

Bu proje, OpenCV kullanarak bir klasördeki resimler üzerinde kedi yüzü tespiti yapmayı amaçlamaktadır. Haar Cascade Classifier kullanarak, belirtilen resimlerdeki kedi yüzlerini tespit eder ve her bir yüzü bir dikdörtgenle işaretler. Ayrıca her yüzün üzerine "Kedi" yazısı ekler.

## Özellikler
- Klasördeki tüm `.jpg` resimlerini işler.
- Her bir resimdeki kedi yüzlerini tespit eder.
- Tespit edilen yüzleri dikdörtgenle işaretler.
- Her yüzün üzerine "Kedi" yazısını ekler.
- Kullanıcı, her bir resim üzerinde işlem tamamlandıktan sonra "q" tuşuna basarak diğer resme geçebilir.

## Başlangıç

Bu projeyi çalıştırabilmek için bilgisayarınızda Python ve gerekli kütüphanelerin kurulu olması gerekir.

### Gereksinimler
Projenin çalışabilmesi için aşağıdaki kütüphanelere ihtiyacınız vardır:

- Python 3.x
- OpenCV (`cv2`)

Bu kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

```bash
pip install opencv-python
