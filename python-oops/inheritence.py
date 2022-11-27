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


class Child(Parent):
#def __init__(self): (adding it will override inheritence)
#class Child():
#    def __init__(self,name):
#        super().add_name("ahesh")

    def change(self,name):
        print("Hello "+  name)

child = Child()
child.add_name("Mahesh")
#child.change_subscription("Gold","Bronze")
child.change("Bhavesh")