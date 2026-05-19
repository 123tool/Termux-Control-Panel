COMMAND_SCHEMAS = {
    "torch": {
        "title": "🔦 Kontrol Senter",
        "description": "Menyalakan atau mematikan lampu senter perangkat.",
        "binary": "termux-torch",
        "params": [
            {
                "name": "state",
                "label": "Status Senter",
                "type": "select",
                "options": ["on", "off"],
                "default": "off",
                "validation": "^(on|off)$"
            }
        ]
    },
    "volume": {
        "title": "🔊 Volume Suara",
        "description": "Mengatur volume audio untuk berbagai jenis aliran.",
        "binary": "termux-volume",
        "params": [
            {
                "name": "stream",
                "label": "Jenis Aliran Audio",
                "type": "select",
                "options": ["music", "alarm", "notification", "ring", "system", "call"],
                "default": "music",
                "validation": "^(music|alarm|notification|ring|system|call)$"
            },
            {
                "name": "volume",
                "label": "Level Volume (0-15)",
                "type": "range",
                "min": 0,
                "max": 15,
                "default": 5,
                "validation": "^[0-9]+$"
            }
        ]
    },
    "tts": {
        "title": "🗣️ Text-to-Speech (Suara)",
        "description": "Berbicara menggunakan mesin penyuara Android.",
        "binary": "termux-tts-speak",
        "params": [
            {
                "name": "text",
                "label": "Teks yang Diucapkan",
                "type": "text",
                "placeholder": "Halo bos bro cak...",
                "default": "Halo SPY E dan 123Tool siap beraksi",
                "validation": "^[a-zA-Z0-9\s\.,!\?]+$"
            }
        ]
    },
    "vibrate": {
        "title": "📳 Efek Getar",
        "description": "Menggetarkan perangkat dalam durasi milidetik.",
        "binary": "termux-vibrate",
        "params": [
            {
                "name": "duration",
                "label": "Durasi Getar (Milidetik)",
                "type": "number",
                "default": 500,
                "validation": "^[0-9]+$"
            },
            {
                "name": "force",
                "label": "Paksa Getar (Meskipun Mode Senyap)",
                "type": "select",
                "options": ["Ya", "Tidak"],
                "default": "Tidak",
                "validation": "^(Ya|Tidak)$"
            }
        ]
    },
    "battery": {
        "title": "🔋 Status Baterai",
        "description": "Mengambil informasi kesehatan, persentase, dan suhu baterai.",
        "binary": "termux-battery-status",
        "params": [] # Tidak butuh parameter
    },
    "location": {
        "title": "📍 Lokasi GPS",
        "description": "Mendapatkan koordinat GPS terkini dari perangkat.",
        "binary": "termux-location",
        "params": [
            {
                "name": "provider",
                "label": "Penyedia Lokasi",
                "type": "select",
                "options": ["gps", "network", "passive"],
                "default": "gps",
                "validation": "^(gps|network|passive)$"
            }
        ]
    },
    "toast": {
        "title": "💬 Tampilkan Pesan Toast",
        "description": "Memunculkan notifikasi pop-up kecil (toast) di layar Android.",
        "binary": "termux-toast",
        "params": [
            {
                "name": "text",
                "label": "Isi Pesan",
                "type": "text",
                "placeholder": "Pesan rahasia...",
                "default": "Sistem Terhubung!",
                "validation": "^[a-zA-Z0-9\s\.,!\?]+$"
            },
            {
                "name": "color",
                "label": "Warna Background",
                "type": "select",
                "options": ["black", "white", "red", "green", "blue", "yellow"],
                "default": "black",
                "validation": "^(black|white|red|green|blue|yellow)$"
            }
        ]
    }
}
