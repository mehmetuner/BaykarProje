### İnsansız Hava Aracı Kiralama Uygulaması 

## Kod için gereksinimler
Python <br>
Django <br>
PostgreSQL <br>
Postman
### Tanım📌
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20205930.png" alt="alt text" width="500" height="500">
Postman ile kullanıcıdan username ve password isteniliyor. CustomUser tablosundaki verilerle uyuşmadığında hata veriyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210004.png" alt="alt text" width="500" height="500">
Doğru girildiğinde ise giriş başarılı oluyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210115.png" alt="alt text" width="500" height="500">
Giriş yapılmadan ihadata url sine giriş hakkı verilmiyor ve ayriyetten ihadata url sine giriş yapılabilmesi için giriş yapan kişinin admin yetkisine sahip olması gerekiyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210136.png" alt="alt text" width="500" height="500">
Bu kullanıcı giriş yapıyor fakat admin yetkisine sahip değil.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210249.png" alt="alt text" width="500" height="500">
Admin yetkisine sahip olmadığı için ihadata url sine erişemiyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210738.png" alt="alt text" width="500" height="500">
Admin yetkisine sahip ve giriş yapan admin veritabanına veriler ekliyor bazı sutünlar ise otomatik kendiliğinden default olarak ekleniyor(Currency,IsForRent ve IsDelete)
IsForRent Stock sutünü 0 dan büyükse otomatik olarak True olurken 0 ise False oluyor. IsDelete sutunu ise verilerin silindikten sonra da veritabanında de kalıp veri kaybolmasını engelleniyor.Currency de default olarak '₺' olarak geliyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210914.png" alt="alt text" width="500" height="650">
Veriler eklendikten sonra GET methodu ile gösterilimi.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210940.png" alt="alt text" width="500" height="500">
Verilerimizde silme işlemi yapmak için DELETE methodunu kullanıyoruz.Silme işlemi ile IsDelete sutunu otomatik olarak True oluyor
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20211107.png" alt="alt text" width="500" height="500">
IsDelete False olanları filtreleyecek şekilde GET methodu ile verilerin gösterimi
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20211256.png" alt="alt text" width="500" height="500">
useriha url sine hem admin hem de kullanıcı olarak erişim bulunuyor eğer login yapılmadıysa buraya da erişim hakkı verilmiyor. ve post methoduyla ekleme işlemi yapılıyor fakat IhaId foreign key ile IhaData tablosundaki Id sutunu ile eşleştiriliyor
olmayan IhaId eklenmeye çalıştığında ekleme hatası veriyor ve böylece olmayan IhaId eklenemiyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20211405.png" alt="alt text" width="500" height="500">
Doğru IhaId girildiğinde ise veritabanına ekleme işlemi başarıyla gerçekleşiyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20211504.png" alt="alt text" width="500" height="500">
UserWindowIha tablosunda bulunan tüm verileri GET methodu ile gösterilimi bu şekildedir ve PurpchaseDate sutunu,TotalFee sutunu ve Currency sutunu otomatik olarak eklenmektedir. PurpchaseDate şuanki yılı otomatik olarak alıyor. TotalFee ise kullanıcının istediği İnsansız Hava Aracının yıllık maliyeti * Kaç yıl kiralayacağı * Alacağı adet ile çarpılıp otomatik olarak TotalFee sutununa eklenmektedir. Currency de default olarak '₺' olarak geliyor.

PostgreSQL görüntüleri ise şu şekildedir

<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20213440.png" alt="alt text" width="500" height="500">
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20213509.png" alt="alt text" width="500" height="500">
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20213525.png" alt="alt text" width="500" height="500">
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20213556.png" alt="alt text" width="500" height="500">
