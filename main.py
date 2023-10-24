from pygame_simulation import PygameSimulation



def main():
    
    width = 750
    height = 400
    food = 500
    generation_size = 21
    frame = 15
    reproduction_pool_size = 7
    mutation_parameters = 0.4

    p = PygameSimulation(width=width, height=height, food=food, generation_size=generation_size, frame=frame, reproduction_pool_size=reproduction_pool_size, mutation_parameters=mutation_parameters)
    while True:
        p.cicle()


if __name__ == "__main__":
    main()