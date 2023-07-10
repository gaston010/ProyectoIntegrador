from faker import Faker

# faker para obtener ramdom data
# https://faker.readthedocs.io/en/stable/index.html

fake = Faker()

data = []


# reccorre un for dando datos ramdom mediante la libreria de Faker
for _ in range(1):
    data.append((
        fake.text(max_nb_chars=100),
        fake.date('%Y-%m-%d'),
        fake.time('%H:%M:%S'),
        fake.text(max_nb_chars=40),
        fake.pyint(min_value=1, max_value=24),
    ))
