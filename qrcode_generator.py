import qrcode
import os
from datetime import datetime

DOWNLOAD_FOLDER = "Download"

def create_download_folder():
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

def generate_qr(link):
    create_download_folder()

    filename = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    filepath = os.path.join(DOWNLOAD_FOLDER, filename)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filepath)

    print(f"[OK] QR code enregistré : {filepath}")

# ===== BOUCLE INFINIE =====
if __name__ == "__main__":
    print("=== GENERATEUR QR CODE (BOUCLE) ===")
    print("Tape 'exit' pour quitter\n")

    while True:
        link = input("Entre un lien (https://...) : ")

        if link.lower() == "exit":
            print("Fermeture du programme...")
            break

        if not link.startswith("http"):
            print(" Lien invalide, recommence.\n")
            continue

        generate_qr(link)
        print("\n--- Nouveau QR possible ---\n")