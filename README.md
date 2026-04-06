# Proyecto Django Stateful y Stateless

Proyecto basado en la guía del PDF compartido. Incluye:

- Login y dashboard protegido usando sesiones de Django (`stateful`)
- API pública de productos en `/api/products/` que responde JSON sin autenticación (`stateless`)

## Ejecutar

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Luego abre:

- `http://127.0.0.1:8000/login/`
- `http://127.0.0.1:8000/api/products/`
