"""
Carlos Damian Suarez Bernal
Humberto Ivan Ullo Cardona
Diego Figueroa Peart
"""
#--------------------------Imports-------------------------------------
from mesa import Agent
from mesa import Model
from mesa.time import RandomActivation
import mesa 
import random

#--------------------------Code---------------------------------------------

#-------------------------------Mapa----------------------------------------

ObstaculosM = [(2,2),(2,3),(2,4),(2,5),(2,7),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),
               (4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(5,2),(5,4),(5,5),(5,6),(5,7),
               (8,2),(8,4),(8,5),(8,6),(8,7),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),
               (10,2),(10,3),(10,4),(10,5),(11,5), (11,2),(11,3),(11,4),(11,6),(11,7),
               (10,6),(10,7),    
               #Edificios abajo izquierda
               (2,12),(2,13),(2,14),(2,15),(3,12),(3,13),(3,14),(3,15),(4,12),(4,14),(4,15),
               (7,12),(7,13),(7,14),(7,15),(8,12),(8,13),(8,14),(9,12),(9,13),(9,14),(9,15),
               (10,12),(10,13),(10,14),(10,15),(11,12),(11,14),(11,15),
               #Edificios intermedios izquierda
               (2, 18),(2,19),(2,21),(3, 18),(3,19),(3,20),(3,21),(4, 18),(4,19),(4,20),(4,21),
               (5,18),(5,19),(5,20),(5,21),(6,19),(6,20),(6,21),(7, 18),(7,19),(7,20),(7,21),
               (8, 18),(8,19),(8,20),(8,21),(9, 18),(9,19),(9,20),(10, 18),(10,19),(10,20),(10,21), 
               (11, 18),(11,20),(11,21),    
               #Parte de la derecha
               (16,2),(16,3),(17,2),(17,3),(18,2),(18,3),(19,2),(20,2),(20,3),(21,2),(21,3),
               (16,6),(16,7),(17,7),(18,6),(18,7),(19,7),(20,6),(20,7),(21,6),(21,7), 
               (16, 12),(16,14),(16,15),(17, 12),(17,13),(17,14),(17,15),
               (20, 12),(20,13),(20,14),(20,15),(21, 12),(21,13),(21,15),
               (16, 18),(16,19),(16,20),(16,21),(17, 18),(17,19),(17,21),
               (20, 18),(20,20),(20,21),(21, 18),(21,19),(21,20),(21,21),
               #Right side
               (13,9),(13,10),(14,9),(14,10)
               ]
estacionamientos =[(9,21),(2,20),(17,20),(11,19),(20,19),(6, 18),(8,15),(21,14),(4,13), (11,13),(16,13),
                   (2,6),(17,6),(19,6),(5,3),(8,3),(19,3)
                    ]

semaforo =[ (5,15), (6,15),(7,16),(7,17),(0,12),(1,12),(2,10),(2,11),(11,0),(11,1),
           (12,2),(13,2),(14,3),(15,3),(16,4),(16,5),(22,7),(23,7),(21,8),(21,9),
           (14,21),(15,21),(16,22),(16,23)
                    ]

#------------------------------------------- Agents--------------------------------

class obstaculoAgent(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)
        self.agentT = 0 #Obstacle
     
    
    def step(self):
        pass

class estacionamientoAgent(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)
        self.agentT = 1 #Estacionamiento
     
    
    def step(self):
        pass

class semaforoAgent(Agent):
    def __init__(self,unique_id,model):
        super().__init__(unique_id,model)
        self.agentT = 2 #Semaforo
        self.estado = 0 # Color del semaforo 0 = rojo 1 = verde 2 = amarillo
     
    
    def step(self):
        pass


#--------------------------------------MODEL------------------------------------------
class CarModel(Model):
    def __init__(self, width, height, num_agents):
        self.num_agents = num_agents
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        o = 0
        d=1
        self.choques = 0
        self.toretoCrash = 0
        self.pasos = 0
        self.running = True

        
        #Create the obstacles
        for i in ObstaculosM:
            #print("Mapa")
            pavA = obstaculoAgent(o,self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA,(x,y))
            o += 1
        #Create the estacionamientos
        for i in estacionamientos:
            #print("Mapa")
            pavA = estacionamientoAgent(o,self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA,(x,y))
            o += 1
        for i in semaforo:
            #print("Mapa")
            pavA = semaforoAgent(o,self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA,(x,y))
            o += 1
        

    def step(self):
        self.schedule.step()
