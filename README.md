## 📱 termux.Control-Panel

### *Dynamic Data-Driven Web GUI Runner for Android Termux Ecosystem*
Brought to you by **SPY-E** & **123Tool**  

---

`termux.Control-Panel` adalah platform manajemen dan ekosistem kontrol perangkat Android berbasis web yang dijalankan langsung dari dalam lingkungan Termux. Berbeda dengan pengontrol remote tradisional yang menggunakan logika kode permanen (*hardcoded*), alat ini menerapkan arsitektur **Data-Driven UI**—di mana antarmuka pengguna (formulir input, slider, dropdown) di-generate secara otomatis dan dinamis berdasarkan skema perintah JSON (*Schema-Driven*).

Alat ini dirancang dengan mengutamakan aspek keamanan tinggi (*Secure Execution Layer*), menggunakan eksekusi proses berbasis list array tanpa melalui interupsi shell mentah, sehingga sepenuhnya kebal terhadap serangan *Shell/Command Injection*.

---

## 🔥 Fitur Utama

* **Dual-Branded Core:** Dikembangkan eksklusif untuk portofolio digital **SPY-E** dan **123Tool**.
* **Schema-Driven Dynamic Form:** Cukup ubah/tambah perintah di file konfigurasi backend (`command_schema.py`), maka tampilan form web, filter, tipe data input, dan validasi di frontend akan otomatis menyesuaikan diri tanpa perlu menyentuh kode HTML/JS.
* **Premium Neo-Brutalism UI:** Tampilan visual web modern, adaptif, ringkas, dan sangat ramah ketika diakses melalui perangkat seluler (*Mobile-First Responsive Design*).
* **Hardened Security Layer:** Validasi input menggunakan kombinasi Regex sisi klien dan server, serta pemanfaatan `subprocess` yang aman tanpa flag `shell=True`.
* **Full Termux-API Support:** Siap mengontrol fitur perangkat keras Android (Senter, Level Volume, Text-to-Speech, Sensor Getar, Status Baterai, GPS Lokasi, hingga Notifikasi Layar).

---

## 🛠️ Panduan Instalasi & Setup Lengkap

Ikuti langkah-langkah di bawah ini untuk memasang dan menjalankan panel kontrol pada aplikasi Termux Anda:

### 1. Persiapan Lingkungan Termux (Prasyarat)
Pastikan Termux Anda telah memiliki akses ke fitur internal Android dengan memasang paket **Termux:API**.

```bash
# Perbarui repositori dan instal paket utama
pkg update && pkg upgrade -y
pkg install python termux-api git -y
