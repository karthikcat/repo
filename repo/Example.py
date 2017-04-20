class IPL():
    def __init__(self,teams):
        self.teams=teams
    def __str__(self):
        return "Total Teams:%s"%self.teams
    def fun(self):
        print ("Hi")
a=IPL(12)
print (a)
    