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
cell_size = 50
canvas_width = cell_size * 9
canvas_height = canvas_width + ( cell_size *2)
add_number = [1,2,3,4,5,6,7,8,9]

def setup():
    size(canvas_width,canvas_height)
    textAlign(CENTER, CENTER)
    textSize(24)
    random_blank()
    
def draw():
    background(250)
    draw_board()
    draw_numbers()
    highlight_selected_cell()
    draw_add_number()
    
def draw_board():
    for i in range(10):
        if i % 3 == 0:
            strokeWeight(5)
        else :
            strokeWeight(1)
        line(i*cell_size,0,i*cell_size,canvas_height - (cell_size * 2))
        line(0,i*cell_size,canvas_width,i*cell_size)

def draw_add_number():
    for i in range(9):
        strokeWeight(5)
        fill(250)
        square(i*cell_size,canvas_height - (cell_size) ,cell_size)
        fill(0)
        num = add_number[i]
        x = i * (canvas_width/9) + (canvas_width/9) / 2
        y = (canvas_height - (cell_size/2))
        text(str(num), x, y)

def draw_numbers():
    fill (0)
    for rol in range(9):
        for col in range(9):
            num = board_b[rol][col]
            if num != 0:
                x = col * (canvas_width/9) + (canvas_width/9) / 2
                y = rol * ((canvas_height - (cell_size*2)) /9) + ((canvas_height - (cell_size*2)) /9) / 2
                text(str(num), x, y)

def draw_numbers():
    fill (0)
    for rol in range(9):
        for col in range(9):
            num = board_b[rol][col]
            if num != 0:
                x = col * (canvas_width/9) + (canvas_width/9) / 2
                y = rol * ((canvas_height - (cell_size*2)) /9) + ((canvas_height - (cell_size*2)) /9) / 2
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
    col = mouseX / (canvas_width/9)
    row = mouseY / ((canvas_height - (cell_size*2)) /9)
    if 0 <= row < 9 and 0 <= col < 9:
        selected_cell = (row, col)
        
def highlight_selected_cell():
    if selected_cell != (-1, -1):
        row, col = selected_cell
        fill(300,300,0,100)
        rect(col * ((canvas_height - (cell_size*2)) /9), row * (canvas_width/9), ((canvas_height - (cell_size*2)) /9), (canvas_width/9))
        for i in range (9):
            for  j in range (9):
                if board_b[i][j] == board_b[row][col] and board_b[row][col] !=  0:
                    fill(300,300,0,20)
                    rect(j * ((canvas_height - (cell_size*2)) /9), i * (canvas_width/9), ((canvas_height - (cell_size*2)) /9), (canvas_width/9))



    
