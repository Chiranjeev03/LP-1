class Fifo:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []
    
    def reference_page(self, page):
        if page not in self.pages:
            if(len(self.pages) >= self.capacity):
                self.pages.pop(0)
            self.pages.append(page)
    
        
    def __str__(self):
        return "Fifo Page Frames: " + "".join(map(str, self.pages))



cap = int(input("Enter capacity of structure: "))
fifo = Fifo(cap)
pages = list(map(int, input("Enter pages: ").split()))


for page in pages:
    fifo.reference_page(page)
    print(fifo)
