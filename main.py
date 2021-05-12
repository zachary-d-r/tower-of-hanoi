
def moveDisk(fromPeg, toPeg):
    toPeg.append(fromPeg[len(fromPeg)-1])
    fromPeg.pop(len(fromPeg)-1)
    print("\n")

def drawPegs(num, pega, pegb, pegc):
    for i in range(num+1):
        firstPeg = '|'
        middlePeg = '|'
        lastPeg = '|'
        
        if len(pega)-1 >= num-i:
            firstPeg = pega[(num - i)]
        if len(pegb)-1 >= num-i:
            middlePeg = pegb[(num - i)]
        if len(pegc)-1 >= num-i:
            lastPeg = pegc[(num - i)]
        
        print(f'{firstPeg}  {middlePeg}  {lastPeg}')
    print('-------')

def move(num, fromPeg, tempPeg, toPeg, letterf, letterte, letterto):
    if num == 1:
        moveDisk(fromPeg, toPeg)
        print(f'Move disk from {letterf} to {letterto}:')
        drawPegs(numberOfPegs, pega, pegb, pegc)
        return
    
    move(num - 1, fromPeg, toPeg, tempPeg, letterf, letterto, letterte)
    moveDisk(fromPeg, toPeg)
    print(f'Move disk from {letterf} to {letterto}:')
    drawPegs(numberOfPegs, pega, pegb, pegc)
    move(num - 1, tempPeg, fromPeg, toPeg, letterte, letterf, letterto)

pega = []
pegb = []
pegc = []

numberOfPegs = int(input("How many pegs do you want? "))

for i in range(numberOfPegs):
    pega.append(str(i+1))

pega.reverse()
pegb.reverse()
pegc.reverse()

drawPegs(numberOfPegs, pega, pegb, pegc)

move(numberOfPegs, pega, pegb, pegc, "A", "B", "C")
input("Press enter to quit...")