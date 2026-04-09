@echo off
echo ===============================
echo Installation des dependances...
echo ===============================

pip install qrcode[pil]

echo ===============================
echo Lancement du generateur...
echo ===============================

python qrcode_generator.py

pause