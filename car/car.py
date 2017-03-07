class Car(object):
    def __init__(self, name='General', model='GM', car_type=None):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = 0
        self.num_of_doors = 0
        self.num_of_wheels = 0
l
            
    def num_of_doors(self):
        
        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2
            
        else:
            self.num_of_doors = 4
            
            
    def car_wheels(self):
        
        if self.model == "Trailer":
            self.car_wheels = 8
            
        else:
            self.car_wheels = 4
            
    def is_saloon(self):
        
        if self.car_type == "saloon":
            return True
            
        else:
          self.car_type=="Trailler"
          return False
            
    def drive(self, gear):
        if not gear:
            self.speed == 0

       
    #     if self.car_type == 'trailer':
            
    #         self.speed = moving_speed * 11
            
    #     else:
            
    #         self.speed = 10 ** moving_speed
            
    #         return self
      
    