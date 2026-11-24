# TUGAS 3, 4, 5 - Memeriksa tanda tangan
# Jalankan biasa:           python 3_verify.py
# Tugas 4 (pesan diubah):   python 3_verify.py pesan_diubah.docx
# Tugas 5 (key salah):      python 3_verify.py pesan.docx teman_public_key.pem
import sys
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Nama file bisa diganti lewat perintah; kalau tidak diisi, pakai bawaan
file_pesan = sys.argv[1] if len(sys.argv) > 1 else "pesan.docx"
file_kunci = sys.argv[2] if len(sys.argv) > 2 else "public_key.pem"

with open(file_pesan, "rb") as f:
    pesan = f.read()
with open("pesan.sig", "rb") as f:
    signature = f.read()
with open(file_kunci, "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

print("File pesan :", file_pesan)
print("Public key :", file_kunci)

try:
    public_key.verify(signature, pesan, padding.PKCS1v15(), hashes.SHA256())
    print("HASIL VERIFIKASI: BERHASIL")
except InvalidSignature:
    print("HASIL VERIFIKASI: GAGAL")
