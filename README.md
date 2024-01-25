### İnsansız Hava Aracı Kiralama Uygulaması 
## Mehmet Üner
## Kod için gereksinimler
Python <br>
Django <br>
PostgreSQL <br>
Postman
### Tanım📌
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20205930.png" alt="alt text" width="500" height="500">
Postman üzerinden kullanıcıdan kullanıcı adı ve şifre isteniyor. Girilen bilgiler CustomUser tablosundaki verilerle eşleşmediğinde hata mesajı döndürülüyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210004.png" alt="alt text" width="500" height="650">
Girilen bilgiler CustomUser tablosundaki verilerle eşleştiğinde giriş başarılı oluyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210115.png" alt="alt text" width="500" height="650">
Giriş yapılmadan ihadata URL'sine erişim hakkı verilmiyor ve ayrıca ihadata URL'sine erişim için giriş yapan kişinin admin yetkisine sahip olması gerekiyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210136.png" alt="alt text" width="500" height="650">
Bu kullanıcı giriş yapıyor fakat admin yetkisine sahip değil.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210249.png" alt="alt text" width="500" height="650">
Admin yetkisine sahip olmadığı için ihadata url sine erişemiyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210738.png" alt="alt text" width="500" height="650">
Admin yetkisine sahip olan bir kullanıcı veritabanına veriler ekliyor. Bazı sütunlar otomatik olarak default değerlerle dolduruluyor:
Currency sütunu default olarak '₺' olarak atanıyor.
IsForRent sütunu, Stock sütunu 0'dan büyükse otomatik olarak True olarak atanıyor, aksi halde False oluyor.
IsDelete sütunu, veriler silindikten sonra dahi veritabanında kalıp veri kaybolmasını engelliyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210914.png" alt="alt text" width="500" height="650">
Veriler eklendikten sonra GET methodu ile gösterilimi.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20210940.png" alt="alt text" width="500" height="650">
Verilerimizi silmek için DELETE yöntemini kullanıyoruz. Silme işlemi gerçekleştirildiğinde, IsDelete sütunu otomatik olarak True değerini alıyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20211107.png" alt="alt text" width="500" height="650">
IsDelete False olanları filtreleyecek şekilde GET methodu ile verilerin gösterimi
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20211256.png" alt="alt text" width="500" height="650">
"useriha" URL'sine hem admin hem de kullanıcı olarak erişim sağlanabiliyor, ancak giriş yapılmadığı sürece buraya erişim izni verilmiyor. Verilerin eklenmesi için POST yöntemi kullanılıyor ve ekleme işlemi sırasında "IhaId" foreign key olarak "IhaData" tablosundaki "Id" sütunuyla eşleştiriliyor. Eğer mevcut olmayan bir "IhaId" eklenmeye çalışılırsa, ekleme hatası alınıyor ve böylece olmayan "IhaId" eklenemiyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20211405.png" alt="alt text" width="500" height="650">
Doğru IhaId girildiğinde ise veritabanına ekleme işlemi başarıyla gerçekleşiyor.
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20211504.png" alt="alt text" width="500" height="650">
UserWindowIha tablosunda bulunan tüm verileri GET methodu ile gösterilir. PurpchaseDate, TotalFee ve Currency sütunları otomatik olarak eklenir.
PurpchaseDate şu anki yılı otomatik olarak alır.
TotalFee, kullanıcının istediği İnsansız Hava Aracının yıllık maliyeti, kiralama süresi ve alınacak adet ile çarpılarak otomatik olarak TotalFee sütununa eklenir.
Currency sütunu default olarak '₺' olarak atanır.
Kullanıcı satın alma işlemi yaptıktan sonra aldığı adet stock sutünundan düşürülür.

PostgreSQL görüntüleri ise şu şekildedir

<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20213440.png" alt="alt text" width="500" height="600">
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20213509.png" alt="alt text" width="500" height="600">
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20213525.png" alt="alt text" width="500" height="600">
<img src="https://github.com/mehmetuner/BaykarProje/blob/main/fotograflar/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-01-25%20213556.png" alt="alt text" width="500" height="600">
