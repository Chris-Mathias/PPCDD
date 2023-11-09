import pandas as pd
import csv
import banco

xlsFile = pd.read_excel('popxls.xls')
xlsFile.to_csv('popcsv.csv', index = None, header=True)

csvFile = open('popcsv.csv', 'r', encoding='utf-8')

conn = banco.getConexao()
cursor = conn.cursor()

for row in csv.DictReader(csvFile):

    uf = row['uf']
    cod_uf = int(row['cod_uf'])
    cod_municipio = int(row['cod_municipio'])
    nome_municipio = row['nome_municipio']
    populacao = int(row['populacao'])

    sql = "INSERT INTO municipio (id, uf, cod_uf, cod_municipio, nome_municipio, populacao) VALUES (default, %s, %s, %s, %s, %s)"
    x = (uf, cod_uf, cod_municipio, nome_municipio, populacao)
    cursor.execute(sql, x)

conn.commit()

conn.close()
csvFile.close()