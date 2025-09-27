board_a = [[8,7,6, 5,4,3, 1,9,2],
     [5,4,3, 2,1,9, 7,6,8],
     [2,1,9, 8,7,6, 4,3,5],
                   
     [1,9,8, 7,6,5, 3,2,4],
     [4,3,2, 1,9,8, 6,5,7],
     [7,6,5 ,4,3,2, 9,8,1],
                   
     [3,2,1, 9,8,7, 5,4,6],
     [6,5,4, 3,2,1, 8,7,9],
     [9,8,7, 6,5,4, 2,1,3]]

board_b  = board_a
selected_cell = (-1, -1)

def setup():
    global cell_size
    size(600,600)
    textAlign(CENTER, CENTER)
    textSize(24)
    random_blank()
    
def draw():
    background(250)
    draw_board(width/9)
    draw_numbers()
    highlight_selected_cell()
    
def draw_board(c):
    for i in range(10):
        if i % 3 == 0:
            strokeWeight(5)
        else :
            strokeWeight(1)
        line(i*c,0,i*c,height)
        line(0,i*c,width,i*c)

def draw_numbers():
    fill (0)
    for rol in range(9):
        for col in range(9):
            num = board_b[rol][col]
            if num != 0:
                x = col * (width/9) + (width/9) / 2
                y = rol * (height/9) + (height/9) / 2
                text(str(num), x, y)

def random_number_forbank():
    blank = []
    blank = [0]*7
    for i  in range(7):
        blank[i] = int(random(1,10))
    return  blank
    
def random_blank():
    for rol in range(9):
        random_number_forbank()
        for col in range(9):
            if board_b[rol][col] in random_number_forbank():
                board_b[rol][col] = 0
                
def mousePressed():
    global selected_cell
    col = mouseX // (width/9)
    row = mouseY // (width/9)
    if 0 <= row < 9 and 0 <= col < 9:
        selected_cell = (row, col)
        
def highlight_selected_cell():
    if selected_cell != (-1, -1):
        row, col = selected_cell
        fill(300,300,0,100)
        rect(col * (width/9), row * (width/9), (width/9), (width/9))
