import os
import csv
import re

# Podanie lokalizacji folderu z plikami PDF przez użytkownika
folder_path = input('Podaj lokalizację folderu z plikami PDF: ')

# Wyodrębnienie daty z nazwy folderu
folder_name = os.path.basename(folder_path)  # Pobranie nazwy folderu
date_from_folder = folder_name  # Zakładamy, że nazwa folderu to data w formacie DD-MM-YYYY

# Lista do przechowywania danych do CSV
data = []

# Przeszukiwanie folderu w poszukiwaniu plików PDF
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        # Rozdzielanie nazwy pliku na części
        parts = re.split(r'[_]', filename[:-4])  # Usuwamy '.pdf' i dzielimy po '_'
        
        # Dodajemy do listy danych
        data.append(parts)

# Ścieżka do pliku CSV z nową nazwą
csv_file_path = os.path.join(folder_path, f'Flashing raport from {date_from_folder}.csv')

# Zapis danych do pliku CSV
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    # Zapisujemy nagłówki (jeśli potrzebne)
    writer.writerow(['Product', 'Machine', 'Status', 'ID', 'SOCKET', 'Date', 'Time'])
    
    # Zapisujemy dane
    writer.writerows(data)

print(f'Dane zostały zapisane do pliku: {csv_file_path}')
