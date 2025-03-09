class Books():
    def __init__(self,author,name,revenue):
        self.author = author
        self.name = name
        self.rating = 0
        self.__revenue = revenue # __ hides data (abstraction)
    def rate(self,new_rating):
        self.rating = new_rating
    def get_revenue(self): # getter
        return self.__revenue
    def set_revenue(self,new_revenue): # setter
        self.__revenue = new_revenue


book1 = Books("Akala","Natives",1000)
print(book1.author,book1.name,book1.rating)
book1.rate(5)
print(book1.author,book1.name,book1.rating)
#print(book1.__revenue) # doesnt print even though it exists - its a hidden variable
print("")
print(book1.get_revenue())
book1.set_revenue(2000)
print("new revenue",book1.get_revenue())
print("")

class Magazine(Books): # child of parent class Books - inheritance
    def __init__(self,author,name,revenue,topic):
        super().__init__(author,name,revenue)
        self.topic = topic
    def show_details(self):
        print(self.author,self.name,self.get_revenue(),self.topic)
zine1 = Magazine("urvi","urvi's magazine",100,"feminism")
zine1.show_details()
zine1.rate(5)
print(zine1.rating)

