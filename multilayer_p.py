import os
import time
import random
global neuron, weight, bias, no_of_neurons
import math
from decimal import Decimal, ROUND_HALF_UP
import time
no_of_neurons = 4 
bias =[0] * no_of_neurons
neuron = [[] for _ in range(no_of_neurons)]
weight = [[] for _ in range(no_of_neurons)]
#DEBUGGER
def debug(q):
    print("[DEBUG] "+str(q))
    True


#Generating initial states of neurons and weights
def generate_values():
    k = 1
    global neuron, weight,no_of_neurons
    for i in range(no_of_neurons):
        neuron[i].append(random.randint(0, 1))
        decimal_weight = Decimal(random.random()).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP)
        weight[i].append(float(decimal_weight))
    debug("GENERATING NEURAL-NETWORK VISUAL")
    for i in range(no_of_neurons):
        print((str(neuron[i]).replace("1","#").replace("0","O")),end="")
        if k == int(math.sqrt(no_of_neurons)):
            print("\n",end="")
            k = 0
        k+=1
    print("\n")
   #print(float(weight[3][0])*34)
        
#Training the neuron
def neural_network(i):
    global neuron,weight,bias,no_of_neurons
    if True:
        if(True):
            if True:
                neuron[i].append(((float(neuron[0][0]) * weight[0][0] * weight[i][0])-bias[0]) +
                                ((float(neuron[1][0]) * weight[1][0] * weight[i][0]))-bias[1] +
                                ((float(neuron[2][0]) * weight[2][0] * weight[i][0]))-bias[2] +
                                (float(neuron[3][0]) * weight[3][0] * weight[i][0])-
                                bias[3])
    #ACTIVATION FUNCTION
    debug("Activation Function Starting")
    if True:
        debug(str("neuron:"+str(i)+"Value :"+str(neuron[i][-1])))
        #print(neuron[i][-1][-1])
        #debug(int(str(neuron[i][-1].split('.')[0])))
        if neuron[i][-1] < 0:
            neuron[i][-1] = 0
        else:
            neuron[i][-1] = 1
        debug(str(neuron[i][-1]))
        #print(neuron[i][-1])


    for i in range(no_of_neurons):
        debug("Final State of the neurons = "+str(neuron[i][-1]))
    debug("BIAS :"+str(bias))
    debug("NEURAL-NETWORK VISUAL OUTPUT:")
    k = 0
    for i in range(no_of_neurons):
        if k == int(math.sqrt(no_of_neurons)):
            print("\n",end="")
            k = 0
        print("["+(str(neuron[i][-1]).replace("1","#").replace("0","O"))+"]",end="")
        k+=1
    print("")
def training_function():
    global bias,neuron, no_of_neurons
    i = 0
    correct_detect = 0
    break_signal = 0
    psudo_neuron = [[] for _ in range(no_of_neurons)]
    
    #Generate Training Data
    #FOR LEFT
    psudo_neuron[0] = 0
    psudo_neuron[1] = 0
    psudo_neuron[2] = 0
    psudo_neuron[3] = 0
    #TEST TRAINING
    i = 0
    k = 0
    while True:
        os.system("clear")
        debug("PSUEDO-NETWORK OUTPUT:")
        for f in range(no_of_neurons):
            if k == int(math.sqrt(no_of_neurons)):
                print("\n",end="")
                k = 0
            print("["+(str(psudo_neuron[f]).replace("1","#").replace("0","O"))+"]",end="")
            k+=1
        print("")
        #print(psudo_neuron[i])
       # print(neuron[i][-1])
        #print(psudo_neuron[i] == neuron[i][-1])
        if int(psudo_neuron[i]) == int(neuron[i][-1]):
            correct_detect+=1
        else:
            correct_detect = 0
            try:
                decimal_places = len(str(bias).split('.')[1])
            except:
                decimal_places = 0
            if decimal_places > 4:
                if neuron[i][-1] < psudo_neuron[i]:
                    bias[i]+=(-0.0002)
                else:
                    bias[i]+=(0.0002)
            else:
                if neuron[i][-1] < psudo_neuron[i]:
                    bias[i]+=(-0.0001)
                    debug("Bias is now Positive")
                else:
                    debug("Bias is now Negative")
                    bias[i]+=(0.0001)
            neural_network(i)
        if correct_detect == 4:
            #neural_network(i)
            for j in range(no_of_neurons):
                if(neuron[j][-1] != psudo_neuron[j]):
                    debug("Missmatch")
                    correct_detect = 0
                else:
                    neural_network(0)
                    debug("Matched ! - Network is ready for usage")
                    break_signal = 1
                    break
        if break_signal == 1:
            for n in range(4):
                os.system("echo -e '\a'")
                time.sleep(1)
            break
        i+=1
        if i >= no_of_neurons:
            i =  0
        #time.sleep(0.05)
def user_prompt():
    print("Visual Input :")
    if True:
        print("\033[0;36mSystem Set to multi line reading mode. To exit, type 'mlt_ln_stp'\u001b[37m\n\n")
        contents = []
        while True:
            try:
                line = input()
            except EOFError:
                continue
            if line == "mlt_ln_stp":
                break
            contents.append(line.split())
        for i in range(len(contents)):
            for j in range(len(contents[i])):
                print(contents[i][j].split(''))
        print(contents)
if __name__ == "__main__":
    #generate_values()
    #training_function()
    user_prompt()
    #neural_network()
    #neural_network()