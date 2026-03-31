# 1. Definisikan transformasinya di baris paling atas (sebelum label start)
transform sesuaikan_gui:
    zoom 1.4 

label start:

    # Show a background. 
    scene bg_parkiran

    # 2. Panggil gambar tesini dan tambahkan transformasinya di sini
    show ms_cowok at center, sesuaikan_gui

    # These display lines of dialogue.
    mc "Halo, selamat datang di BPJS Ketenagakerjaan"

    mc "Ada yang bisa dibantu?"

    # This ends the game.
    return