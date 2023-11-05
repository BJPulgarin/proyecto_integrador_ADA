import random
import os
import readchar
from functools import reduce

class Juego:
    def __init__(self, posicion_inicial=None, posicion_final=None, mapa=None):
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        self.mapa = mapa

    def imprimir_matriz(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for filas in self.mapa:
            print(''.join(filas))

    def main_loop(self):
        px = self.posicion_inicial[0]
        py = self.posicion_inicial[1]

        self.mapa[px][py] = "p"
        self.imprimir_matriz()
        print("\n" + "Posición: " + str(px) + ", " + str(py))

        while True:
            k = readchar.readkey()
            if k == readchar.key.UP:
                if 0 < px <= len(self.mapa):
                    if self.mapa[px - 1][py] != "#":
                        self.mapa[px][py] = "."
                        px -= 1
            elif k == readchar.key.DOWN:
                if 0 <= px < len(self.mapa) - 1:
                    if self.mapa[px + 1][py] != "#":
                        self.mapa[px][py] = "."
                        px += 1
            elif k == readchar.key.LEFT:
                if 0 < py <= len(self.mapa[px]):
                    if self.mapa[px][py - 1] != "#":
                        self.mapa[px][py] = "."
                        py -= 1
            elif k == readchar.key.RIGHT:
                if 0 <= py < len(self.mapa[px]) - 1:
                    if self.mapa[px][py + 1] != "#":
                        self.mapa[px][py] = "."
                        py += 1

            self.mapa[px][py] = "p"
            self.imprimir_matriz()
            print("\n" + "Posición: " + str(py) + ", " + str(px))

            if px == self.posicion_final[1] and py == self.posicion_final[0]:
                print("Felicidades!")
                break

class JuegoArchivo(Juego):

    def __init__(self):
        super().__init__()
        lista_de_mapas = os.listdir("./mapas")
        mapa_aleatorio = random.choice(lista_de_mapas)
        self.path = "./mapas/" + mapa_aleatorio

    def LeerMapa(self):
        with open(self.path, "r") as f:
            lines = f.readlines()

        cadena = reduce(lambda x, y: x + y, lines)
        cadena = cadena.strip()

        mapa = list(map(list, map(lambda line: list(filter(lambda c: c != '\n', line)), cadena.split("\n")[1:])))
        self.mapa = mapa

        coordenadas = cadena.split("\n")[0].split(" ")

        self.posicion_inicial = tuple(map(int, coordenadas[:2]))
        self.posicion_final = tuple(map(int, coordenadas[2:]))

nuevo_juego = JuegoArchivo()
nuevo_juego.LeerMapa()  # Básicamente podemos usar este método para elegir nuevos mapas al azar
nuevo_juego.main_loop()
