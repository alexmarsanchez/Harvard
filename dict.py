students=[
    {"name": "Hermione","House":"Gryffindor","Patronus":"Otter"}, #1diccionario
    {"name": "Harry","House":"Gryffindor","Patronus":"Stag"}, # 2º diccionario
    {"name": "Ron","House":"Gryffindor","Patronus":"Jack Russel Terrier"}, #3º diccionario
    {"name": "Draco","House":"Slyterin","Patronus": None} #None significa que no hay valor, está vacío ese lugar, va con la primera es mayúscula
]

for student in students:
    print(student["name"], student["House"], student["Patronus"], sep=", ")
# me faltaba las comas para separar cada titulo y datos y llamé a mostrar House, con mayúscula y todo
