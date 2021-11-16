

matrix = []
print("Enter the matrix rowwise:")
  

for i in range(3):          
    a =[]
    for j in range(3):     
         a.append(int(input()))
    matrix.append(a)
  

for i in range(3):
    for j in range(3):
        print(matrix[i][j], end = " ")
    print()

A = matrix
B= matrix
C= matrix
D= matrix


for i in range(len(matrix)):
   for j in range(len(matrix[0])):
       if(matrix[i][j]==0):
         
          c=input("Operation: ")
        
          if(c=='D'):
              if(i<(len(matrix)-1)):
                 temp=matrix[i][j]
                 matrix[i][j]=matrix[i+1][j]
                 matrix[i+1][j]=temp
                 for i in range(len(matrix)):
                   for j in range(len(matrix[0])):
                    print(matrix[i][j], end = " ")
                   print()
                
              else:
                 print("Invalid Operation")   

          elif(c=='U'):
                 if(i>0):
                   temp=matrix[i][j]
                   matrix[i][j]=matrix[i-1][j]
                   matrix[i-1][j]=temp
                   for i in range(len(matrix)):
       
                    for j in range(len(matrix[0])):
                      print(matrix[i][j], end = " ") 
                    print()  
                
                 else:
                  print("Invalid Operation")  

          elif(c=='R'):
                if(j<(len(matrix[0])-1)):
                  temp=matrix[i][j]
                  matrix[i][j]=matrix[i][j+1]
                  matrix[i][j+1]=temp
                  for i in range(len(matrix)):
    
                      for j in range(len(matrix[0])):
                       print(matrix[i][j], end = " ")
                      print() 
                
                else:
                 print("Invalid Operation")   

          else:
                if(j>0):
                 temp=matrix[i][j]
                 matrix[i][j]=matrix[i][j-1]
                 matrix[i][j-1]=temp 
                 for i in range(len(matrix)):
       
                      for j in range(len(matrix[0])):
                         print(matrix[i][j], end = " ")  
                      print()   

                else:
                  print("Invalid Operation") 
         
      
  