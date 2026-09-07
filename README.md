Nama : Ranu Ario Sulistianto

NPM : 2506657270

Kelas : PBP F   

### Tugas 1

1. Saya menggunakan elemen semantik HTML5 secara konsisten dalam merancang struktur halaman, seperti <header>, <nav>, <main>, <section>, dan <footer>. Penggunaan tag <section> membantu membagi portofolio ke dalam blok-blok informasi independen yang terstruktur (Profile, Skills, Experience, dan Education). Penerapan elemen semantik ini memudahkan screen reader memahami hirarki konten sekaligus meningkatkan keterbacaan serta pemeliharaan kode (code maintainability) jika dibandingkan hanya menggunakan <div> bersarang. Selain itu, struktur ini membantu mesin pencari mengindeks bagian-bagian penting situs secara lebih akurat, sementara penggunaan tag seperti daftar deskripsi (<dl>, <dt>, <dd>) dan tag <strong> memberikan penekanan semantik yang tepat pada informasi kunci.
2. Tantangan utama yang saya temui saat mengatur responsivitas CSS adalah mengelola tata letak Hero section yang menggunakan CSS Grid dua kolom dengan grid-template-areas, karena elemen foto dan teks yang berdampingan berisiko mengalami overflow saat ukuran layar menyempit. Untuk mengevaluasi tata letak dari desktop ke mobile, saya mengalihkan fokus utama ke keterbacaan vertikal dengan mengubah tata letak grid menjadi satu kolom (grid-template-columns: 1fr). Posisi identitas nama ditempatkan paling atas, diikuti oleh foto profil dengan pembatasan ukuran maksimal (max-width: 220px), lalu diakhiri dengan deskripsi bio serta tautan sosial. Elemen navigasi juga diatur ulang menggunakan Flexbox dengan penyesuaian jarak (gap) dan padding agar tetap nyaman diakses melalui layar sentuh tanpa memakan terlalu banyak ruang viewport.
3. Batasan utama yang saya rasakan pada static web murni adalah pengelolaan data yang kaku dan tidak efisien, karena setiap pembaruan informasi harus dilakukan secara manual di dalam kode sumber HTML, serta interaksi pengguna seperti tombol Dark Mode yang statusnya belum tersimpan di database. Untuk mengatasi batasan tersebut, fungsionalitas dinamis yang ingin saya persiapkan pada iterasi selanjutnya menggunakan framework Django adalah mengintegrasikan Model Django (MVT Architecture) agar konten portofolio dapat dikelola secara dinamis melalui halaman Admin tanpa menyentuh kode HTML. Saya juga berencana menambahkan fitur formulir kontak interaktif yang terhubung dengan basis data, serta menyimpan preferensi tema pengguna ke dalam session atau database agar pilihan tema tetap bertahan saat berpindah halaman.

AI disclosure
Dalam pengerjaan tugas ini, saya menggunakan Gemini AI sebagai asisten dan teman diskusi untuk membantu menyusun serta merapikan tampilan website.
Saya memanfaatkan AI secara bertahap sesuai kebutuhan pengerjaan, seperti menanyakan saran struktur halaman, mencari solusi saat menemukan kendala tampilan, serta mengosultasikan cara penataan layout agar tetap rapi di berbagai ukuran layar.

Bagian yang dibantu:
- Pembuatan fungsi tombol dark mode
- Membantu menemukan penyebab dan solusi ketika warna latar header terpotong serta efek glow pada menu navigasi tidak berjalan sesuai keinginan.
