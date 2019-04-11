
def generate_dict(line):
    values = {key: value for key, value in
              zip(atributos, line.strip().split(","))}
    del values["alteraciones"]
    return values


atributos = ["tipo", "consumo", "energia", "region",
             "comuna", "alteraciones"]

def generator():
    for i in range(4):
        sistema = []
        with open(f"sistemas/sistema_{i}.csv", "r", encoding="utf-8") as file:
            sistema.append(generate_dict(file.readline()))
            for line in file:
                sistema.append(generate_dict(line))
        yield sistema

generador = generator()

def obtener_sistema():
    return next(generador)
