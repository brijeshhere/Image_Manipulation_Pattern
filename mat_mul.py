import numpy as np

mat1=np.random.randint(0,10,size=(3,4))
mat2=np.random.randint(0,10,size=(4,5))

mat3=np.zeros((3,5))
for i in range(mat1.shape[0]):
    for j in range(mat2.shape[1]):
        for k in range(4):
            mat3[i,j]+=mat1[i,k]*mat2[k,j]
print(mat3)
print(np.matmul(mat1,mat2))