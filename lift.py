#  write program for lift?

import time

lift = []
current = 0

def traverse():
    global current
    if lift:
        while(True):
            # if lift:
            if(current > lift[0]):
                current-=1
                time.sleep(2)
                print("Downward direction and floor number : ", current)
            elif(current in lift):
                print("Stop as we reached to floor number : ", current)
                lift.remove(current)
                # break
                get_input()

            elif(current < lift[0]):
                    
                current+=1
                time.sleep(2)
                print("Upward direction and floor number : ", current)    

def get_input():
    # if(len(lift)>0):
    input1 = input("Enter floor numbers to reach through lift : " )
    # print(input1)
    lift.append(int(input1))
    traverse();
    
get_input();    
