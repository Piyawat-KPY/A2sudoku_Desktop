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

def setup():
    global cell_size
    size(600,600)
    textAlign(CENTER, CENTER)
    textSize(24)


def draw():
    draw_board(width/9)
    draw_numbers()
    
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
    for rols in range(9):
        for cols in range(9):
            num = board_b[rols][cols]
            if num != 0:
                x = cols * (width/9) + (width/9) / 2
                y = rols * (height/9) + (height/9) / 2
                text(str(num), x, y)
