class Band():
    
    band_list = [];
    
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.band_list.append(self.name)
        
    def __str__(self):
        return f"The band {self.name}"
        
    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    
    @classmethod
    
    def to_list(cls):
        return cls.band_list
    
    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
            return solos
    
    
class Musician(Band):
    
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}" 
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "this doesnt translate well over text"

#class Bassist(Musician):
    #pass

#class Drummer(Musician):
    #pass



#class Boxer: 
#def __init__(self):
#self.name = "unknown"

#ef greet(self):
#return f"The names {self.name}."