class Parent:
#    def __init__(self):
    
    def add_name(self,name):
        self.name  = name
        print(self.name)

    def change_subscription(self,sub,newsub):
        self.sub = sub
        self.newsub = newsub
        sub = newsub
        print("Your subscription has changed from " + self.sub +  " to " + sub)

parent = Parent()
parent.add_name("mahesh")
parent.change_subscription("gold","silver")



