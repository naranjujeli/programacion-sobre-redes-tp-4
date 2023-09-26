from pygame_simulation import PygameSimulation


def main():
    
    width = 400
    height = 400
    food = 30
    generation_size = 7

    p = PygameSimulation(width, height, food, generation_size)
    final_generation = 15
    counter = 0
    while counter <= final_generation:
        p.cicle()
        counter += 1


if __name__ == "__main__":
    main()