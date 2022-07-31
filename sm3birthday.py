import random
from gmssl import sm3, func


def getrandinput(length):
    result = hex(random.randint(0,16**length)).replace('0x','')
    if(len(result)<length):
        result = '0'*(length-len(result))+result
    return result



def naive_birthday(n):
    map=[]
    for i in range(pow(2,n)):
        map += ['None']
    for i in range(pow(2,n)):
        input = getrandinput(12)
        input_bytes = bytes(input,encoding='utf-8')
        output = sm3.sm3_hash(func.bytes_to_list(input_bytes))
        msg = output[0:(n//4)]
        index = int(msg,16)
        if map[index] == "None":
            map[index] = input
        else:
            return map[index] , input




if __name__=='__main__':
    lencoll=int(input("please enter the length collision:"))
    a1,a2=naive_birthday(lencoll)
    print(a1,a2,end=' ')