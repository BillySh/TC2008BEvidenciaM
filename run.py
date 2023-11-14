import mesa

# Data manipulation and analysis.
from evi_model import (
    CarModel,
    obstaculoAgent,
    estacionamientoAgent,
    semaforoRAgent,
    CarAgent, semaforoVAgent
)


def agent_portrayal(agent):
    portrayal = {}
    if isinstance(agent, obstaculoAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "#5A9BD5"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True

    if isinstance(agent, estacionamientoAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "yellow"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True

    if agent.estado == 0:
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True
    elif agent.estado == 1:
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "green"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True

    if isinstance(agent, CarAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "#00AF4F"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True

    return portrayal


grid = mesa.visualization.CanvasGrid(agent_portrayal, 24, 24)
server = mesa.visualization.ModularServer(
    CarModel, [grid], "Car Model", {"width": 24, "height": 24, "num_agents": 5}
)
server.port = 8521  # the default

server.launch()
