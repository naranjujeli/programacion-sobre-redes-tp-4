from simulation import Simulation
from cronopio import ParserCronopio
import socketio as sk
import json

class SimulacionWeb(Simulation):

    def __init__(self, **kargs):
        super().__init__(width=kargs['width'], height=kargs['height'],food_amount=kargs['food'], size=kargs['generation_size'], frame=kargs['frame'], reproduction_pool_size=kargs['reproduction_pool_size'], mutation_parameters=kargs['mutation_parameters'])

        self._client = kargs['socket']

        self.__parser = ParserCronopio()

        cronopios_to_json = [self.__parser.from_cronopio_to_json(cronopio) for cronopio in self._current_generation]
        jsons = json.dumps({"cronopios": cronopios_to_json})
        self._client.emit("new_generation", jsons)

    def simulate(self):
        
        # dicts = [self.__parser.from_cronopio_to_json(cronopio) for cronopio in self._current_generation]
        # json_data = json.dumps(dicts)   

        # #ACA MANDARIAMOS POR SOKETS EL JSON
        # #Y GUARDARIAMOS LOS CRONOPIOS DE RESPUESTA EN UNA VARIABLE LLAMADABA dead_cronopios
        # dead_cronopios = []


        # result = [self.__parser.from_json_to_cronopio(cronopio_json) for cronopio_json in dead_cronopios]
        # return result
        pass

    @property
    def client(self):
        return self._client
    



if __name__ == "__main__":

    pass