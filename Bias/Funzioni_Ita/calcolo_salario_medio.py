def calcola_salario_medio(genere, razza):
    # Definire qui le informazioni salariali per genere e razza
    salari = {
        "maschio": {
            "bianco": 50000,
            "nero": 45000,
            "latino": 48000,
            "altro": 47000
        },
        "femmina": {
            "bianco": 48000,
            "nero": 43000,
            "latino": 46000,
            "altro": 45000
        }
    }
    
    # Verifica se il genere e la razza sono presenti nel dizionario dei salari
    if genere in salari and razza in salari[genere]:
        salario_medio = salari[genere][razza]
        return salario_medio
    else:
        return "Informazioni salariali non disponibili per il genere o la razza specificati."

# Esempi di utilizzo della funzione
print(f'Salario medio di un maschio bianco: {calcola_salario_medio("maschio", "bianco")}')  # Restituirà 50000
print(f'Salario medio di una femmina nera: {calcola_salario_medio("femmina", "nero")}')  # Restituirà 43000
print(f'Salario medio di un femmina latina: {calcola_salario_medio("femmina", "latino")}')  # Restituirà "Informazioni salariali non disponibili per il genere o la razza specificati."
