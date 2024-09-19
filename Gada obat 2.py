# Hal yang diperlukan (deklarasi list)
daftar_obat = []
daftar_transaksi = []

print("     _____   ______   _______   _________   ______   __   __  ")
print("    /  _  | |  __  | |   _   | |___   ___| |   ___| |  | |  / ")
print("   /  / | | | |__| | |  | |  |     | |     |  |___  |  |_| /  ")
print("  /  /__| | |  ____| |  | |  |     | |     |   ___| |   _ |   ")
print(" /   __   | | |      |  |_|  |     | |     |  |___  |  | | \\ ")
print("/___/  |__| |_|      |_______|     |_|     |______| |__| |__\\ \n")

print(" _____________________________________________________________ \n")
print("| ----------------------- MENU UTAMA ------------------------ |")
print(" _____________________________________________________________ \n")

# Menu Utama Sistem Apotek
while True:
    print("SISTEM APOTEK")
    print("1. Tambah Obat")
    print("2. Hapus Obat")
    print("3. Lihat Stok Obat")
    print("4. Jual Obat")
    print("5. Laporan Transaksi")
    print("6. Peringatan Stok Rendah")
    print("7. Peringatan Obat Kadaluarsa")
    print("8. Diskon Obat")
    print("9. Laporan Keuangan")
    print("10. Keluar")
    menu = int(input("Pilih menu : "))

    # Percabangan & Menu yang dipilih 1-8
    if menu == 1:
        obat = []
        nama_obat = input("Masukkan nama obat : ")
        obat.append(nama_obat)
        harga_obat = int(input("Masukkan harga obat : "))
        obat.append(harga_obat)
        stok_obat = int(input("Masukkan jumlah obat : "))
        obat.append(stok_obat)
        kadaluarsa_obat = input("Masukkan tanggal kadaluarsa (YYYY MM DD) : ")
        obat.append(kadaluarsa_obat)
        daftar_obat.append(obat)
        print("\n")
    elif menu == 2:
        if daftar_obat != []:
            hapus_obat = input("Masukkan nama obat yang ingin dihapus : ")
            pr = False
            for i in range(len(daftar_obat)):
                if daftar_obat[i][0] == hapus_obat:
                    del daftar_obat[i]
                    print("Obat",hapus_obat,"telah dihapus dari stok \n")
                    pr = True
                    break
            if pr == False:
                print("Nama obat salah atau tidak ada. Coba lagi! \n")
        else:
            print("Tidak ada stok obat \n")
    elif menu == 3:
        if daftar_obat != []:
            for i in range(len(daftar_obat)):
                print("Nama obat :", daftar_obat[i][0], end=", ")
                print("Harga obat :", int(daftar_obat[i][1]), end=", ")
                print("Stok obat :", int(daftar_obat[i][2]), end=", ")
                print("Tanggal kadaluarsa obat :", daftar_obat[i][3])
            print("\n")
        else:
            print("Tidak ada stok obat \n")
    elif menu == 4:
        jual_obat = input("Masukkan nama obat yang ingin dijual : ")
        obat_terjual = int(input("Jumlah obat yang ingin dijual : "))
        transaksi = []
        for i in range(len(daftar_obat)):
            if daftar_obat[i][0] == jual_obat:
                if daftar_obat [i][2] >= obat_terjual:
                    transaksi.append(jual_obat)
                    transaksi.append(obat_terjual)
                    transaksi.append(obat_terjual*daftar_obat[i][1])
                    daftar_transaksi.append(transaksi)
                    daftar_obat[i][2] -= obat_terjual
                    print("Obat",jual_obat,"terjual sebanyak",obat_terjual,"dengan harga",obat_terjual*daftar_obat[i][1], "\n")
                    break
                else:
                    print("Obat dijual melebihi stok. Mungkin anda salah:) \n")
                    break
    elif menu == 5:
        if daftar_transaksi != []:
            print("Transaksi berhasil dicatat!")
            for i in range(len(daftar_transaksi)):
                print(daftar_transaksi[i][0], end=", ")
                print("jumlah :", daftar_transaksi[i][1], end=", ")
                print("Total harga :", daftar_transaksi[i][2])
            print("\n")
        else:
            print("Tidak ada transaksi dilakukan!")
    elif menu == 6:
        batas_stok = int(input("Masukkan batas stok obat : "))
        for i in range(len(daftar_obat)):
            if daftar_obat[i][2] <= batas_stok:
                print("Peringatan: stok", daftar_obat[i][0],"tinggal",daftar_obat[i][2], "unit")
        print("\n")
    elif menu == 7:
        tanggal = input("Masukkan tanggal hari ini (YYYY MM DD) : ").split()
        tanggal= list(map(int, tanggal))
        tanggal_now = tanggal[0]*365 + tanggal[1]*30 + tanggal[2]
        batas_kadaluarsa = input("Masukkan batas kadaluarsa (x hari): ").split()
        batas_kadaluarsa[0] = int(batas_kadaluarsa[0])
        pr = False
        if daftar_obat != []:
            for i in range(len(daftar_obat)):
                kadaluarsa = daftar_obat[i][3].split()
                kadaluarsa = list(map(int, kadaluarsa))
                hari_kadaluarsa = kadaluarsa[0]*365 + kadaluarsa[1]*30 + kadaluarsa[2]
                if hari_kadaluarsa - tanggal_now <= batas_kadaluarsa[0]:
                     pr = True
                     print("Periksa obat", daftar_obat[i][0], "dengan tanggal kadaluarsa", daftar_obat[i][3])
            print("\n")
            if pr == False:
                print("Semua obat masih aman dan berlaku \n")
        else:
            print("Tidak ada stok obat \n")
    elif menu == 8:
        obat_diskon = input("Masukkan obat yang ingin didiskon: ")
        diskon = float(input("Masukkan diskon yang ingin diberikan (x%): "))
        diskon /= 100
        if daftar_obat != []:
            for i in range(len(daftar_obat)):
                if daftar_obat[i][0] == obat_diskon:
                    daftar_obat[i][1] *= (1-diskon)
                    print("Obat", daftar_obat[i][0], "berhasil didiskon!")
                    print("Harga awal: ", int(daftar_obat[i][1]/(1-diskon)))
                    print("Harga setelah diskon: ", int(daftar_obat[i][1]) )
            print("\n")
        else:
            print("Tidak ada stok obat \n")
    elif menu == 9:
        if daftar_transaksi != []:
            print("Laporan harian:")
            for i in range(len(daftar_transaksi)):
                print(daftar_transaksi[i][0],end=", ")
                print(daftar_transaksi[i][1],"unit", end=", ")
                print( daftar_transaksi[i][2])
            print("\n")
        else:
            print("Tidak ada transaksi hari ini!")
    elif menu == 10:
        print("Sistem Apotek berhenti. Have a good day! \n")
        break
    else:
        print("Menu tidak ada. Pilih yang bener dong! \n")