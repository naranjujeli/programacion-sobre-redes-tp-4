from pygame_simulation import PygameSimulation


def main():
    
    width = 1500
    height = 800
    food = 300
    generation_size = 21

    p = PygameSimulation(width, height, food, generation_size)
    while True:
        p.cicle()


if __name__ == "__main__":
    main()