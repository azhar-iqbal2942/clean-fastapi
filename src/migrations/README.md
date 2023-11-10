# To create new migration
```bash
alembic revision --autogenerate -m "Your message"
```

# To apply migration on DB
```bash
alembic upgrade heads
```