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
A=np.zeros((4,5))
#here we make a random 1 or 0 inside the matrix
A[1:-1,1:-1]=np.random.randint(2,size=(2,3))

# here we can check if the cell we be live or die .
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if (A[i][j]==1):
            #checking the sum of the neighbors of the live cell
            #total_sum=np.sum([A[i-1][j],A[i+1][j],A[i-1][j-1],A[i-1][j+1],A[i+1][j+1],A[i+1][j-1],A[i][j-1],A[i][j+1]])
            total_sum=np.sum([A[i-1,j-1:j+2:2],A[i,j-1:j+2:2],A[i+1,j-1:j+2:2]])
            A[i][j]=live_cell(total_sum)
        elif ((A[i][j]==0) and (i not in [0,A.shape[0]-1]) and (j not in [0,A.shape[1]-1])):
           total_sum2=np.sum([A[i-1,j-1:j+2:2],A[i,j-1:j+2:2],A[i+1,j-1:j+2:2]])
           if total_sum2==3:
               A[i][j]=1
            else:
               A[i][j] = 0
