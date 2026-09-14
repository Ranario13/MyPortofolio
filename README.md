Nama : Ranu Ario Sulistianto

NPM : 2506657270

Kelas : PBP F   

### Tugas 1

1. Saya menggunakan elemen semantik HTML5 secara konsisten dalam merancang struktur halaman, seperti header, nav, main, section, dan footer. Penggunaan tag section membantu membagi portofolio ke dalam blok-blok informasi independen yang terstruktur (Profile, Skills, Experience, dan Education). Penerapan elemen semantik ini memudahkan screen reader memahami hirarki konten sekaligus meningkatkan keterbacaan serta pemeliharaan kode (code maintainability) jika dibandingkan hanya menggunakan div bersarang. Selain itu, struktur ini membantu mesin pencari mengindeks bagian-bagian penting situs secara lebih akurat, sementara penggunaan tag seperti daftar deskripsi (dl, dt, dd) dan tag strong memberikan penekanan semantik yang tepat pada informasi kunci.
2. Tantangan utama yang saya temui saat mengatur responsivitas CSS adalah mengelola tata letak Hero section yang menggunakan CSS Grid dua kolom dengan grid-template-areas, karena elemen foto dan teks yang berdampingan berisiko mengalami overflow saat ukuran layar menyempit. Untuk mengevaluasi tata letak dari desktop ke mobile, saya mengalihkan fokus utama ke keterbacaan vertikal dengan mengubah tata letak grid menjadi satu kolom (grid-template-columns: 1fr). Posisi identitas nama ditempatkan paling atas, diikuti oleh foto profil dengan pembatasan ukuran maksimal (max-width: 220px), lalu diakhiri dengan deskripsi bio serta tautan sosial. Elemen navigasi juga diatur ulang menggunakan Flexbox dengan penyesuaian jarak (gap) dan padding agar tetap nyaman diakses melalui layar sentuh tanpa memakan terlalu banyak ruang viewport.
3. Batasan utama yang saya rasakan pada static web murni adalah pengelolaan data yang kaku dan tidak efisien, karena setiap pembaruan informasi harus dilakukan secara manual di dalam kode sumber HTML, serta interaksi pengguna seperti tombol Dark Mode yang statusnya belum tersimpan di database. Untuk mengatasi batasan tersebut, fungsionalitas dinamis yang ingin saya persiapkan pada iterasi selanjutnya menggunakan framework Django adalah mengintegrasikan Model Django (MVT Architecture) agar konten portofolio dapat dikelola secara dinamis melalui halaman Admin tanpa menyentuh kode HTML. Saya juga berencana menambahkan fitur formulir kontak interaktif yang terhubung dengan basis data, serta menyimpan preferensi tema pengguna ke dalam session atau database agar pilihan tema tetap bertahan saat berpindah halaman.

AI disclosure
Dalam pengerjaan tugas ini, saya menggunakan Gemini AI sebagai asisten dan teman diskusi untuk membantu menyusun serta merapikan tampilan website.
Saya memanfaatkan AI secara bertahap sesuai kebutuhan pengerjaan, seperti menanyakan saran struktur halaman, mencari solusi saat menemukan kendala tampilan, serta mengosultasikan cara penataan layout agar tetap rapi di berbagai ukuran layar.

Bagian yang dibantu:
- Pembuatan fungsi tombol dark mode
- Membantu menemukan penyebab dan solusi ketika warna latar header terpotong serta efek glow pada menu navigasi tidak berjalan sesuai keinginan.


### Tugas 2

1. Alur mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser:
- Pengguna mengetik URL atau mengklik tautan di browser, yang mengirimkan HTTP Request ke server Django.
- Django pertama kali melihat file urls.py tingkat proyek. File ini akan meneruskan URL dengan awalan tertentu ke aplikasi yang tepat
- Permintaan diteruskan ke urls.py milik aplikasi main. File ini mencocokkan pola URL dan memanggil fungsi View yang sesuai.
- Fungsi di dalam views.py menerima permintaan. View bertugas mengambil data dari database dengan memanggil Model.
- Model (models.py) berinteraksi langsung dengan database untuk mengambil data riwayat pendidikan yang diminta, lalu mengembalikannya ke View dalam bentuk objek Python.
- View membungkus data tersebut ke dalam sebuah variabel dan mengirimkannya ke template. Template kemudian merender data dinamis tersebut menggunakan Django Template Language (DTL) ke dalam struktur HTML dasar. HTML yang sudah matang ini kemudian dikembalikan oleh View sebagai HTTP Response ke browser pengguna.

2. Jika data ditulis langsung di HTML, setiap kali kita ingin menambah pengalaman atau menghapus proyek lama, kita harus membuka, membaca, dan mengubah kode sumber secara manual. Dengan model, data dipisahkan dari struktur tampilan. Kita dapat mengedit data dengan mudah melalui antarmuka visual seperti Django Admin tanpa perlu menyentuh atau merusak kode HTML. Terlebih lagi, jika kita memiliki banyak (misal 100) data proyek, menuliskannya di HTML akan membuat file menjadi sangat panjang dan sulit dikelola. Dengan Model, template hanya perlu menulis satu blok desain HTML yang kemudian diulang secara otomatis ({% for project in projects %}) menggunakan perulangan. Model juga memungkinkan kita untuk melakukan manipulasi data tingkat lanjut, seperti mengurutkan proyek dari yang terbaru, atau melakukan pencarian dan filter data sebelum dikirim ke pengguna.

3. makemigrations, berfungsi untuk mendeteksi setiap perubahan yang kita ketik di file models.py dan mencatat perubahan tersebut ke dalam sebuah file migrasi baru. Perintah ini belum mengubah database sungguhan.Sedangkan migrate, berfungsi untuk membaca file instruksi/cetak biru yang dibuat oleh makemigrations tadi, lalu menerapkannya secara nyata ke dalam skema database, misalnya membuat tabel baru atau menghapus kolom di database.
Contoh: Ketika kita sebelumnya mengubah tipe data Primary Key dari Integer menjadi UUIDField, kita harus menjalankan makemigrations agar Django membuat file instruksi tentang pergantian tipe ID tersebut, lalu menjalankan migrate agar tabel di dalam database SQLite kita benar-benar diperbarui menggunakan struktur yang baru.

AI disclosure
Dalam pengerjaan tugas ini, saya menggunakan Gemini AI sebagai asisten dan teman diskusi untuk membantu memahami arsitektur Django serta merapikan struktur kode dan tampilan website.
Saya memanfaatkan AI secara bertahap sesuai kebutuhan pengerjaan, seperti meminta penjelasan konsep dasar Model-View-Template (MVT), mencari solusi saat menemukan bug pada tampilan antar halaman, serta mengonsultasikan cara penulisan unit test yang efisien.

Bagian yang dibantu:
- Pembuatan kerangka awal untuk model database (Education dan Skill)
- Membantu menemukan penyebab dan solusi perbaikan ketika fitur dark mode tidak berfungsi sebagaimana mestinya
- Membantu menemukan penyebab dan solusi perbaikan menu navigation pada mobile view