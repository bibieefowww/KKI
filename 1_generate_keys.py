# TUGAS 1 - Membuat sepasang kunci RSA (privat + publik)
# Jalankan:  python 1_generate_keys.py
# Untuk kunci "salah" (Tugas 5):  python 1_generate_keys.py teman
import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Awalan nama file (kosong = kunci asli, "teman" = kunci tambahan untuk Tugas 5)
awalan = sys.argv[1] + "_" if len(sys.argv) > 1 else ""

# Buat kunci RSA 2048 bit
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Simpan kunci privat (RAHASIA, dipakai untuk menandatangani)
with open(awalan + "private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption()))

# Simpan kunci publik (boleh dibagikan, dipakai untuk memeriksa tanda tangan)
with open(awalan + "public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo))

print("Kunci berhasil dibuat:", awalan + "private_key.pem", "dan", awalan + "public_key.pem")
