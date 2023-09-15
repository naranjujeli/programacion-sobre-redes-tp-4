from pygame_simulation import PygameSimulation


def main():
    
    p = PygameSimulation(400, 400, 42, 21)
    p.simulate(p.cronopios)

if __name__ == "__main__":
    main()