board_a = [[8,7,6, 5,4,3, 1,9,2],
     [5,4,3, 2,1,9, 7,6,8],
     [2,1,9, 8,7,6, 4,3,5],
     [1,9,8, 7,6,5, 3,2,4],
     [4,3,2, 1,9,8, 6,5,7],
     [7,6,5, 4,3,2, 9,8,1],
     [3,2,1, 9,8,7, 5,4,6],
     [6,5,4, 3,2,1, 8,7,9],
     [9,8,7, 6,5,4, 2,1,3]]

board_b = [row[:] for row in board_a]
cell_size = 50
canvas_width = cell_size * 9
canvas_height = canvas_width + ( cell_size *2)

selected_cell = (-1, -1)
Fixed_number = [[False for _ in range(9)] for _ in range(9)]
selected_number = None
dragging = False
drag_x, drag_y = 0, 0
chance = 3
IsComplete = False
file_name = "sudoku_save_game.txt"


def setup():
    size(canvas_width, canvas_height)
    textAlign(CENTER, CENTER)
    textSize(24)
    reset_game()
    load_game()
  
      
def draw():
    background(250)
    draw_board()
    draw_numbers()
    highlight_selected_cell()
    draw_add_number_cell()
    if dragging and selected_number is not None:
        fill(0, 0, 0, 0)
        square(drag_x - cell_size/2 , drag_y - cell_size/2 , cell_size)
        fill(0)
        text(str(selected_number) , drag_x , drag_y )
    lose_win_chance_reset_save()
    checkComplete()


def draw_board():
    for i in range(10):
        strokeWeight(5 if i % 3 == 0 else 1)
        line(i*cell_size, 0, i*cell_size, canvas_height - (cell_size * 2))
        line(0, i*cell_size, canvas_width, i*cell_size)


def draw_add_number_cell():
    for i in range(9):
        strokeWeight(5)
        fill(250)
        square(i*cell_size, canvas_height - cell_size ,cell_size)
        fill(0)
        x = i * cell_size + cell_size / 2
        y = canvas_height - (cell_size / 2)
        text(str(i+1), x, y)


def draw_numbers():
    for row in range(9):
        for col in range(9):
            if board_b[row][col] != 0:
                if Fixed_number[row][col]:
                    fill(0)
                elif isDuplicate(row , col , board_b[row][col]):
                    fill(200, 0, 0)    
                else:
                    fill(0, 200, 100)
                text(str(board_b[row][col]), col*cell_size + cell_size/2 , row*cell_size + cell_size/2)


def random_number_forbank():
    blank = []
    blank = [0]*6
    for i  in range(6):
        blank[i] = int(random(1,10))
    return  blank



def random_blank():
    for row in range(9):
        blanks = random_number_forbank()
        for col in range(9):
            if board_b[row][col] in blanks:
                board_b[row][col] = 0
                Fixed_number[row][col] = False


def mousePressed(): 
    global selected_cell, selected_number, drag_x, drag_y, dragging
    col = mouseX // cell_size
    row = mouseY // cell_size
    if 0 <= row < 9 and 0 <= col < 9:
        selected_cell = (row, col)
    elif canvas_height - cell_size <= mouseY < canvas_height:
        selected_number = col + 1
        dragging = True
        drag_x, drag_y = mouseX, mouseY
    elif row == 9 and col >= 7:
        reset_game()
    elif row == 9 and 5 <= col < 7:
        save_game()
        print("saved")


def highlight_selected_cell():
    if selected_cell != (-1, -1):
        row, col = selected_cell
        fill(255, 255, 0, 100)
        square(col * cell_size , row * cell_size, cell_size)
        for i in range(9):
            for j in range(9):
                if board_b[i][j] == board_b[row][col] and board_b[row][col] != 0:
                    fill(255, 255, 0, 20)
                    square(j * cell_size, i * cell_size, cell_size)


def mouseDragged():
    global drag_x, drag_y
    if dragging:
        drag_x, drag_y = mouseX, mouseY


def mouseReleased():
    global dragging, selected_number, chance
    if dragging and selected_number is not None:
        col = mouseX // cell_size
        row = mouseY // cell_size
        if 0 <= row < 9 and 0 <= col < 9:
            if not Fixed_number[row][col]: 
                if board_a[row][col] != selected_number:
                    chance -= 1
                board_b[row][col] = selected_number        
    dragging = False
    selected_number = None
    
    
def lose_win_chance_reset_save():
    global dragging, chance
    fill(0)
    text("Chance: %d" % chance, cell_size*2 - cell_size/2, canvas_height - (cell_size + cell_size/2))
    
    # Reset button
    fill(255)
    rect(canvas_width - cell_size*2 , cell_size*9 , cell_size*2 ,cell_size)
    fill(255, 0, 0)
    text("reset", canvas_width - cell_size, canvas_height - (cell_size + cell_size/2))
    
    # Save button
    fill(255)
    rect(canvas_width - cell_size*4 , cell_size*9 , cell_size*2 ,cell_size)
    fill(0, 255, 0)
    text("save", canvas_width - cell_size*3, canvas_height - (cell_size + cell_size/2))
    
    # Load button
    fill(255)
    rect(canvas_width - cell_size*6 , cell_size*9 , cell_size*2 ,cell_size)
    fill(155,0,300)
    text("load", canvas_width - cell_size*5, canvas_height - (cell_size + cell_size/2))
    
    if chance <= 0:
        fill(255, 0, 0)
        rect(canvas_width/2 - cell_size*2 , cell_size*4.5 - cell_size/2 , cell_size*4, cell_size)
        fill(0)
        text("You lose!", canvas_width/2 , cell_size*4.5)
        dragging = False
        
    elif IsComplete == True:
        fill(0, 255, 0)
        rect(canvas_width/2 - cell_size*2 , cell_size*4.5 - cell_size/2 , cell_size*4, cell_size)
        fill(0)
        text("You win!", canvas_width/2 , cell_size*4.5)
        dragging = False
    
            
def isDuplicate(that_row, that_col, answer):
    for j in range(9):
        if j != that_col and board_b[that_row][j] == answer:
            return True
    for i in range(9):
        if i != that_row and board_b[i][that_col] == answer:
            return True
        
    start_row = (that_row // 3) * 3
    start_col = (that_col // 3) * 3
    
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if (i != that_row or j != that_col) and board_b[i][j] == answer:
                return True
    return False

    
def checkComplete():
    global IsComplete
    for row in range (9):
        for col in range (9):
            if board_b[row][col] == 0 or isDuplicate(row , col , board_b[row][col]):
                IsComplete = False
                return
    IsComplete = True

        
def reset_game():
    global board_b, chance , Fixed_number
    board_b = [row[:] for row in board_a] 
    chance = 3
    Fixed_number = [[True for _ in range(9)] for _ in range(9)]                        
    random_blank()

def save_game():
    file = createWriter(file_name)
    for row in board_b:
        for num in row:
            file.write(str(num) + " ")
        file.print("\n") 
    file.close()

def load_game():
    global board_b, Fixed_number
    board_b = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
    for line in lines:
        row = [int(num) for num in line.split()]
        board_b.append(row)

    Fixed_number = []
    for row in board_b:
        fixed_row = []
        for num in row:
            if num == 0:
                fixed_row.append(False)  
            else:
                fixed_row.append(True)  
        Fixed_number.append(fixed_row)
