URL PWS: https://amadio-juno-footballshop.pbp.cs.ui.ac.id/

Tugas Individu 2
    1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat sebuah proyek Django baru.
        1. Membuat virtual environment pada direktori proyek
        2. Menyiapkan dan meng-install dependencies Django
        3. Membuat proyek Django dengan nama football_shop
    - Membuat aplikasi dengan nama main pada proyek tersebut.
        1. Membuat aplikasi main dengan command python manage.py startapp main
        2. Memasukkan main ke dalam setting.py di INSTALLED_APPS
    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        1. Mengkonfigurasi urls.py pada main
        2. Mengkonfigurasi urls.py pada football_shop agar agar proyek dapat melakukan pemetaan ke rute URL pada aplikasi main
    - Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
        name sebagai nama item dengan tipe CharField.
        price sebagai harga item dengan tipe IntegerField.
        description sebagai deskripsi item dengan tipe TextField.
        thumbnail sebagai gambar item dengan tipe URLField.
        category sebagai kategori item dengan tipe CharField.
        is_featured sebagai status unggulan item dengan tipe BooleanField.
        1. Membuat Product dengan atribut name, brand, price, description, rating, thumbnail, category, dan is_featured pada models.py
    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        1. Mengisi main.html dengan sintaks Django untuk menampilkan name dan class, yang merujuk pada views.py pada main
    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        1. Mengimpor fungsi include untuk mengimpor URL dari main ke urls.py football_shop
        2. Memasukkan URL pattern kosong agar aplikasi main dapat langsung diakses
    - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        1. Mengkonfigurasi environs pada PWS sesuai .env.prod
        2. Menambahkan branch pada pws
        3. Melakukan add, commit, push ke github dan juga PWS -> memasukkan kredensial

    2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
        Request dari browser
            |
            V
        urls.py - mencocokkan url request dengan fungsi pada views.py
            |
            V
        views.py - menerima request dan mengambil data dari models.py 
            |
            V
        models.py - memberi data
            |
            V
        views.py - menerima data
            |
            V
        template - menampilkan data ke user


    3. Jelaskan peran settings.py dalam proyek Django!
        File settings.py mengkonfigurasi berbagai aspek aplikasi Django, seperti database, aplikasi yang terpasang (INSTALLED_APPS), middleware, serta lokasi file statis dan media. File ini juga mengatur pengaturan keamanan seperti SECRET_KEY, proteksi CSRF, serta pengaturan internasionalisasi dan debugging. Secara keseluruhan, settings.py mengontrol bagaimana aplikasi Django berfungsi.

    4. Bagaimana cara kerja migrasi database di Django?
        Migrasi di Django digunakan untuk menyinkronkan model dengan database. Setelah mengubah model, kita membuat file migrasi dengan python manage.py makemigrations. Perintah python manage.py migrate kemudian diterapkan untuk memperbarui struktur database sesuai dengan perubahan model. Django secara otomatis melacak migrasi yang telah diterapkan.

    5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
        Django dipilih sebagai framework pembelajaran pertama karena kemudahan penggunaan dan dokumentasinya yang lengkap. Dengan fitur bawaan seperti autentikasi pengguna, admin panel, dan ORM, Django memudahkan pemula untuk mulai membangun aplikasi web tanpa konfigurasi rumit. Selain itu, Django menggunakan Python, yang dikenal mudah dipahami, dan memiliki komunitas besar yang mendukung developer pemula.

    6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
        Sudah baik dan mudah dimengerti

Tugas Individu 3
    1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
        - Data delivery memungkinkan komunikasi efektif antara client dan server, mendukung integrasi komponen yang berbeda, dan memungkinkan pembaruan data tanpa reload penuh. Format terstandarisasi seperti JSON dan XML memfasilitasi pertukaran data antar sistem, mendukung arsitektur yang modular dan terpisah antara frontend dan backend.

    2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
        - JSON lebih populer karena sintaksnya lebih ringkas, terintegrasi dengan JavaScript, memiliki ukuran data lebih kecil, dan lebih mudah dibaca. Dibandingkan XML yang lebih verbose, JSON menawarkan parsing lebih cepat dan dukungan tipe data natif yang menyederhanakan serialisasi. XML masih berguna untuk dokumen kompleks yang memerlukan namespaces atau validasi skema yang ketat.

    3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
        - Method is_valid() memvalidasi input pengguna sebelum diproses lebih lanjut, mengembalikan boolean yang menunjukkan validitas data. Fungsi ini mencegah data berbahaya masuk ke database, menyediakan pesan kesalahan untuk feedback pengguna, dan menghindari validasi manual yang rawan kesalahan, sehingga meningkatkan keamanan dan pengalaman pengguna.

    4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
        - CSRF token melindungi aplikasi dari serangan Cross-Site Request Forgery dengan memverifikasi bahwa request berasal dari aplikasi yang sah. Tanpa token ini, penyerang bisa membuat situs berbahaya dengan form tersembunyi yang mengirim request ke aplikasi target menggunakan cookies otentikasi pengguna yang sudah login, potensial melakukan tindakan berbahaya seperti transfer dana atau perubahan password tanpa sepengetahuan korban.

    5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
        1. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
            - Membuat function show_xml, show_json, show_xml_by_id, dan show_json_by_id dan mengimport HttpResponse dan serializers pada views.py main
            - Mengimport function show_xml, show_json, show_xml_by_id, dan show_json_by_id pada urls.py main
        2. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
            - Menambahkan path url pada urlpatterns untuk function-function tadi pada urls.py main
        3. Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
            - Menambahkan add_product.html
            - Menambahkan show_product.html
        4. Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
            - Menambahkay forms.py yang berisi "name", "brand", "price", "description", "rating", "thumbnail", "category", dan "is_featured"
        5. Membuat halaman yang menampilkan detail dari setiap data objek model.
            - Mengimplementasikan show_product.html

    6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
        Sudah baik dan mudah dimengerti

    7. Screenshot postman
        https://drive.google.com/drive/folders/1zvVjnvm5FTsAuevugN86n3dece2psdFX?usp=sharing

Tugas Individu 4
    1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
        - Django AuthenticationForm adalah form built-in di Django untuk menangani proses login pengguna. Form ini secara otomatis memvalidasi username dan password, memudahkan implementasi autentikasi
        - Kelebihannya adalah sangat praktis dan mengurangi penulisan kode yang berulang.
        - Kekurangannya adalah terbatas dalam kustomisasi, terutama jika aplikasi membutuhkan logika autentikasi yang lebih kompleks.
    2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
        - Autentikasi adalah proses verifikasi identitas pengguna (misalnya, melalui username dan password), sedangkan otorisasi adalah proses pemberian hak akses kepada pengguna setelah identitasnya terverifikasi. Django mengelola autentikasi dengan model User dan form AuthenticationForm, sementara otorisasi menggunakan sistem permissions dan grup untuk mengatur akses ke berbagai bagian aplikasi.
    3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
        - Session menyimpan data di server, sehingga lebih aman dan tidak mudah dimanipulasi oleh pengguna, tetapi dapat mempengaruhi performa jika data terlalu besar. Cookies menyimpan data di sisi klien, mengurangi beban server dan meningkatkan kecepatan, namun lebih rentan terhadap serangan seperti pencurian data atau manipulasi pengguna.
    4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
        - Penggunaan cookies tidak sepenuhnya aman secara default karena berisiko terpapar serangan seperti XSS atau CSRF. Risiko ini dapat diminimalkan dengan enkripsi data, serta pengaturan atribut cookie seperti HttpOnly (mencegah akses JavaScript) dan Secure (hanya dikirim melalui HTTPS). Django membantu dengan mengaktifkan perlindungan CSRF dan menyediakan cara untuk mengatur cookies dengan aman.
    5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step:
        1. Implementasi registrasi, login, dan logout:
            - Membuat fungsi register, login_user, dan logout_user di views.py
            - Membuat template register.html dan login.html
            - Mengimplementasi cookie last_login untuk mencatat waktu login
            - Menambahkan path URL untuk ketiga fungsi di urls.py
        2. Membuat dua akun pengguna dengan tiga dummy data:
            - Menggunakan form register untuk membuat dua akun berbeda
            - Menambahkan tiga produk untuk setiap akun melalui form Add Product
        3. Menghubungkan model Product dengan User:
            - Menambahkan ForeignKey(User) pada model Product
            - Memodifikasi add_product untuk menyimpan user yang login sebagai pemilik
            - Menjalankan makemigrations dan migrate
            - Menambahkan filter produk (all/my) di halaman utama
        4. Menampilkan informasi pengguna dan cookies:
            - Menampilkan username dan last_login di halaman utama
            - Menyimpan cookie saat login dan menghapusnya saat logout
            - Menambahkan informasi author pada halaman detail produk

Tugas Individu 5
    1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
        - !important (mengalahkan semua, jika sama -> spesifisitas + urutan sumber)
        - Inline style (style="...")
        - Selector berdasarkan spesifisitas: ID (#id) > class/attribute/pseudo-class (.class, [attr], :hover) > elemen/pseudo-element (div, ::after)
        - Jika spesifisitas sama -> aturan yang ditulis terakhir (source order) menang.
    2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
        - Penting karena perangkat berlainan ukuran, meningkatkan UX, aksesibilitas, SEO, dan maintainability.
        - Contoh sudah responsive: Wikipedia, Twitter, tampil konsisten di mobile & desktop.
        - Contoh belum responsive: situs web lama/legacy (beberapa situs pemerintahan/korporat tua), biasanya tampilan rusak di layar kecil karena layout tetap (fixed width). Contoh: SIAKNG
    3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
        - Margin: ruang luar elemen (memisahkan elemen lain). CSS: margin: 10px,
        - Border: garis di tepi elemen, di antara padding dan margin. CSS: border: 1px solid #000,
        - Padding: ruang dalam elemen antara konten dan border. CSS: padding: 8px,
    4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
        - Flexbox: layout satu dimensi (baris/kolom) untuk alignment dan distribusi ruang pada item, bagus untuk navbar, card row, centering. Properti utama: display: flex, justify-content, align-items.
        - Grid: layout dua dimensi (baris + kolom) untuk tata letak kompleks halaman, bagus untuk desain grid halaman, dashboard. Properti utama: display: grid, grid-template-columns/rows, gap.
        - Flex untuk item linear, grid untuk susunan kompleks dua arah.
    5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
        -  Implementasikan fungsi untuk menghapus dan mengedit product.
            1. Membuat fungsi edit_product yang menggunakan ProductForm dengan instance product yang sudah ada
            2. Membuat fungsi delete_product untuk menghapus produk berdasarkan ID
            3. Mendefinisikan URL patterns di urls.py:
            4. Menambahkan path edit_product/<str:id>/str:id/ dan delete_product/<str:id>/str:id/
            5. Membuat template edit_product.html dengan form untuk mengedit produk
        - Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
            - Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.
            - Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
                - Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
                - Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card
            1. Mengimplementasikan Tailwind CSS via CDN di base.html
            2. Mendesain form dengan background image dan efek overlay
            3. Menggunakan card style dengan warna gelap dan box-shadow
            4. Menerapkan desain clean dengan spacing yang konsisten
            5. Menambahkan validasi form dan handling error
            6. Menampilkan informasi lengkap dengan layout yang menarik
            7. Menambahkan rating stars dan formating harga
            8. Menampilkan gambar no-products.png dan pesan informatif
            9. Menambahkan tombol "Add New Product" untuk UX yang lebih baik
        - Untuk setiap card product, buatlah dua buah
         button untuk mengedit dan menghapus product pada card tersebut!
            1. Membuat template card_product.html yang dapat digunakan kembali
            2. Menerapkan grid layout responsif (1 kolom mobile, 3 kolom desktop)
            3. Menambahkan hover effect dan transisi pada card
        - Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
            1. Mendesain navbar yang fixed di bagian atas
            2. Mengimplementasikan menu mobile yang disembunyikan dan dapat ditoggle
            3. Menggunakan flexbox dan media queries dengan Tailwind
            4. Menu desktop: menampilkan semua item secara horizontal
            5. Menu mobile: menggunakan hamburger button dan panel dropdown
            6. Menambahkan fitur highlight menu aktif berdasarkan kategori yang dipilih