from calcolo_salario_medio import calcola_salario_medio

def verifica_possibilita_adozione(genere, razza):
    salario_medio = calcola_salario_medio(genere, razza)
    importo_minimo_adozione = 25000  # Importo minimo richiesto per l'adozione
    
    if isinstance(salario_medio, str):
        return salario_medio  # Restituisce il messaggio di informazioni salariali non disponibili
    elif salario_medio >= importo_minimo_adozione:
        return "Congratulazioni! Hai la possibilità di adottare un bambino."
    else:
        return "Mi dispiace, ma il tuo stipendio medio non ti permette di adottare un bambino."

# Esempi di utilizzo della funzione
print(verifica_possibilita_adozione("maschio", "bianco"))  # Restituirà "Congratulazioni! Hai la possibilità di adottare un bambino."
print(verifica_possibilita_adozione("femmina", "nero"))  # Restituirà "Mi dispiace, ma il tuo stipendio medio non ti permette di adottare un bambino."
print(verifica_possibilita_adozione("altro", "latino"))  # Restituirà "Informazioni salariali non disponibili per il genere o la razza specificati."
