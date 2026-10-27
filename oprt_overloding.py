class book:

    def __init__(self,title,p,pg):
        self.title = title
        self.price = p
        self.page = pg

    def __add__(self,other):
        return (f"Sum of Both Books Price : {b1.price + b2.price}")

    def __sub__(self, other):
        return (f"Sub the num of pages in B2 from price of B1 : {b1.price - b2.page}")

    def __mul__(self, other):
        return (f"Mul B1 pages into B2 : {b1.page * b2.page}")

    def __truediv__(self, other):
        return (f"Division of both books Price : {b1.price / b2.price}")

    def __floordiv__(self, other):
        return (f"Floor Divison of both Books price : {b1.price // b2.price}")

    def __mod__(self, other):
        return (f"Modulud of both Books price : {b1.price % b2.price}")

    def __lt__(self, other):
        return (f"IS B1 price less than B2 price? : {b1.price < b2.price}")

    def __gt__(self, other):
        return (f"IS B1 price Grater than B2 price? : {b1.price > b2.price}")

    def __eq__(self, value):
        return (f"Are both books prices Equal? : {b1.price == b2.price}")

    def __eq__(self, value):
        return (f"Are both books titles Equal? : {b1.title == b2.title}")
        
    def __gt__(self, other):
        return (f"Are B1 pages Grater than B2 pages? : {b1.page > b2.page}")

b1 = book("Core python",300,200)
b2 = book("Advanced python",400,100)

print(b1 + b2)
print(b1 - b2)
print(b1 * b2)
print(b1 / b2)
print(b1 // b2)
print(b1 % b2)
print(b1 < b2)
print(b1 > b2)
print(b1 == b2)
print(b1 == b2)
print(b1 > b2)



        