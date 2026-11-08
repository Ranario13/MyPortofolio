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


# Tugas 3

1. Alasan penggunaan ModelForm:
- ModelForm membuat komponen form secara otomatis berdasarkan skema pada model Django, sehingga tidak perlu menulis elemen input satu per satu secara manual di HTML.
- Menyediakan validasi data terintegrasi sesuai dengan aturan tipe data, panjang karakter, dan kriteria wajib diisi yang terdaftar pada model.
- Perubahan struktur pada skema model Django akan langsung terintegrasi ke form tanpa harus mengubah skema tag HTML secara manual.

Alasan diwajibkan menambahkan {% csrf_token %}:
- Melindungi aplikasi dari serangan Cross-Site Request Forgery, yaitu kondisi di mana situs asing mengeksekusi perintah jahat atas nama pengguna yang sedang terautentikasi.
- Django membuat kode rahasia unik untuk setiap sesi pengguna. Saat form dikirim via metode POST, Django memverifikasi token dari form tersebut untuk memastikan permintaan benar-benar berasal dari antarmuka aplikasi resmi.

2. JSON memiliki sintaksis yang efisien tanpa menggunakan tag penutup berulang seperti pada XML, sehingga ukuran transfer data lebih kecil dan menghemat penggunaan bandwidth. JSON secara alami memetakan langsung ke struktur objek dan array pada JavaScript, sehingga browser dapat melakukan parsing data jauh lebih cepat tanpa memerlukan mekanisme DOM Parser yang kompleks. Format pasangan key-value pada JSON jauh lebih bersih dan mudah dibaca oleh pengembang dibanding struktur pohon XML yang berbunga-bunga.

3. Alur Pengembalian Data JSON:
- Klien mengirimkan permintaan HTTP GET ke endpoint URL yang terdaftar di urls.py.
- Fungsi view mengambil data dari basis data menggunakan Django ORM dalam bentuk objek QuerySet.
- Fungsi view memuat QuerySet tersebut ke modul serialisasi (misalnya serializers.serialize('json', queryset)) untuk dikonversi menjadi string JSON.
- String JSON dikembalikan ke klien membungkus HttpResponse dengan header content_type='application/json'.
- Klien/browser menerima respon string JSON, melakukan deserialization (parsing menjadi objek JavaScript), dan menampilkannya pada halaman web.
Objek QuerySet pada Django merupakan objek kompleks Python yang tersimpan di dalam memori server. Protokol HTTP hanya dapat mentransfer aliran data berbasis teks atau biner. Serialization bertugas menerjemahkan objek Python yang kompleks tersebut menjadi format string terstruktur (seperti JSON) agar dapat dikirimkan melalui jaringan dan dipahami oleh bahasa pemrograman lain di sisi klien.
    
AI disclosure
Dalam pengerjaan tugas ini, saya menggunakan Gemini AI sebagai asisten diskusi dan pengerjaan untuk membantu memahami refactoring template, pembuatan form, serta pengelolaan data JSON pada Django.

Bagian yang dibantu:
- Pembuatan ModelForm dan fungsi views untuk operasi CRUD (Create, Read, Update, Delete).
- Implementasi fitur JSON Data Delivery dan proses deserialization.
- Penerapan sistem proteksi password mode edit.


# Tugas 4

AI disclosure
Dalam pengerjaan tugas ini, saya menggunakan Gemini AI sebagai asisten diskusi dan pengerjaan untuk membantu memahami penerapan sistem autentikasi, otorisasi berbasis peran (RBAC), serta interaktivitas halaman pada Django. 

Bagian yang dibantu:
- Penerapan pembatasan hak akses berbasis peran (Pengunjung, User Biasa, Editor, Superuser) di sisi server dan template.
- Pembuatan helper function is_editor_or_superuser untuk pengelolaan grup dan permission.
- Implementasi fitur toggle star secara asynchronous (tanpa reload halaman) menggunakan JavaScript Fetch API / AJAX. 


# Tugas 5

1. Debouncing adalah teknik pemrograman yang digunakan untuk menunda eksekusi suatu fungsi hingga durasi waktu tertentu berlalu sejak terakhir kali sebuah event dipicu. Tanpa debouncing, setiap kali pengguna mengetik satu karakter pada kolom pencarian, event listener akan langsung merespons dan mengirimkan HTTP request baru ke server. Hal ini menyebabkan beban berlebih pada server (server overload), pemborosan lalu lintas jaringan, serta potensi race condition pada tampilan hasil pencarian. Dengan menerapkan debouncing, permintaan AJAX hanya akan dikirimkan satu kali setelah pengguna benar-benar berhenti mengetik dalam jeda waktu tertentu (misalnya 300 milidetik).

2. Fungsi await ketika menggunakan fetch() adalah untuk menghentikan sementara eksekusi kode di dalam fungsi async hingga proses asinkron mengambil data dari jaringan selesai (Promise resolved) dan mengembalikan objek Response. Jika tidak menggunakan await: Fungsi fetch() akan langsung mengembalikan sebuah objek Promise yang masih berstatus pending, bukan data atau objek Response asli. Kode di baris berikutnya akan terus dieksekusi secara instan tanpa menunggu proses download data selesai. Akibatnya, operasi seperti response.json() akan menghasilkan galat (error) karena dipanggil pada objek Promise yang belum selesai diproses.

3. Serangan XSS (Cross-Site Scripting) adalah kerentanan keamanan web di mana penyerang berhasil menyisipkan skrip berbahaya (biasanya kode JavaScript) ke dalam halaman web yang nantinya dieksekusi oleh peramban (browser) milik pengguna lain.

Penyebab data via AJAX/JavaScript lebih rentan daripada Template Django:
- Template Django memiliki fitur keamanan bawaan berupa auto-escaping secara otomatis. Setiap kali variabel dirender menggunakan sintaks {{ variable }}, Django mengubah karakter khusus HTML (seperti < menjadi &lt; dan > menjadi &gt;) sehingga skrip tidak dapat berjalan sebagai kode yang dieksekusi peramban.
- AJAX / JavaScript melakukan manipulasi DOM di sisi klien (client-side). Jika data JSON dari server dimasukkan langsung ke HTML menggunakan properti seperti innerHTML tanpa sanitasi manual, peramban akan mengonstruksi string tersebut sebagai elemen HTML asli. Jika string tersebut memuat kode JavaScript jahat (misalnya <img src="x" onerror="alert('XSS')">), peramban akan langsung mengeksekusi skrip tersebut. Oleh karena itu, pengolahan data via AJAX mewajibkan sanitasi manual seperti penggunaan escapeHtml() atau pemakaian properti .textContent.

AI disclosure
Dalam pengerjaan tugas ini, saya menggunakan Gemini AI sebagai asisten diskusi dan pengerjaan untuk membantu memahami penerapan interaktivitas AJAX, debouncing, modal form, notifikasi toast, serta perlindungan XSS pada Django.

Bagian yang dibantu:
- Implementasi pemuatan data secara asynchronous (AJAX GET) menggunakan Fetch API beserta penanganan loading, empty, dan error state.
- Penerapan fitur pencarian dinamis dengan teknik debouncing untuk mengoptimalkan jumlah permintaan HTTP ke server.
- Pembuatan form penambahan data via modal dialog dan aksi hapus data secara asynchronous (AJAX POST) lengkap dengan validasi ModelForm, penanganan token CSRF, serta notifikasi toast.

# Tugas 6

1. REST (Representational State Transfer) adalah gaya arsitektur untuk layanan jaringan yang menggunakan resource, URL, HTTP method, representasi data, dan status HTTP secara konsisten. JSON saja belum cukup disebut RESTful karena format JSON hanya menjelaskan representasi data; API juga perlu mengikuti prinsip seperti resource yang dapat diidentifikasi, penggunaan method HTTP sesuai semantik, stateless request, dan status response yang tepat. PUT digunakan untuk mengganti representasi resource secara lengkap, sedangkan PATCH digunakan untuk mengubah sebagian field. Contohnya, PUT cocok ketika seluruh data pengalaman dikirim ulang, sementara PATCH cocok ketika hanya judul pengalaman yang diperbarui.

2. Serializer DRF mengubah object atau queryset Django menjadi representasi primitif yang dapat dikirim sebagai JSON, dan melakukan proses sebaliknya ketika menerima input. Serializer juga menjadi tempat validasi field, sanitasi teks, penentuan field read-only, serta pemetaan relasi. Dibanding merakit dictionary manual dengan JsonResponse, ModelSerializer lebih konsisten, mengurangi kode berulang, terintegrasi dengan validasi model, dan mudah digunakan kembali pada endpoint list maupun detail.

3. Autentikasi menentukan siapa pengguna yang mengirim request, sedangkan otorisasi menentukan tindakan apa yang boleh dilakukan pengguna tersebut. Hak akses harus diperiksa di permission class pada server karena tombol yang disembunyikan di template hanya memengaruhi tampilan dan dapat dilewati dengan mengirim request HTTP secara langsung. Pada API ini, pengunjung hanya dapat membaca, user biasa dapat memberi atau membatalkan star, Editor dapat melakukan PUT/PATCH, dan pemilik portofolio dapat membuat, mengubah, serta menghapus data.

4. SessionAuthentication memakai cookie session yang otomatis dikirim browser, sehingga request mutasi memerlukan token CSRF untuk membuktikan bahwa request berasal dari aplikasi yang sah. Tanpa perlindungan ini, situs lain dapat mencoba mengirim request atas nama session pengguna. Test dengan force_authenticate tidak cukup karena metode tersebut melewati proses login berbasis session dan pemeriksaan CSRF. Karena itu, test CSRF menggunakan APIClient dengan enforce_csrf_checks=True, login(), lalu membuktikan request tanpa token ditolak dan request dengan token berhasil.

AI disclosure

Dalam pengerjaan Tugas 6, saya menggunakan Codex sebagai asisten diskusi dan pengerjaan untuk membantu memahami penerapan Django REST Framework, pengelolaan permission berbasis peran, pengujian API, serta integrasi Fetch API pada halaman web.

Bagian yang dibantu:
- Pembuatan endpoint API untuk menampilkan, mencari, menambah, mengubah, menghapus, serta memberi atau membatalkan star pada data Experience.
- Pembuatan test API untuk permission, validasi input, CRUD, star, dan CSRF.
- Integrasi halaman Experience dengan Fetch API agar dapat berinteraksi tanpa reload halaman.
