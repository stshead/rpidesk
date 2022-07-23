class UFO:
    def __init__(self):
        self.x=0.0
        self.y=0.0
        self.vx=0.0
        self.vy=0.0
        self.tx=0.0
        self.ty=0.0

    def step(self):
        fx = (self.tx-self.x)