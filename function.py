# TUGAS FUNCTION & MANIPULASI STRING
# Nama   : Dendika Riyadi
# NIM    : 20250040005
# Sesi   : 12

def reverse_per_kata(kalimat):
    """
    Fungsi untuk membalik setiap kata dalam kalimat tanpa mengubah urutan kata.

    Cara kerja:
    1. Memisahkan kalimat menjadi list of words menggunakan method split()
    2. Untuk setiap kata, balik urutan karakternya menggunakan slicing [::-1]
    3. Gabungkan kembali kata-kata yang sudah dibalik dengan spasi

    Parameter:
        kalimat (str): String kalimat yang akan diproses

    Returns:
        str: Kalimat baru dengan setiap kata terbalik
    """
    kata_kata = kalimat.split()
    kata_terbalik = [kata[::-1] for kata in kata_kata]
    return " ".join(kata_terbalik)


def urutkan_kalimat(kalimat, urutan):
    """
    Fungsi untuk mengurutkan kata-kata dalam kalimat berdasarkan indeks yang ditentukan.

    Cara kerja:
    1. Memisahkan kalimat menjadi list of words
    2. Mengambil kata berdasarkan indeks yang terdapat pada list urutan
    3. Menggabungkan kembali menjadi kalimat baru

    Parameter:
        kalimat (str): String kalimat yang akan diurutkan
        urutan (list): List berisi angka (mulai dari 1)

    Returns:
        str: Kalimat baru dengan urutan kata sesuai parameter urutan
    """
    kata_kata = kalimat.split()
    hasil = []

    for posisi in urutan:
        hasil.append(kata_kata[posisi - 1])

    return " ".join(hasil)


def ganti_vokal(kalimat, opsi):
    """
    Fungsi untuk mengganti huruf vokal dengan simbol tertentu.

    Cara kerja:
    1. Menentukan mapping penggantian untuk vokal kecil dan vokal besar
    2. Jika opsi = 1: hanya vokal kecil yang diganti
    3. Jika opsi = 2: hanya vokal besar yang diganti
    4. Iterasi setiap karakter dan lakukan penggantian jika memenuhi kondisi

    Parameter:
        kalimat (str): String kalimat yang akan diproses
        opsi (int): 1 untuk ganti vokal kecil, 2 untuk ganti vokal besar

    Returns:
        str: Kalimat baru dengan vokal yang telah diganti sesuai opsi
    """
    mapping_kecil = {
        'a': '4',
        'i': '1',
        'u': '|_|',
        'e': '3',
        'o': '0'
    }

    mapping_besar = {
        'A': '4',
        'I': '1',
        'U': '|_|',
        'E': '3',
        'O': '0'
    }

    hasil = []

    if opsi == 1:
        for karakter in kalimat:
            if karakter in mapping_kecil:
                hasil.append(mapping_kecil[karakter])
            else:
                hasil.append(karakter)

    elif opsi == 2:
        for karakter in kalimat:
            if karakter in mapping_besar:
                hasil.append(mapping_besar[karakter])
            else:
                hasil.append(karakter)

    else:
        return kalimat

    return "".join(hasil)


# ==========================
# UJI PROGRAM
# ==========================

print("=" * 50)
print("UJI FUNGSI reverse_per_kata()")
print("=" * 50)
print('Input : "AKU CINTA KAMU"')
print('Output:', reverse_per_kata("AKU CINTA KAMU"))
print()

print("=" * 50)
print("UJI FUNGSI urutkan_kalimat()")
print("=" * 50)
print('Input kalimat : "HARI INI SEDANG BELAJAR PYTHON"')
print('Input urutan  : [5, 1, 4, 3, 2]')
print('Output       :', urutkan_kalimat(
    "HARI INI SEDANG BELAJAR PYTHON",
    [5, 1, 4, 3, 2]
))
print()

print("=" * 50)
print("UJI FUNGSI ganti_vokal()")
print("=" * 50)
print('Input : "Aku Cinta Kamu", opsi = 1')
print('Output:', ganti_vokal("Aku Cinta Kamu", 1))
print()

print('Input : "Aku Cinta Kamu", opsi = 2')
print('Output:', ganti_vokal("Aku Cinta Kamu", 2))
print()

print("=" * 50)
print("UJI TAMBAHAN")
print("=" * 50)
print(reverse_per_kata("PYTHON PROGRAMMING"))
print(urutkan_kalimat("SATU DUA TIGA EMPAT", [4, 2, 1, 3]))
print(ganti_vokal("Belajar Python itu Menyenangkan", 1))
print(ganti_vokal("Belajar Python itu Menyenangkan", 2))