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

def clean_and_convert_to_int(value):
    try:
        return int(value.strip())
    except ValueError:
        return 0  # Devuelve 0 si no se puede convertir a entero

def load_csv_to_db(csv_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_filepath = os.path.join(base_dir, csv_filename)

    with open(csv_filepath, newline='', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            print(row)
            medidor_val = row['medidor'][-4:]
            loteo_instance = Loteo.objects.get(pk=2)  # Obtiene la instancia de Loteo, ajusta según sea necesario
            
            medidor, created = Medidor.objects.get_or_create(
                medidor=medidor_val,
                defaults={
                    'cliente': row['cliente'],
                    'fecha_instalacion': parse_date(row['fecha_instalacion']),
                    'lote': row['lote'],
                    'manzana': row['manzana'],
                    'lectura_anterior': clean_and_convert_to_int(row['lectura_anterior']),
                    'lectura_actual': clean_and_convert_to_int(row['lectura_actual']),
                    'loteo_name': loteo_instance
                }
            )
            if not created:
                # Actualiza el objeto si ya existe
                medidor.cliente = row['cliente']
                medidor.fecha_instalacion = parse_date(row['fecha_instalacion'])
                medidor.lote = row['lote']
                medidor.manzana = row['manzana']
                medidor.lectura_anterior = clean_and_convert_to_int(row['lectura_anterior'])
                medidor.lectura_actual = clean_and_convert_to_int(row['lectura_actual'])
                medidor.loteo_name = loteo_instance
                medidor.save()

            print(f"Medidor {row['medidor']} guardado con éxito")

if __name__ == "__main__":
    csv_filepath = 'Libro2.csv'  # Cambia esto a la ruta de tu archivo CSV
    load_csv_to_db(csv_filepath)




""" def update_consumo():
    medidores = Medidor.objects.all()
    for medidor in medidores:
        # Calcula el consumo
        medidor.consumo = medidor.lectura_actual - medidor.lectura_anterior
        # Guarda la instancia con el consumo actualizado
        medidor.save()
        print(f"Medidor {medidor.medidor}: consumo actualizado a {medidor.consumo}")

if __name__ == "__main__":
    update_consumo() """