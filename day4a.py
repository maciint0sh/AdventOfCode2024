data = '''
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

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
    for y in range(len(word_search)-4):
        for x in range(len(word_search[y])):
            if (word_search[y][x] == 'X') and (word_search[y+1][x] == 'M') and (word_search[y+2][x] == 'A') and (word_search[y+3][x] == 'S'):
                count += 1
    
    # upwards
    for y in range(len(word_search)-4):
        for x in range(len(word_search[y])):
            if (word_search[y][x] == 'S') and (word_search[y+1][x] == 'A') and (word_search[y+2][x] == 'M') and (word_search[y+3][x] == 'X'):
                count += 1
    
    return count

def check_diagonal(word_search):
    



    # upwards


    
