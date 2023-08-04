import readchar

while True:
    key = readchar.readkey()
    if key == readchar.key.UP:
        print("Adiós")
        break
    print(f"Presionaste la tecla: {key}")
