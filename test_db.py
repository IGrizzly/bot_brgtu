import sqlite3

conect = sqlite3.connect("test.db")
cursor = conect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS test(
   que_id integer PRIMARY KEY,
   que_one text,
   que_two text
   )
""")
conect.commit()


que_list = [(1,"Автомеханик","Авиаконструктор"),
            (2,"Егерь","Интервьюер"),
            (3,'Кондитер','Делопроизводитель'),
            (4,'Пасечник', "Администратор"),
            (5,"Радиооператор", "Актер"),
            (6, "Астроном", "Гид-экскурсовод"),
            (7,"Бактериолог","Корректор текстов"),
            (8,"Зоолог","Брокер"),
            (9,"Минеролог","Актер цирка"),
            (10,"Гувернентка","Работник архива"),
            (11,"Священик","Глава администрации"),
            (12,"Консультант по профориентации","Драматург"),
            (13,"Финансовый контролер","Директор"),
            (14,"Директор магазина","Композитор"),
            (15,"Шифровальщик","Искусствовед")]
cursor.executemany("INSERT INTO test VALUES(?,?,?);", que_list)

conect.commit()
