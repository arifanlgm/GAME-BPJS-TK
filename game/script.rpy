# 1. Definisikan transformasinya di baris paling atas (sebelum label start)
transform sesuaikan_gui:
    zoom 1.4 

label start:

    # Show a background.
    scene bg_halaman with dissolve

    # 2. Panggil gambar tesini dan tambahkan transformasinya di sini
    show ms_cowok at center, sesuaikan_gui with dissolve

    # These display lines of dialogue.
    mc "Halo, selamat datang di BPJS Ketenagakerjaan"

    mc "Ada yang bisa dibantu?"
    menu:
        "Iya.":
            mc "Baiklah, sebelumnya apa kamu sudah tahu tentang BPJS Ketenagakerjaan"
        "Tidak.":
            mc "Baiklah"
        "..Diam saja..":
            jump say_nothing


    

    # This ends the game.
    return

label say_nothing:
    mc "Kalau  begitu, saya izin pamit..."