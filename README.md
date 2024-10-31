# Hava Aracı Üretim Uygulaması

Bu proje, hava aracı üretim sürecini yöneten bir Django REST API uygulamasıdır. Uygulama, farklı parçaların üretimi, montajı ve envanter yönetimi için gerekli işlevleri sağlar. Bu doküman, uygulamanın kurulumu, kullanımı ve geliştirme süreçlerine dair gerekli bilgileri içermektedir.

## Proje Özellikleri

- **Parçalar**: Kanat, Gövde, Kuyruk, Aviyonik.
- **Uçaklar**: TB2, TB3, AKINCI, KIZILELMA.
- **Takımlar**: Kanat Takımı, Gövde Takımı, Kuyruk Takımı, Aviyonik Takımı, Montaj Takımı.
- **Fonksiyonlar**:
  - Personel giriş ekranı.
  - Takımların kendi parçalarını üretme, listeleme ve geri dönüşüme gönderme (CRUD) işlemleri.
  - Montaj takımının uyumlu parçaları kullanarak uçak üretmesi.
  - Eksik parça durumunda uyarı verme.

## Teknolojiler

- Python
- Django & Django Rest Framework
- PostgreSQL
- Docker (Opsiyonel)

## Kurulum

### Gereksinimler

- Python 3.x
- PostgreSQL
- Pip
- Virtualenv

### Adımlar

1. **Depoyu Klonlayın**
   ```sh
   git clone https://github.com/mertalicikoglu/baykarbackend.git
   cd baykarbackend
   ```

2. **Sanal Ortam Oluşturun ve Aktif Edin**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows kullanıcıları için: venv\Scripts\activate
   ```

3. **Bağımlılıkları Yükleyin**
   ```sh
   pip install -r requirements.txt
   ```

4. **Veritabanı Ayarları**
   `settings.py` dosyasındaki `DATABASES` bölümünü PostgreSQL ayarlarınıza göre düzenleyin.

5. **Migrasyonları Uygulayın**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Süper Kullanıcı Oluşturun**
   ```sh
   python manage.py createsuperuser
   ```

7. **Sunucuyu Başlatın**
   ```sh
   python manage.py runserver
   ```

## API Kullanımı

### Kimlik Doğrulama

- Yeni bir kullanıcı kaydetmek için `/register/` endpoint'ini kullanabilirsiniz.
- Token almak için `/api-token-auth/` endpoint'ine kullanıcı adı ve şifre gönderin.

### CRUD İşlemleri

- **Takımlar**: `/teams/` - Takım oluşturma, listeleme, güncelleme, silme.
- **Personel**: `/personnel/` - Personel oluşturma, listeleme, güncelleme, silme.
- **Parçalar**: `/parts/` - Parça üretme, listeleme, güncelleme, silme.
- **Uçaklar**: `/aircraft/` - Uçak oluşturma, listeleme, güncelleme, silme.
- **Montaj**: `/aircraft/{id}/assemble/` - Uçak montajı.


## Testler

- API endpoint'lerini test etmek için `curl` veya [Postman](https://www.postman.com/) kullanabilirsiniz.
- Örnek bir personel oluşturma isteği:
  ```sh
  curl -X POST http://127.0.0.1:8000/personnel/ -H "Authorization: Token YOUR_TOKEN_HERE" -H "Content-Type: application/json" -d '{"name": "Mert Alicikoglu", "team": 1}'
  ```

## Ekstralar

- **Docker Desteği**: Proje Docker ile çalıştırılabilir hale getirildi. `docker-compose.yml` dosyasını kullanarak uygulamayı hızlıca ayağa kaldırabilirsiniz.
- **Birim Testleri**: Projede birim testleri yazılmıştır. Testleri çalıştırmak için:
  ```sh
  python manage.py test
  ```

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.

