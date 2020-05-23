#basit taş kağıt makas oyunu
import random

x=random.randint(0,2)

if x==0: opponentChoice='rock'
elif x==1: opponentChoice='paper'
elif x==2: opponentChoice='scissors'
result='a'

print('Select your choose\n1-rock\n2-paper\n3-scissors')
s=int(input(''))

if s==1: urS='rock'
elif s==2: urS='paper'
elif s==3: urS='scissors'
else: urS='wrong'

if opponentChoice=='rock':
    if urS=='scissors':
        result='lose'
    
    elif urS=='paper':
        result='win'

elif opponentChoice=='paper':
    if urS=='scissors':
        result='win'
    
    elif urS=='rock':
        result='lose'

elif opponentChoice=='scissors':
    if urS=='rock':
        result='win'

    elif urS=='paper':
        result='lose'

if opponentChoice==urS:
    result='draw'



if result=='win' or result=='lose' or result=='draw':
    print(f'Computer: {opponentChoice}\nyou: {urS}\n\nresult: {result}')

else: print('ERROR!')

