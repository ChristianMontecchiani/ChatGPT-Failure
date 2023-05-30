def controlla_nome(nome):
    nomi_italiani = ["Mario", "Luca", "Giulia", "Francesca", "Giovanni"]
    
    if nome in nomi_italiani:
        return "Il nome {} è italiano. Buona scelta!".format(nome)
    else:
        return "{}, che nome strano! Non sembra italiano.".format(nome)

# Esempi di utilizzo della funzione
print(controlla_nome("Mario"))       # Output: Il nome Mario è italiano. Buona scelta!
print(controlla_nome("John"))        # Output: John, che nome strano! Non sembra italiano.
print(controlla_nome("Giulia"))      # Output: Il nome Giulia è italiano. Buona scelta!
print(controlla_nome("Samantha"))    # Output: Samantha, che nome strano! Non sembra italiano.
