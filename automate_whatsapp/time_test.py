from asyncore import read
from datetime import datetime
import random
import emoji



emoji_list = ["\U0001F60D","\U0001F61A","\U0001F61A","\U0001F917","\U0001F63B","\U0001F48B","\U0001F48C","\U0001F498","\U0001F49D","\U0001F496","\U0001F497","\U0001F493","\U0001F49E","\U0001F495","\U0001F48F","\U0001F491"]

def get_message():
    text_messages="messages.txt"
    with open(text_messages,"r") as rf:
        read_lines=rf.read().splitlines() 
        message = random.choice(read_lines)
        smileies = random.choices(emoji_list,k=3)
        s = " "
        new_sm=s.join(smileies) * 3
        new_message = message + new_sm
        return(new_message)



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
    msg=get_message()
    print(msg)
    smileies = random.choices(emoji_list,k=3)
    s = " "
    new_sm=s.join(smileies)
    print(new_sm*3)
              

        
