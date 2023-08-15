import os
import readchar

map_oneline = "..###################\n..#.#.......#...#.#.#\n#.#.#.#.#.###.###.#.#\n#.#...#.#...#.......#\n#.#######.#######.###\n#...#.......#...#.#.#\n#.#######.###.###.#.#\n#.#.........#.....#.#\n#.#.###.#.#####.###.#\n#.....#.#.....#...#.#\n###########.#.###.#.#\n#.#.......#.#.....#.#\n#.###.###.#.#######.#\n#.......#.....#.#...#\n#.###.#######.#.###.#\n#...#...#.......#...#\n#.#######.#########.#\n#.#.....#.#.........#\n#.#.#.#.#.#.#.###.#.#\n#...#.#.#...#.#...#.#\n###################.."

map_split = list(map_oneline.split("\n"))

matriz = []

for fila in map_split:
    matriz.append(list(fila))

def imprimir_matriz(mapa):
    os.system('cls' if os.name == 'nt' else 'clear')
    for filas in mapa:
        print(''.join(filas))

def main_loop(mapa, posicion_inicial, posicion_final):
    px = posicion_inicial[0]
    py = posicion_inicial[1]

    mapa[px][py] = "p"
    imprimir_matriz(mapa)
    print("\n" + "Posición: " + str(px) + ", " + str(py))

    while True:
        k = readchar.readkey()
        if k == readchar.key.UP:
            if 0 < px <= len(mapa):
                if mapa[px - 1][py] != "#":
                    mapa[px][py] = "."
                    px -= 1
        elif k == readchar.key.DOWN:
            if 0 <= px < len(mapa) - 1:
                if mapa[px + 1][py] != "#":
                    mapa[px][py] = "."
                    px += 1
        elif k == readchar.key.LEFT:
            if 0 < py <= len(mapa[px]):
                if mapa[px][py - 1] != "#":
                    mapa[px][py] = "."
                    py -= 1
        elif k == readchar.key.RIGHT:
            if 0 <= py < len(mapa[px]) - 1:
                if mapa[px][py + 1] != "#":
                    mapa[px][py] = "."
                    py += 1

        mapa[px][py] = "p"
        imprimir_matriz(mapa)
        print("\n" + "Posición: " + str(px) + ", " + str(py))

        if px == posicion_final[0] and py == posicion_final[1]:
            print("Felicidades!")
            break

main_loop(matriz, (0, 0), (20, 20))
