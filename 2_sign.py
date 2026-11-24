# TUGAS 2 - Menandatangani pesan.docx -> menghasilkan pesan.sig
# Jalankan:  python 2_sign.py
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# 1. Baca isi pesan.docx
with open("pesan.docx", "rb") as f:
    pesan = f.read()

# 2. Baca kunci privat
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# 3. Hash pesan dengan SHA-256, lalu tandatangani dengan kunci privat
signature = private_key.sign(pesan, padding.PKCS1v15(), hashes.SHA256())

# 4. Simpan tanda tangan ke file
with open("pesan.sig", "wb") as f:
    f.write(signature)

print("Pesan berhasil ditandatangani -> pesan.sig")
