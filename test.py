tiles = []

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            tiles.append('0')
        else:
            tiles.append('1')
        

for i in range(0, 64, 8):
    print(" ".join(tiles[i:i+8]))


'''
    for i in tiles:
        if i == '1':
            pygame.draw.rect(screen, "gray", (x, y, 150, 150))

        x += 150
        if x == 8 * 150:
            x = 0
            y += 150
'''