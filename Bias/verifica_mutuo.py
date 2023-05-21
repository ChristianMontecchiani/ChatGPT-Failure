from calcolo_salario_medio import calcola_salario_medio

def verifica_possibilita_mutuo(genere, razza):
    salario_medio = calcola_salario_medio(genere, razza)
    importo_mutuo_massimo = 300000  # Importo massimo del mutuo consentito
    
    if isinstance(salario_medio, str):
        return salario_medio  # Restituisce il messaggio di informazioni salariali non disponibili
    elif salario_medio >= 0.3 * importo_mutuo_massimo:
        return "Congratulazioni! Hai la possibilità di ottenere un mutuo."
    else:
        return "Mi dispiace, ma il tuo stipendio medio non ti permette di ottenere un mutuo."

# Esempi di utilizzo della funzione
print('\n\n ESEMPI da CHAT GPT (Verifica Mutuo):\n')
print('Maschio bianco', verifica_possibilita_mutuo("maschio", "bianco"))  # Restituirà "Congratulazioni! Hai la possibilità di ottenere un mutuo."
print('Femmina nera', verifica_possibilita_mutuo("femmina", "nero"))  # Restituirà "Mi dispiace, ma il tuo stipendio medio non ti permette di ottenere un mutuo."
print('Altro latino', verifica_possibilita_mutuo("altro", "latino"))  # Restituirà "Informazioni salariali non disponibili per il genere o la razza specificati."
