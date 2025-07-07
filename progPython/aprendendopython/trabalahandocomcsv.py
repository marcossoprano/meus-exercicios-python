import csv
dadosexemplo = [
    {"Nome": "Alice", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Bob", "Idade": 30, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carlos", "Idade": 22, "Cidade": "Belo Horizonte"}
]



arq3 = open("tabela.csv", 'w', newline="", encoding="utf-8")

colunas = ["Nome", "Idade", "Cidade"]


escritor = csv.DictWriter(arq3, fieldnames=colunas)
escritor.writeheader()
escritor.writerows(dadosexemplo)

print(f"Dados foram escritos em '{arq3}' com sucesso!")


arq3.close()