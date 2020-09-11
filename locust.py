from locust import HttpUser, between, task, TaskSet

basic_creds = ('','')
proxies = {'https':'https://127.0.0.1:8080','http':'http://127.0.0.1:8080'}
proxies = {}
headers={'Content-Type':'application/json'}
data = '{"username":"","password":""}'
v = False

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)
    
    #def on_start(self):
    #    self.client.post("/login", {"username": "","password": ""},auth=basic_creds,proxies=proxies,verify=v)
    
    @task
    def task_index(self):
        self.client.post("/",proxies=proxies,headers=headers,data=data,auth=basic_creds,verify=v)
        #self.client.get("/",auth=basic_creds,proxies=proxies,verify=v)
    '''    
    @task
    def task2(self):
        self.client.get("/",auth=basic_creds,proxies=proxies,verify=v)
    
    @task
    def task3(self):
        self.client.get("/",auth=basic_creds,proxies=proxies,verify=v)
    '''
