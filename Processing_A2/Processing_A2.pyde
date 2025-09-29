board_a = [[8,7,6, 5,4,3, 1,9,2],
     [5,4,3, 2,1,9, 7,6,8],
     [2,1,9, 8,7,6, 4,3,5],
                   
     [1,9,8, 7,6,5, 3,2,4],
     [4,3,2, 1,9,8, 6,5,7],
     [7,6,5 ,4,3,2, 9,8,1],
                   
     [3,2,1, 9,8,7, 5,4,6],
     [6,5,4, 3,2,1, 8,7,9],
     [9,8,7, 6,5,4, 2,1,3]]

board_b = [row[:] for row in board_a]
selected_cell = (-1, -1)
selected_number = None
cell_size = 50
canvas_width = cell_size * 9
canvas_height = canvas_width + ( cell_size *2)
dragging = False
drag_x,drag_y = 0,0
chance = 3

def setup():
    size(canvas_width,canvas_height)
    textAlign(CENTER, CENTER)
    textSize(24)
    reset_game()
    
def draw():
    background(250)
    draw_board()
    draw_numbers()
    highlight_selected_cell()
    draw_add_number_cell()
    if dragging and selected_number is not None:
        fill(0,0,0,0)
        square(drag_x - cell_size/2 , drag_y - cell_size/2 , cell_size)
        fill(0)
        text(str(selected_number) , drag_x , drag_y )
    lose_win_chance_reset_save()

def draw_board():
    for i in range(10):
        if i % 3 == 0:
            strokeWeight(5)
        else :
            strokeWeight(1)
        line(i*cell_size,0,i*cell_size,canvas_height - (cell_size * 2))
        line(0,i*cell_size,canvas_width,i*cell_size)

def draw_add_number_cell():
    for i in range(9):
        strokeWeight(5)
        fill(250)
        square(i*cell_size,canvas_height - (cell_size) ,cell_size)
        fill(0)
        x = i * (canvas_width/9) + (canvas_width/9) / 2
        y = (canvas_height - (cell_size/2))
        text(str(i+1), x, y)

def draw_numbers():
    for rol in range(9):
        for col in range(9):
            num = board_b[rol][col]
            if num != 0:
                fill (0)
                x = col * (canvas_width/9) + (canvas_width/9) / 2
                y = rol * ((canvas_height - (cell_size*2)) /9) + ((canvas_height - (cell_size*2)) /9) / 2
                if num != board_a[rol][col]:
                    fill (300,0,0)
                text(str(num), x, y)
              
def random_number_forbank():
    blank = []
    blank = [0]*6
    for i  in range(6):
        blank[i] = int(random(1,10))
    return  blank
    
def random_blank():
    for rol in range(9):
        random_number_forbank()
        for col in range(9):
            if board_b[rol][col] in random_number_forbank():
                board_b[rol][col] = 0
                
def mousePressed(): 
    global selected_cell,selected_number,drag_x,drag_y,dragging
    col = mouseX // (cell_size)
    row = mouseY // (cell_size)
    if 0 <= row < 9 and 0 <= col < 9:
        selected_cell = (row, col)
    if row  == 10:
        selected_number = (col+1)
        dragging = True
        drag_x,drag_y = mouseX,mouseY
    if row == 9  and col >= 7:
        reset_game()
    if col >= 5  and col < 7:
        save_game("sudoku_save_game.txt")
        print("saved")

def highlight_selected_cell():
    if selected_cell != (-1, -1):
        row, col = selected_cell
        fill(300,300,0,100)
        rect(col * ((canvas_height - (cell_size*2)) /9), row * (canvas_width/9), ((canvas_height - (cell_size*2)) /9), (canvas_width/9))
        for i in range (9):
            for  j in range (9):
                if board_b[i][j] == board_b[row][col] and board_b[row][col] !=  0:
                    fill(300,300,0,20)
                    square(j * ((canvas_height - (cell_size*2)) /9), i * (canvas_width/9), ((canvas_height - (cell_size*2)) /9))

def mouseDragged():
    global drag_x,drag_y
    if dragging:
        drag_x,drag_y = mouseX, mouseY

def mouseReleased():
    global dragging, selected_number, chance
    if dragging and selected_number is not None:
        col = mouseX // cell_size
        row = mouseY // cell_size
        if row < 9 and col < 9:
            if board_a[row][col] != selected_number:
                chance -= 1
            board_b[row][col] = selected_number        
    dragging = False
    selected_number = None
    
def lose_win_chance_reset_save():
    global dragging
    global chance
    
    text("chance : %d" % chance  , cell_size*2 - cell_size/2  , canvas_height  - (cell_size  + cell_size/2) )
    fill(255)
    
    rect(canvas_width - cell_size*2 , cell_size*9  , cell_size*2 ,cell_size)
    fill(300,0,0)
    text("reset" ,canvas_width - cell_size, canvas_height  - (cell_size  + cell_size/2) )
    
    fill(255)
    rect(canvas_width - cell_size*4 , cell_size*9  , cell_size*2 ,cell_size)
    fill(0,300,0)
    text("save" ,canvas_width - cell_size*3, canvas_height  - (cell_size  + cell_size/2) )
    
    if  chance <= 0  :
        fill(300,0,0)
        rect(canvas_width/2 - cell_size*2 , cell_size*9/2 - cell_size/2 , cell_size*4,cell_size)
        fill(0)
        text("You  lose!",canvas_width/2 , cell_size*9/2 )
        dragging = False
    
    if  board_b == board_a:
        fill(0,300,0)
        rect(canvas_width/2 - cell_size*2 , cell_size*9/2 - cell_size/2 , cell_size*4,cell_size)
        fill(0)
        text("You  win!",canvas_width/2 , cell_size*9/2 )
        dragging = False
        
def reset_game():
    global board_b, chance
    board_b = [row[:] for row in board_a] 
    chance = 3                            
    random_blank()

def save_game(filename):
    file = createWriter(filename)
    for row in board_b:
        for num in row:
            file.write(str(num) + " ")
        file.print("\n") 
    file.close()
