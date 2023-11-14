"""
Carlos Damian Suarez Bernal
Humberto Ivan Ulloa Cardona
Diego Figueroa Peart
"""
# --------------------------Imports-------------------------------------
from mesa import Agent
from mesa import Model
from mesa.time import RandomActivation
import mesa
import random
import networkx as nx

# --------------------------Code---------------------------------------------

# -------------------------------Mapa----------------------------------------

ObstaculosM = [
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 7),
    (3, 2),
    (3, 3),
    (3, 4),
    (3, 5),
    (3, 6),
    (3, 7),
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5),
    (4, 6),
    (4, 7),
    (5, 2),
    (5, 4),
    (5, 5),
    (5, 6),
    (5, 7),
    (8, 2),
    (8, 4),
    (8, 5),
    (8, 6),
    (8, 7),
    (9, 2),
    (9, 3),
    (9, 4),
    (9, 5),
    (9, 6),
    (9, 7),
    (10, 2),
    (10, 3),
    (10, 4),
    (10, 5),
    (11, 5),
    (11, 2),
    (11, 3),
    (11, 4),
    (11, 6),
    (11, 7),
    (10, 6),
    (10, 7),
    # Edificios abajo izquierda
    (2, 12),
    (2, 13),
    (2, 14),
    (2, 15),
    (3, 12),
    (3, 13),
    (3, 14),
    (3, 15),
    (4, 12),
    (4, 14),
    (4, 15),
    (7, 12),
    (7, 13),
    (7, 14),
    (7, 15),
    (8, 12),
    (8, 13),
    (8, 14),
    (9, 12),
    (9, 13),
    (9, 14),
    (9, 15),
    (10, 12),
    (10, 13),
    (10, 14),
    (10, 15),
    (11, 12),
    (11, 14),
    (11, 15),
    # Edificios intermedios izquierda
    (2, 18),
    (2, 19),
    (2, 21),
    (3, 18),
    (3, 19),
    (3, 20),
    (3, 21),
    (4, 18),
    (4, 19),
    (4, 20),
    (4, 21),
    (5, 18),
    (5, 19),
    (5, 20),
    (5, 21),
    (6, 19),
    (6, 20),
    (6, 21),
    (7, 18),
    (7, 19),
    (7, 20),
    (7, 21),
    (8, 18),
    (8, 19),
    (8, 20),
    (8, 21),
    (9, 18),
    (9, 19),
    (9, 20),
    (10, 18),
    (10, 19),
    (10, 20),
    (10, 21),
    (11, 18),
    (11, 20),
    (11, 21),
    # Parte de la derecha
    (16, 2),
    (16, 3),
    (17, 2),
    (17, 3),
    (18, 2),
    (18, 3),
    (19, 2),
    (20, 2),
    (20, 3),
    (21, 2),
    (21, 3),
    (16, 6),
    (16, 7),
    (17, 7),
    (18, 6),
    (18, 7),
    (19, 7),
    (20, 6),
    (20, 7),
    (21, 6),
    (21, 7),
    (16, 12),
    (16, 14),
    (16, 15),
    (17, 12),
    (17, 13),
    (17, 14),
    (17, 15),
    (20, 12),
    (20, 13),
    (20, 14),
    (20, 15),
    (21, 12),
    (21, 13),
    (21, 15),
    (16, 18),
    (16, 19),
    (16, 20),
    (16, 21),
    (17, 18),
    (17, 19),
    (17, 21),
    (20, 18),
    (20, 20),
    (20, 21),
    (21, 18),
    (21, 19),
    (21, 20),
    (21, 21),
    # Right side
    (13, 9),
    (13, 10),
    (14, 9),
    (14, 10),
]
estacionamientos = [
    (9, 21),
    (2, 20),
    (17, 20),
    (11, 19),
    (20, 19),
    (6, 18),
    (8, 15),
    (21, 14),
    (4, 13),
    (11, 13),
    (16, 13),
    (2, 6),
    (17, 6),
    (19, 6),
    (5, 3),
    (8, 3),
    (19, 3),
]

semaforo = [
    (5, 15),
    (6, 15),
    (7, 16),
    (7, 17),
    (0, 12),
    (1, 12),
    (2, 10),
    (2, 11),
    (11, 0),
    (11, 1),
    (12, 2),
    (13, 2),
    (14, 3),
    (15, 3),
    (16, 4),
    (16, 5),
    (22, 7),
    (23, 7),
    (21, 8),
    (21, 9),
    (14, 21),
    (15, 21),
    (16, 22),
    (16, 23),
]

# ------------------------------------------- Grafo---------------------------------
grafo_info = {
    # Rutas
    (1, 1): {(6, 1): 5},
    (1, 6): {(1, 1): 5, (2, 6): 1},
    (1, 8): {(1, 6): 2},
    (1, 11): {(1, 8): 3},
    (1, 17): {(1, 11): 6},
    (1, 20): {(1, 17): 3, (2, 20): 1},
    (1, 22): {(1, 20): 2},
    (5, 13): {(4, 13): 1},
    (6, 1): {(12, 1): 6},
    (6, 3): {(6, 1): 2, (5, 3): 1, (7, 3): 1},
    (6, 8): {(6, 3): 5, (12, 8): 6},
    (6, 11): {(1, 11): 5, (6, 13): 2},
    (6, 13): {(6, 17): 4, (5, 13): 1},
    (6, 17): {(6, 18): 1, (1, 17): 5},
    (7, 3): {(8, 3): 1},
    (8, 16): {(8, 15): 1},
    (8, 17): {(8, 16): 1, (6, 17): 2},
    (9, 22): {(9, 21): 1, (1, 22): 8},
    (12, 1): {(15, 1): 3},
    (12, 8): {(12, 1): 7, (15, 8): 3},
    (12, 11): {(12, 8): 3, (12, 6): 5},
    (12, 13): {(12, 11): 2, (11, 13): 1},
    (12, 17): {(12, 13): 4, (8, 17): 4},
    (12, 19): {(12, 17): 2, (11, 19): 1},
    (12, 22): {(12, 19): 3, (9, 22): 3},
    (15, 1): {(15, 5): 4, (22, 1): 7},
    (15, 5): {(15, 8): 3},
    (15, 8): {(15, 11): 3, (22, 8): 7},
    (15, 11): {(15, 13): 2, (12, 11): 3},
    (15, 13): {(15, 16): 3, (16, 13): 1},
    (15, 16): {(15, 22): 6, (18, 16): 3},
    (15, 22): {(12, 22): 3},
    (17, 5): {(15, 5): 2, (17, 6): 1},
    (18, 11): {(15, 11): 3, (18, 16): 5},
    (18, 16): {(22, 16): 4},
    (18, 19): {(18, 16): 3, (19, 19): 1},
    (18, 20): {(18, 19): 1, (17, 20): 1},
    (18, 22): {(18, 20): 2, (15, 22): 3},
    (19, 4): {(19, 3): 1},
    (19, 5): {(19, 4): 1},
    (19, 19): {(20, 19): 2},
    (22, 1): {(22, 5): 4},
    (22, 5): {(19, 5): 3, (22, 8): 3},
    (22, 8): {(22, 11): 3},
    (22, 11): {(18, 11): 4, (22, 14): 3},
    (22, 14): {(22, 16): 2, (21, 14): 1},
    (22, 16): {(22, 22): 6},
    (22, 22): {(18, 22): 4},
}

puntos_inicio = [
    (1, 6),
    (1, 20),
    (5, 13),
    (6, 3),
    (6, 17),
    (7, 3),
    (8, 16),
    (9, 22),
    (12, 13),
    (12, 19),
    (15, 13),
    (17, 5),
    (18, 20),
    (19, 4),
    (19, 5),
    (19, 19),
    (22, 14),
]

# Estacionamientos
lineas_llegada = [
    (2, 6),
    (2, 20),
    (4, 13),
    (5, 3),
    (6, 18),
    (8, 3),
    (8, 15),
    (9, 21),
    (11, 13),
    (11, 19),
    (16, 13),
    (17, 6),
    (17, 20),
    (19, 3),
    (19, 5),
    (20, 19),
    (21, 14),
]

puntos_inicio_random = random.sample(puntos_inicio, 5)
lineas_llegada_random = random.sample(lineas_llegada, 5)

# ------------------------------------------- Agents--------------------------------


class obstaculoAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.agentT = 0  # Obstacle

    def step(self):
        pass


class estacionamientoAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.agentT = 1  # Estacionamiento

    def step(self):
        pass


class semaforoAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.agentT = 2  # Semaforo
        self.estado = 0  # Color del semaforo 0 = rojo 1 = verde 2 = amarillo

    def step(self):
        pass


# --------------------------------------Main AGENT------------------------------------------


class CarAgent(Agent):
    def __init__(self, unique_id, model, pos, destino):
        super().__init__(unique_id, model)
        self.pos = pos
        self.destino = destino
        self.ruta = model.dijkstra(pos, destino)
        # self.ruta = self.ruta[1:]
        self.step_count = 0  # Contador de pasos
        print(
            f"Agente en {self.pos} con destino a {self.destino}. Mi ruta es: {self.ruta}"
        )

    def move(self):
        if len(self.ruta) > 1:
            siguiente_paso = self.ruta[1]

            dx = siguiente_paso[0] - self.pos[0]
            dy = siguiente_paso[1] - self.pos[1]

            if dx != 0:
                new_pos = (self.pos[0] + (dx // abs(dx)), self.pos[1])
            elif dy != 0:
                new_pos = (self.pos[0], self.pos[1] + (dy // abs(dy)))
            else:
                new_pos = self.pos
                self.ruta = self.ruta[1:]

            # TODO: Semaforos y colisiones
            self.model.grid.move_agent(self, new_pos)
            self.pos = new_pos
            self.step_count += 1

    def step(self):
        self.move()


# --------------------------------------MODEL------------------------------------------
class CarModel(Model):
    def __init__(self, width, height, num_agents):
        self.num_agents = num_agents
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.graph = nx.Graph()
        self.unique_id_counter = 0

        for node, connections in grafo_info.items():
            for neighbor, cost in connections.items():
                self.graph.add_edge(node, neighbor, weight=cost)

        self.running = True
        o = 0

        # Djikstra
        self.puntos_inicio = puntos_inicio_random
        self.lineas_llegada = lineas_llegada_random

        for punto, destino in zip(self.puntos_inicio, self.lineas_llegada):
            x, y = punto
            carro = CarAgent(o, model=self, pos=(x, y), destino=destino)
            self.schedule.add(carro)
            self.grid.place_agent(carro, (x, y))
            o += 1

        # Create the obstacles
        for i in ObstaculosM:
            # print("Mapa")
            pavA = obstaculoAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1
        # Create the estacionamientos
        for i in estacionamientos:
            # print("Mapa")
            pavA = estacionamientoAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1
        for i in semaforo:
            # print("Mapa")
            pavA = semaforoAgent(o, self)
            x, y = i
            self.schedule.add(pavA)
            self.grid.place_agent(pavA, (x, y))
            o += 1

    def dijkstra(self, inicio, destino):
        ruta_mas_corta = nx.shortest_path(
            self.graph, source=inicio, target=destino, weight="weight"
        )
        return ruta_mas_corta

    def step(self):
        self.schedule.step()
