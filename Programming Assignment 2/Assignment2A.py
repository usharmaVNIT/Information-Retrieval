# UJJWAL SHARMA
# BT18CSE021
# usharma@students.vnit.ac.in




SubstitutionMatrix = [
    [0,0, 7, 1, 342, 0, 0, 2, 118, 0, 1, 0, 0, 3, 76, 0, 0, 1, 35, 9 ,9 ,0, 1, 0, 5, 0]
    ,[0 ,0 ,9 ,9 ,2 ,2 ,3 ,1 ,0 ,0 ,0 ,5 ,11 ,5 ,0 ,10, 0, 0, 2, 1, 0, 0, 8, 0, 0, 0]
    ,[6, 5, 0, 16, 0, 9, 5, 0, 0, 0, 11, 0, 7, 9, 1, 10, 2, 5, 39, 40, 1, 3, 7, 1, 1, 0]
    ,[1, 10, 13, 0, 12, 0, 5, 5, 0, 0, 2, 3, 7, 3, 0, 1, 0, 43, 39, 22, 0, 0, 4, 0, 2, 0]
    ,[388, 0, 3, 11, 0, 2, 2, 0, 89, 0, 0, 3, 0, 5, 93, 0, 0, 14, 12, 6, 15, 0, 1, 0, 18, 0]
    ,[0, 15, 0, 3, 1, 0, 5, 2, 0, 0, 0, 3, 4, 1, 0, 0, 0, 6, 4, 12, 0, 0, 2, 0, 0, 0]
    ,[4, 1, 11, 11, 9, 2, 0, 0, 0, 1, 1, 3, 0, 0, 2, 1, 3, 5, 13, 21, 0, 0, 1, 0, 3, 0]
    ,[1, 8, 0, 3, 0, 0, 0, 0, 0, 0, 2, 0, 12, 14, 2, 3, 0, 3, 1, 11, 0, 0, 2, 0, 0, 0]
    ,[103, 0, 0, 0, 146, 0, 1, 0, 0, 0, 0, 6, 0, 0, 49, 0, 0, 0, 2, 1, 47, 0, 2, 1, 15, 0]
    ,[0, 1, 1, 9, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0]
    ,[1, 2, 8, 4, 1, 1, 2, 5, 0, 0, 0, 0, 5, 0, 2, 0, 0, 0, 6, 0, 0, 0, 4, 0, 0, 3]
    ,[2, 10, 1, 4, 0, 4, 5, 6, 13, 0, 1, 0, 0, 14, 2, 5, 0, 11, 10, 2, 0, 0, 0, 0, 0, 0]
    ,[1, 3, 7, 8, 0, 2, 0, 6, 0, 0, 4, 4, 0, 180, 0, 6, 0, 0, 9, 15, 13, 3, 2, 2, 3, 0]
    ,[2, 7, 6, 5, 3, 0, 1, 19, 1, 0, 4, 35, 78, 0, 0, 7, 0, 28, 5, 7, 0, 0, 1, 2, 0, 2]
    ,[91, 1, 1, 3, 116, 0, 0, 0, 25, 0, 2, 0, 0, 0, 0, 14, 0, 2, 4, 14, 39, 0, 0, 0, 18, 0]
    ,[0, 11, 1, 2, 0, 6, 5, 0, 2, 9, 0, 2, 7, 6, 15, 0, 0, 1, 3, 6, 0, 4, 1, 0, 0, 0]
    ,[0, 0, 1, 0, 0, 0, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ,[0, 14, 0, 30, 12, 2, 2, 8, 2, 0, 5, 8, 4, 20, 1, 14, 0, 0, 12, 22, 4, 0, 0, 1, 0, 0]
    ,[11, 8, 27, 33, 35, 4, 0, 1, 0, 1, 0, 27, 0, 6, 1, 7, 0, 14, 0, 15, 0, 0, 5, 3, 20, 1]
    ,[3, 4, 9, 42, 7, 5, 19, 5, 0, 1, 0, 14, 9, 5, 5, 6, 0, 11, 37, 0, 0, 2, 19, 0, 7, 6]
    ,[20, 0, 0, 0, 44, 0, 0, 0, 64, 0, 0, 0, 0, 2, 43, 0, 0, 4, 0, 0, 0, 0, 2, 0, 8, 0]
    ,[0, 0, 7, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 8, 3, 0, 0, 0, 0, 0, 0]
    ,[2, 2, 1, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 7, 0, 6, 3, 3, 1, 0, 0, 0, 0, 0]
    ,[0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]
    ,[0, 0, 2, 0, 15, 0, 1, 7, 15, 0, 0, 0, 2, 0, 6, 1, 0, 7, 36, 8, 5, 0, 0, 1, 0, 0]
    ,[0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 5, 0, 0, 0, 0, 2, 21, 3, 0, 0, 0, 0, 3, 0]]




def EditDistance(string1, string2):
    m, n = len(string1), len(string2)
    matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
    matrix[0][0] = 0 
    insertionCost = 1
    deletionCost = 1
    for i in range(1, n+1):
        matrix[0][i] = matrix[0][i-1] + insertionCost

    for i in range(1, m+1):
        matrix[i][0] = matrix[i-1][0] + deletionCost
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            matrix[i][j] =  min(matrix[i][j-1] + insertionCost, matrix[i-1][j] + deletionCost, matrix[i-1][j-1] + SubstitutionMatrix[ord(string1[i-1])-97][ord(string2[j-1])-97])      

    i, j = m, n 
    answer = [] 
    while i!=0 and j!=0:
        if string1[i-1] == string2[j-1]:
            var = f"No Change i.e {string1[i-1]}"
            answer.append("{:25}".format(var)+ "Cost: 0")
            i, j = i-1, j-1
        else:
            #substitute
            if matrix[i-1][j-1]+SubstitutionMatrix[ord(string1[i-1])-97][ord(string2[j-1])-97] <= min(matrix[i-1][j]+deletionCost, matrix[i][j-1]+insertionCost):
                var = f"Substitute {string1[i-1]} with {string2[j-1]}"
                answer.append("{:25}".format(var)+f"Cost: {SubstitutionMatrix[ord(string1[i-1])-97][ord(string2[j-1])-97]}")
                i=i-1
                j=j-1
            
            #delete
            elif matrix[i-1][j]+deletionCost <= min(matrix[i-1][j-1]+SubstitutionMatrix[ord(string1[i-1])-97][ord(string2[j-1])-97], matrix[i][j-1]+insertionCost):
                var = f"Delete {string1[i-1]}"
                answer.append("{:25}".format(var)+f"Cost: {deletionCost}")
                i=i-1

            #insert
            elif matrix[i][j-1]+insertionCost <= min(matrix[i-1][j-1]+SubstitutionMatrix[ord(string1[i-1])-97][ord(string2[j-1])-97], matrix[i-1][j]+deletionCost):
                var = f"Insert {string2[j-1]}"
                answer.append("{:25}".format(var)+f"Cost: {insertionCost}")
                j = j-1
            
    while i!=0:
        var = f"Delete {string1[i-1]}"
        answer.append("{:25}".format(var)+f"Cost: {deletionCost}")
        i, j = i-1, j

    while j!=0:
        var = f"Insert {string2[j-1]}"
        answer.append("{:25}".format(var)+f"Cost: {insertionCost}")
        i, j = i, j-1


    print("\n")
    print("\n".join(answer[::-1]))
    print('\n\n')
    print(f"Total Cost: {matrix[m][n]}\n\n")
            
    


def main():

    string1 = input("Enter String 1 : ")
    string2 = input("Enter String 2 : ")
    EditDistance(string1 , string2)
    return 0

if __name__=="__main__":
    main()

