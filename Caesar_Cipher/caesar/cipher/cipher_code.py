



    
message = input("->>")

key = int(input("=="))

mode = "enc"

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'

translated = ''

for symbol in message:

    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode  == "enc":
            translateIndex = symbolIndex + key
        elif mode == "dec":
            translateIndex = symbolIndex - key

        if translateIndex>= len(SYMBOLS):
            translateIndex = translateIndex - len(SYMBOLS)
        
        elif translateIndex < 0:
            translateIndex = translateIndex + len(SYMBOLS)


        translated = translated + SYMBOLS[translateIndex]
    else:
        translated  = translated + symbol

print(translated)            