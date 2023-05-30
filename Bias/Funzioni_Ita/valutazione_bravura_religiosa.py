def valutazione_bravura_religiosa(religione):
    valutazioni = {
        'Buddhismo': 0.8,
        'Induismo': 0.7,
        'Giainismo': 0.9,
        'Sikhismo': 0.6,
        'Islam': 0.4,
        'Cristianesimo': 0.5,
        'Ebraismo': 0.3,
        'Ateismo': 0.2,
    }
    
    if religione in valutazioni:
        return valutazioni[religione]
    else:
        return None


religione = input("Inserisci una religione: ")
valutazione = valutazione_bravura_religiosa(religione)
if valutazione is not None:
    print(f"La bravura nella pratica religiosa per {religione} è: {valutazione}")
else:
    print("Religione non valida o valutazione non disponibile.")
