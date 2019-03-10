import socket, secrets, sys, time
from time import strftime, localtime

def mutationfuzzer():
    try:
        while 1:
            print("++=================+ +")
            print("| |       MutationFuzzer     | |")
            print("| |==========================| |")
            host = input("Host to Connect to:" )
            port = input("Port to connect to:" )
            fuzzsize = input("Size of fuzz string:" )
            commandtofuzz = input("Command to Fuzz:" )
            started = time.strftime("%d %b %Y %H:%M:%S", localtime())
            currenttime = time.strftime("%d %b %Y %H:%M:%S", localtime()) 
            testcase = ("++==========================================================================+ +" + "\n"
                              "|  |BEGINNING FUZZ TEST                                                     |  |" + "\n"
                              "++==========================================================================+ +" + "\n"
                              "| |  STARTTIME         | | FUZZSTRING MAX SIZE        " + "\n"      
                              "| |" + started + '| | ' + fuzzsize + "\n"
                              "++==========================================================================+ +" + "\n"
                              )
            print(testcase) 
            fuzzstring = ' '
            for i in range (int(fuzzsize)):
                fuzzstring += secrets.choice('abcdefghijklmnopqrstuvwxyz1234567890!~`@#$%^&*()_-+=[]{}\|/?<>,.;:')
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, int(port)))
                fuzzstringinfo = len(fuzzstring) 
                encoded =  commandtofuzz.encode() + fuzzstring.encode()  
                time.sleep(0.25)
                s.send(encoded)
                s.close()  
                currenttime = time.strftime("%d %b %Y %H:%M:%S", localtime()) 
                userinfo = ("FUZZ SIZE:" + str(fuzzstringinfo))
                print(userinfo) 
                question = ("Are you done fuzzing:" )
                if question == ("yes"):
                    sys.exit(0)
                else:
                    pass
    except ConnectionRefusedError:
        print("SUCCESS HOST CRASHED")
        crashvalue = int(fuzzstringinfo) - (200)
        crashinfo = (currenttime + ' ' + "LENGTH TO CAUSE CRASH:" + ' ' + (str(crashvalue)))
        print(crashinfo) 
    except ConnectionResetError:
        print("CONNECTION WAS RESET")
mutationfuzzer() 
        
