import mesa
# Data manipulation and analysis.
from evi_model import CarModel, obstaculoAgent, estacionamientoAgent, semaforoAgent


def get_pasos(model):
    return f"Pasos: {model.pasos}"


def get_choques(model):
    return f"Choques: {model.choques}"


def get_choquesToreto(model):
    return f"Choques Toreto: {model.toretoCrash}"


def agent_portrayal(agent):
    portrayal = {}
    if isinstance(agent, obstaculoAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "black"
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
    
    if isinstance(agent, semaforoAgent):
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
        portrayal["h"] = 1
        portrayal["w"] = 1
        portrayal["Filled"] = True


    return portrayal

grid = mesa.visualization.CanvasGrid(agent_portrayal,24, 24)
server = mesa.visualization.ModularServer(
    CarModel,[grid],"Car Model",{"width": 24, "height": 24, "num_agents": 1}

)
server.port = 8521  # the default

server.launch()