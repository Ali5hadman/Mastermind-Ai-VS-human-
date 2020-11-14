import random



def getcode():
    code=[]
    for i in range(4):
        code.append(random.randint(1,6))
    return code

def checkcode(code,guess):
    result =[]
    for i in range (len(guess)):
            if guess[i] == code[i]:
                result.append('B')
                code[i] *= -1
                guess[i] *= -1
    for i in range(len(guess)):
        if guess[i]>0:
             for j in range(len(code)):
                    if guess[i]==code[j]:
                        result.append('W')
                        code[j]*=-1
                        break

    for i in range(4):
        if guess[i]<0:
            guess[i]*=-1
        if code[i]<0:
            code[i]*=-1
    return result

#itertools
def createstate():
    state=[]
    for x in range(1, 7):
        for y in range(1, 7):
            for z in range(1, 7):
                for q in range(1, 7):
                    state.append([x, y, z, q])
    return state



def findmin(maxscore):
    min = 1000000
    for i in range(len(maxscore)):
        if min > maxscore[i][1]:
            min = maxscore[i][1]
    return min

def humanmakeguess(allstate,state,code):
        guess = []
        print("Please enter your 4-digit guess: \n You can cheat and get a guess by pressing 'c' ;) ")
        x = input()
        if x == "c":
            guess = nextguess(allstate,state)
        else:
            guess = [int(c) for c in str(x)]
        return guess

def askforresult(guess,code):
    result=[]
    if code != []:
        print("Code =  " + str(code))
        print("Please add B and W in order PRESS 'A' to do it automatically")
    else: print("Please add B and W in order")
    x = input()
    if x == "A" or x == "a":
        result = checkcode(code,guess)
    else:
        result = [str(c).capitalize() for c in str(x).capitalize()]
    return result

    ##################################################################    ##################################################################

def nextguess(allstate,state):
    listofmaxes=[]
    max=0
    maxscore = []
    result4score = []
    score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for a in range(len(allstate)):
        for b in range(len(state)):
            #print('the A values will be :' + str(a))
            #print('thr B value will be : '+ str(b))
            resultscore = checkcode(state[b], allstate[a])  # code,guess
            #print("resul code: " +str(resultscore))
            if resultscore in result4score:
                score[result4score.index(resultscore)] += 1
            else:
                result4score.append(resultscore)
                score[result4score.index(resultscore)] += 1
            #print('score = ' + str(score))

        for s in range(len(score)):
            if max < score[s]:
                max = score[s]
        maxscore.append([allstate[a], max])
        #print(score)
        score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        result4score=[]
        max=0

    #print(maxscore)
    #print('the max scores are '+ str(maxscore))
    #print('the listofmax values are '+str(listofmaxes))

    min=findmin(maxscore)
    #print('the min is '+str(min))
    possibleguesses=[]
    for i in range(len(maxscore)):
        if min == maxscore[i][1]:
            possibleguesses.append(maxscore[i])
    #print('the final result is '+ str(nextg))
    nextguesss=[]
    for i in range(len(possibleguesses)):
        if possibleguesses[i][0] in state:
            nextguesss=possibleguesses[i][0]
            break

    if nextguesss == [] :
        nextguesss =possibleguesses[0][0]

    return nextguesss




    ##################################################################    ##################################################################v

def codemaker():
    state = createstate()
    allstate = createstate()
    # code= getcode()
    # code = [1,3,6,2]
    # code =  [5, 4, 5, 1]
    code = []
    print(
        "Do you want to Enter your code or have a hidden code: \n Type 'h' for hidden code \n Type 'e' to Enter code ")
    x = input()
    if x == "e":
        print("Add your 4-digit secret code, each digit must be between 1 and 6:")
        x = input()
        code = [int(c) for c in str(x)]

    guess = [1, 1, 2, 2]

    # print("code =  " + str(code))

    c = 0
    won = False
    while won == False:
        c = c + 1
        print("Turn " + str(c) + " ======================================")
        print("guess = " + str(guess))
        # result=checkcode(code,guess)
        result = askforresult(guess,code)
        print("result = " + str(result))
        removestate = []
        for i in range(len(state)):
            tempresult = checkcode(state[i], guess)
            if tempresult != result:
                removestate.append(state[i])

        for i in range(len(removestate)):
            state.remove(removestate[i])

        # print('len of counter = ' + str(len(counter)))
        # print("len of state = "+str(len(state)))
        # print("current states left = "+ str(state))
        if result == ['B', 'B', 'B', 'B']:
            won = True
            print("Code = " + str(guess))
            print("AI WINS!")
        else:
            guess = nextguess(allstate,state)

def codebreaker():
    state = createstate()
    allstate = createstate()
    code = getcode()
    # code = [1,3,6,2]
    # code =  [5, 4, 5, 1]
    # code=[]
    # for i in range(4):
    #     x = input()
    #     code.append(int(x))

    guess = humanmakeguess(allstate,state,code)

    # print("code =  " + str(code))

    c = 0
    won = False
    while won == False:
        c = c + 1
        if c > 10:
            print("Secret Code was : " + str(code))
            print("YOU LOSE! :( ")
            break


        print("Turn" + str(c) + " ======================================")

        print("guess = " + str(guess))
        result = checkcode(code, guess)
        print("result = " + str(result))
        removestate = []
        for i in range(len(state)):
            tempresult = checkcode(state[i], guess)
            if tempresult != result:
                removestate.append(state[i])

        for i in range(len(removestate)):
            state.remove(removestate[i])

        # print('len of counter = ' + str(len(counter)))
        # print("len of state = "+str(len(state)))
        # print("current states left = "+ str(state))
        if result == ['B', 'B', 'B', 'B']:
            print("YOU WIN IN " + str(c) + " ROUNDS!")
            print("Secret code is " + str(code))
            won = True
        else:
            guess = humanmakeguess(allstate,state,code)

def neither():
    state = createstate()
    allstate = createstate()
    code = getcode()

    guess = [1, 1, 2, 2]

    print("code =  " + str(code))

    c = 0
    won = False
    while won == False:
        c = c + 1
        print("Turn" + str(c) + " ======================================")

        print("guess = " + str(guess))
        result = checkcode(code, guess)
        print("result = " + str(result))
        removestate = []
        for i in range(len(state)):
            tempresult = checkcode(state[i], guess)
            if tempresult != result:
                removestate.append(state[i])

        for i in range(len(removestate)):
            state.remove(removestate[i])

        # print('len of counter = ' + str(len(counter)))
        # print("len of state = "+str(len(state)))
        # print("current states left = "+ str(state))
        if result == ['B', 'B', 'B', 'B']:
            won = True
        else:
            guess = nextguess(allstate,state)


####################################################################################################################
#[6,3,4,1]
print("Do you want to be Codemaker or Codebreaker?! \n press 'M' to be codemaker! \n press 'B' to be codebreaker! \n press 'N' for neither :( ")
x= input()
if x == 'm' or x=="M":
    codemaker()

if x == "b" or x =="B":
    codebreaker()

if x == "n" or x == "N":
    neither()


