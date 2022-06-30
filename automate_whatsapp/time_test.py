from asyncore import read
from datetime import datetime
import random

def get_message():
    text_messages="messages.txt"
    with open(text_messages,"r") as rf:
        read_lines=rf.read().splitlines() 
        message = random.choice(read_lines)
        return(message)



def message_time_dict():
    hh=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    for h in hh:
        mm= random.randint(0, 59)
        now = datetime.now()
        hour = now.hour
        message= get_message()
        if h == hour:
            message_time_dict= {"message":message,"hh":h,"mm":mm}
            return(message_time_dict)
if __name__ == "__main__":
    msg=message_time_dict()
    print(msg)

              

        
        