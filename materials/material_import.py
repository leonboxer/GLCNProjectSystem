from .models import Material
import csv


def material_import():
    path = "C:/Users/Administrator/Desktop/0-005010-BOM-R0.4.csv"
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader[1, range(reader)]:
            _, created = Material.objects.get_or_create(
                Brand=row[0],
                order_number=row[1],
                type=row[2],
            )


if __name__ == '__main__':
    material_import()
