from datetime import datetime


SQL_BASE = "sqlite:///employees.db"
LAST_NAMES = [('Ivanov', 'Ivanovna'),
              ('Petrov', 'Petrova'),
              ('Sidorov', 'Sidorova'),
              ('Smirnov', 'Smirnova'),
              ('Agapov', 'Agapova'),
              'Vashenko',
              ('Fedorov', 'Fedorova'),
              'Fedoseenko',
              ('Fillipov', 'Fillipova'),
              ('Kurokodov', 'Kurokodova'),
              'Zaichenko',
              ('Belov', 'Belova'),
              ('Tarkov', 'Tarkova')]
FIRST_MALE_NAMES = ['Ivan', 'Kirill', 'Vadim', 'Sergey', 'Michail',
                    'Roman', 'Aleksandr', 'Andrey', 'Konstantin', 'Evgeniy', 'Yuriy']
FIRST_FEMALE_NAMES = ['Evgenia', 'Tatiana', 'Elena', 'Valeria', 'Uliya',
                      'Irina', 'Polina', 'Nina', 'Margarita', 'Sveta', 'Valentina']
PATRINYMICS = [('Ivanovich', 'Ivanovna'),
               ('Kirillovich', 'Kirillovna'),
               ('Vadimovich', 'Vadimovna'),
               ('Sergeevich', 'Sergeevna'),
               ('Michailovich', 'Michailovna'),
               ('Romanovich', 'Romanovna'),
               ('Aleksandrovich', 'Aleksandrovna'),
               ('Andreevich', 'Andreevna')]
START_GENERATED_DATE = datetime(1960, 1, 1)
END_GENERATED_DATE = datetime(2006, 12, 31)
QUANTITY_OF_ENTRIES = 100000
