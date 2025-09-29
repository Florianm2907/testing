import mouse

while True:
    if mouse.is_pressed("left"):
        print(mouse.get_position())