from faker import Faker


# faker para obtener ramdom data
# https://faker.readthedocs.io/en/stable/index.html
class DataRandom():

    def __init__(self):
        self.fake = Faker()
        self.data = []
        # self.con = con.Conexion()

    def generate_data(self,):
        # docstring
        """
        Genera datos aleatorios para la base de datos.
        Args:
        - datos (tuple): Tupla con los datos del evento a insertar.
        Returns:
        - None
        """
        for _ in range(2):
            self.data.append((
                self.fake.text(max_nb_chars=100),
                self.fake.date_between(end_date='today'),
                self.fake.time('%H:%M:%S'),
                self.fake.text(max_nb_chars=40),
                self.fake.pyint(min_value=1, max_value=10),
            ))
