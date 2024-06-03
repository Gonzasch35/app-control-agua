import csv
import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from datos.models import Medidor, Loteo

def parse_date(date_str):
    if not date_str:
        return None
    return datetime.strptime(date_str, '%d/%m/%Y').date()

def load_csv_to_db(csv_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_filepath = os.path.join(base_dir, csv_filename)

    with open(csv_filepath, newline='', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            print(row)
            medidor, created = Medidor.objects.get_or_create(
                medidor=row['medidor'],
                defaults={
                    'cliente': row['cliente'],
                    'fecha_instalacion': parse_date(row['fecha_instalacion']),
                    'lote': row['lote'],
                    'manzana': row['manzana'],
                    'lectura_anterior': row['lectura_anterior'],
                    'lectura_actual': row['lectura_actual']
                }
            )
            if not created:
                # Actualiza el objeto si ya existe
                medidor.cliente = row['cliente']
                medidor.fecha_instalacion = parse_date(row['fecha_instalacion'])
                medidor.lote = row['lote']
                medidor.manzana = row['manzana']
                medidor.lectura_anterior = row['lectura_anterior']
                medidor.lectura_actual = row['lectura_actual']
                medidor.save()

            print(f"Medidor {row['medidor']} guardado con éxito")

if __name__ == "__main__":
    csv_filepath = 'Libro1.csv'  # Cambia esto a la ruta de tu archivo CSV
    load_csv_to_db(csv_filepath)