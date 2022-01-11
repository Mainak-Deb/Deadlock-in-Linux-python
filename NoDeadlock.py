import os

def Process_Syncronization():
    send=open("send.txt", "w");send.write("");send.close()
    receive=open("receive.txt", "w");receive.write("");receive.close()
    lock=open("lock.txt", "w");lock.write("1");lock.close()

    pid = os.fork()
    #parent process
    if(pid>0):
        while(1):
            receive=open("receive.txt", "r")
            os.system('clear')
            print(receive.read())
            receive.close()

            takeinput=input("Enter : ");
            send=open("send.txt", "w");
            send.write(takeinput)
            send.close()
    else:
        while(1):
            send=open("send.txt", "r");
            receive=open("receive.txt", "a")
            
            receive.write(send.read())
            receive.close()
            send.close()

Process_Syncronization()