data = '''
XMASXXSAMX
MSAMXMSMSM
AMXSXMAAMA
SSAMASMSMS
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
AAXAMASAAA
MAMMMXMMMM
XXMXAXMASX'''

word_search = data.split('\n')
word_search.pop(0)


# vertical, up or down
# horizontal, left or right
# diagonal: up left, up right, down left, down right

def check_horizontal(row):
    forwards = 'XMAS'
    backwards = 'SAMX'
    count = 0 # for this row
    for i in range(len(row)-4):
        if row[i:i+4] == forwards or row[i:i+4] == backwards:
            count += 1
    
    return count

def check_vertical(word_search):
    # downwards
    count = 0
    for y in range(len(word_search)-3):
        for x in range(len(word_search[y])):
            # print(word_search[y])
            if (word_search[y][x] == 'X') and (word_search[y+1][x] == 'M') and (word_search[y+2][x] == 'A') and (word_search[y+3][x] == 'S'):
                count += 1
                # print(f"Vertical at {x} {y}")
    
    # upwards
    for y in range(len(word_search)-3):
        for x in range(len(word_search[y])):
            if (word_search[y][x] == 'S') and (word_search[y+1][x] == 'A') and (word_search[y+2][x] == 'M') and (word_search[y+3][x] == 'X'):
                count += 1
                # print(f"Vertical at {x} {y+3}")
    
    return count

def check_diagonal(word_search):
    # down right
    count = 0
    dr = 0
    dl = 0
    ur = 0
    ul = 0
    for y in range(len(word_search)-4):
        for x in range(len(word_search)-4):
            down_right = (word_search[y][x] == 'X') and (word_search[y+1][x+1] == 'M') and (word_search[y+2][x+2] == 'A') and (word_search[y+3][x+3] == 'S')
            if down_right:
                count += 1
                # dr += 1
    # print(dr)
    # down left
    for y in range(len(word_search)-4):
        for x in range(3, len(word_search)):
            down_left = (word_search[y][x] == 'X') and (word_search[y+1][x-1] == 'M') and (word_search[y+2][x-2] == 'A') and (word_search[y+3][x-3] == 'S')
            if down_left:
                count += 1
                # dl += 1
    # print(dl)
    # up right
    for y in range(3, len(word_search)):
        for x in range(len(word_search)-4):
            up_right = (word_search[y][x] == 'X') and (word_search[y-1][x+1] == 'M') and (word_search[y-2][x+2] == 'A') and (word_search[y-3][x+3] == 'S')
            if up_right:
                count += 1
                # ur += 1
    # print(ur)
    # up left
    for y in range(3, len(word_search)):
        for x in range(3, len(word_search)):
            up_left = (word_search[y][x] == 'X') and (word_search[y-1][x-1] == 'M') and (word_search[y-2][x-2] == 'A') and (word_search[y-3][x-3] == 'S')
            if up_left:
                count += 1
                # ul += 1
    # print(ul)
    # this could definitely be made more efficient
    # but naaaaahhhhh
    return count

count = 0
h_count = 0
v_count = 0
diag_count = 0
for row in word_search:
    h_count += check_horizontal(row)
v_count = check_vertical(word_search)
diag_count = check_diagonal(word_search)

print(f"Horizontal: {h_count}")
print(f"Vertical: {v_count}")
print(f"Diagonal: {diag_count}")
print(f"Total: {v_count + h_count + diag_count}")