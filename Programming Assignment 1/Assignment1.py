# UJJWAL SHARMA
# BT18CSE021
# usharma@students.vnit.ac.in


def dp(freq , d):
    if len(freq) == 0:
        return 0
    if tuple(freq) in d:
        return d[tuple(freq)]
    minVal = float('inf')
    for i in range(len(freq)):
        minVal = min(minVal , dp(freq[:i],d) + dp(freq[i+1:] , d))
    ans = sum(freq)
    if minVal != float('inf'):
        ans += minVal
    d[tuple(freq)] = ans
    return ans


class Node:
    def __init__(self , value , frequency , left=None , right=None):
        self.value = value
        self.frequency = frequency
        self.left = left
        self.right = right


def makeBST(sortedVals , frequencies , d):
    if len(frequencies) == 0:
        return None
    ind = -1
    fval = d[tuple(frequencies)]-sum(frequencies)
    for i in range(len(frequencies)):
        val = dp(frequencies[:i],d) + dp(frequencies[i+1:] , d)
        if val == fval:
            # print('found')
            ind = i
            break
    root = Node(sortedVals[ind] , frequencies[ind])
    root.left = makeBST(sortedVals[:ind] , frequencies[:ind] , d)
    root.right = makeBST(sortedVals[ind+1:] , frequencies[ind+1:] , d)
    return root



def breadthFirstSearch(root):
    print('\n\nPrinting Binary Search Tree in Breadth First Manner ... \n\n')
    queue = []
    queue.append([root,0])
    ld = 0
    print("Level : 1\n")
    while queue:
        nd ,d = queue.pop(0)
        if ld<d:
            print('\n\nLevel %d\n'%(d+1))
            ld = d
        print('name -> %s , frequency -> %d , level -> %d '%(nd.value , nd.frequency,d+1)  , sep=',' , end=' || ')
        if nd.left:
            queue.append([nd.left,d+1])
        if nd.right:
            queue.append([nd.right,d+1])
    print('\n\n\n')




def optimalBinarySearchTree(sortedVals , frequencies):
    d = {}
    fval = dp(frequencies , d)
    return makeBST(sortedVals , frequencies , d)





def BinaryTreeSearch(root , value , level):
    if root==None:
        return None , -1
    if value == root.value:
        return root , level
    if value<root.value:
        return BinaryTreeSearch(root.left , value , level+1)
    return BinaryTreeSearch(root.right , value,level+1)

def main():
    words = input("Enter Words ( Space Seperated eg . 'the hello new' : \n").split()
    frequency = list(map(int, input('Enter Correspnding Frequencies ( Space seperated eg. 10 30 500 ) : \n').split()))
    lst = []
    for w,f in zip(words , frequency):
        lst.append([w,f])
    lst = sorted(lst , key=lambda x : x[0])
    sortedWords = []
    sortedFrequencies = []
    for e in lst:
        sortedWords.append(e[0])
        sortedFrequencies.append(e[1])
    print(*sortedWords)
    print(*sortedFrequencies)

    root = optimalBinarySearchTree(sortedWords , sortedFrequencies)

    breadthFirstSearch(root)

    while True:
        print("\n*************************************************\n")
        search = input("Enter the word to search or press ^+c to exit : ")
        val,level = BinaryTreeSearch(root , search , 1)
        if val:
            print("\nFound -> %s , frequency : %d , level : %d \n"%(val.value , val.frequency , level))
        else:
            print("\nValue Not in the Search Tree\n")
        
    




if __name__ == "__main__":
    main()