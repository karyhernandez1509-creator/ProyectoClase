from django.db import migrations


def seed_products(apps, schema_editor):
    Product = apps.get_model("core", "Product")
    Product.objects.bulk_create(
        [
            Product(name="Laptop", price=1200),
            Product(name="Mouse", price=25),
            Product(name="Teclado mecanico", price=80),
            Product(name="Monitor 24 pulgadas", price=240),
        ]
    )


def remove_seed_products(apps, schema_editor):
    Product = apps.get_model("core", "Product")
    Product.objects.filter(
        name__in=[
            "Laptop",
            "Mouse",
            "Teclado mecanico",
            "Monitor 24 pulgadas",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_products, remove_seed_products),
    ]
