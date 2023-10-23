from simulation import Simulation
from cronopio import ParserCronopio

class SimulacionWeb(Simulation):

    def __init__(self, **kargs):
        super().__init__(**kargs)


    def simulate(self, generation):
        
        parser = ParserCronopio()
        jsons = [parser.from_cronopio_to_json(cronopio) for cronopio in generation]

        #ACA MANDARIAMOS POR SOKETS EL JSON
        #Y GUARDARIAMOS LOS CRONOPIOS DE RESPUESTA EN UNA VARIABLE LLAMADABA dead_cronopios
        dead_cronopios = []


        result = [parser.from_json_to_cronopio(cronopio_json) for cronopio_json in dead_cronopios]
        return result

    