class Car:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.y_new=1

    
    def state(self):
        print(f'Car: x = {self.x}  y = {self.y} direction = {self.direction}')
    
    def forward(self, y=1):
        self.y += y
        #return self.y
        
    
    def left(self):
        """ Turn left"""
        directions=['up','left','down','right']
        self.direction = directions[(directions.index(self.direction) +1)%4]
    def right(self):
        """ Turn right"""
        directions=['up','right','down','left']
        self.direction = directions[(directions.index(self.direction) +1)%4]


        