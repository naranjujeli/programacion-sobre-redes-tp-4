from pygame_simulation import PygameSimulation


def main():
    
    width = 800
    height = 800
    food = 100
    generation_size = 21

    p = PygameSimulation(width, height, food, generation_size)
    p.start()

if __name__ == "__main__":
    main()