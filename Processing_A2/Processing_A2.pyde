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
cell_size = 50

def setup():
    global cell_size
    size(600,600)

def draw():
    draw_board(width/9)
    
def draw_board(c):
    fill(0)
    for i in range(9):
        if i % 3 == 0:
            strokeWeight(5)
        else :
            strokeWeight(1)
        line(i*c,0,i*c,height)
        line(0,i*c,width,i*c)
