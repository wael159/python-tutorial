import numpy as np

# first we must check where is the 1 value - and check around it how much 1's he have .

def live_cell(total_sum):
    """:arg: total sum
    :return: 1 or 0"""
    if total_sum<2:
        return 0
    elif total_sum==2 or total_sum==3:
        return 1
    elif total_sum>3:
        return 0

# here we initialize a matrix of zeros , to make the border zeros
Game_of_life=np.zeros((4, 5))
#here we make a random 1 or 0 inside the matrix (the borders are zeros)
Game_of_life[1:-1, 1:-1]=np.random.randint(2, size=(2, 3))

# here we can check if the cell will be live or die and update it.
for i in range(Game_of_life.shape[0]):
    for j in range(Game_of_life.shape[1]):
        if (Game_of_life[i][j]==1):
            #finding the sum of all the 1's around the live cell
            total_sum_1=np.sum([Game_of_life[i - 1, j - 1:j + 2:2], Game_of_life[i, j - 1:j + 2:2], Game_of_life[i + 1, j - 1:j + 2:2]])
            Game_of_life[i][j]=live_cell(total_sum_1)
        elif ((Game_of_life[i][j] == 0) and (i not in [0, Game_of_life.shape[0] - 1]) and (j not in [0, Game_of_life.shape[1] - 1])):
            #finding the sum of all the 1's around the die cell
           total_sum_0=np.sum([Game_of_life[i - 1, j - 1:j + 2:2], Game_of_life[i, j - 1:j + 2:2], Game_of_life[i + 1, j - 1:j + 2:2]])
           if total_sum_0==3:
                Game_of_life[i][j]=1
           else:
               Game_of_life[i][j] = 0

print(Game_of_life)
