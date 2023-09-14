from pygame_simulation import PygameSimulation




def main():
    
    p = PygameSimulation(400, 750, 3)
    p.simulate(p._inicial_cronopios)

if __name__ == "__main__":
    main()