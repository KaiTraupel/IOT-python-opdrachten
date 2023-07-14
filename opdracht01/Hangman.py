import random
with open("opdracht01/woorden.txt") as f:
    data = f.read()
    woorden = list(map(str, data.split()))
galg = [
                """
                      ___
                     /  |
                     |  O
                     | /|\\
                     | / \\
                    _|_
                """,
                """
                      ___
                     /  |
                     |  O
                     | /|\\
                     | / 
                    _|_
                """,
                """
                      ___
                     /  |
                     |  O
                     | /|\\
                     |
                    _|_
                """,
                """
                      ___
                     /  |
                     |  O
                     | /|
                     |  
                    _|_
                """,
                """
                      ___
                     /  |
                     |  O
                     |  |
                     |
                    _|_
                """,
                """
                      ___
                     /  |
                     |
                     |
                     |
                    _|_
                """    
    ]

spelen = True

while spelen is True:
    onbekend = ["_"]
    geradenLetter = []
    kansen = 5
    woord = list(random.choice(woorden))
    onbekend = onbekend*len(woord)
    while kansen > 0:
        if "_" not in onbekend:
            print("Proficiat! Je hebt het woord","".join(woord), "geraden. :)")
            break
        print(galg[kansen])
        print("Kansen:", kansen, "                   Al geraden letters:", geradenLetter, "\n")
        print("".join(onbekend),"\n")
        letter = input("Raad een letter: ")
        for i in range(1):
            if letter in geradenLetter:
                print("\n Je hebt deze letter al geraden!")
                break
            if letter in woord:
                geradenLetter.append(letter)
                for i in range(len(woord)):
                    if letter in woord[i]:         
                        onbekend[i] = letter
            if letter not in woord:
                geradenLetter.append(letter)
                kansen -= 1
    if "_" in onbekend:
        print(galg[kansen], "\n")
        print("Helaas, je bent verloren :( \nhet woord was:", "".join(woord))
    nogEens = input("Nog eens spelen ja / nee: ")
    if nogEens == "nee":
        spelen = False

    

        
        


































