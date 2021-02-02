import camelot
import pandas as pd


tables = camelot.read_pdf("./data/horarios.pdf")
# tables.export("prueba.csv", f = "csv", compress=False)

table_horarios = tables[0].df
table_asignatura = tables[1].df

# table_horarios.to_json("./out/horarios.json")
# table_asignatura.to_json("../out/asignaturas.json")


# print(table_horarios.size)
# print(table_horarios)
print(table_asignatura)
