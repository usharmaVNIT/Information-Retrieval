# UJJWAL SHARMA
# BT18CSE021
# usharma@students.vnit.ac.in



import os
import string
import json
import time
import random
import matplotlib.pyplot as plt


def linearSearch(arr , current):
    if len(arr)==0 or arr[-1]<=current:
        return float('inf')
    if arr[0]>current:
        return arr[0]
    c = 0
    while arr[c]<=current:
        c+=1
    return arr[c]


def nextLinearSearch(arr , current):
    return linearSearch(arr , current)



def BinarySearch(arr , low , high , current):
    while high-low>1:
        mid = (high+low)//2
        if arr[mid] <= current:
            low = mid
        else:
            high = mid
    return high


def nextBinarySearch(arr  , current):
    if len(arr)==0 or arr[-1]<= current:
        return float('inf')
    if arr[0]>current:
        return arr[0]
    ind = BinarySearch(arr , 0 , len(arr)-1 , current)
    return arr[ind]



def GallopingSearch(arr , current):
    if len(arr)==0 or arr[-1]<=current:
        return float('inf')
    if arr[0]>current:
        return arr[0]
    low = 0
    jump = 1
    high = low+jump
    while high < len(arr) and arr[high] <= current:
        low = high
        jump *=2
        high = low+jump
    if high>=len(arr):
        high = len(arr)-1
    ind = BinarySearch(arr , low , high , current)
    return arr[ind]


def nextGallopingSearch(arr , current):
    return GallopingSearch(arr , current)




def nextPhrase(postingLists , position , next):
    v = next(postingLists[0], position)
    u = v

    for e in postingLists[1:]:
        v = next(e , v)
    if v == float('inf'):
        return [float('inf')]*2
    if len(postingLists)-1 == v-u:
        return [u,v]
    return nextPhrase(postingLists , v-len(postingLists) , next)



def makeInvertedIndex():
    invertedIndex = {}
    parentDirectory = os.getcwd()
    corpusDirectory = os.path.join(parentDirectory , "CorpusDirectory")
    os.chdir(corpusDirectory)
    files = os.listdir()
    docIDToFiles = {}
    for docID , file in enumerate(files):
        docIDToFiles[docID+1] = file
        localDict = {}
        with open(file , 'r') as opened:
            lines = opened.readlines()
            position = 0
            for line in lines:
                lineList = line.translate(line.maketrans('', '', string.punctuation)).strip().split()
                for word in lineList:
                    position+=1
                    lword = word.lower()
                    if lword in localDict:
                        localDict[lword].append(position)
                    else:
                        localDict[lword] = [position]
        for word in localDict:
            lword = word.lower()
            if lword not in invertedIndex:
                invertedIndex[lword] = {}
            invertedIndex[lword][docID+1] = localDict[lword]
        # print(localDict)
    sortedWords = sorted(invertedIndex.keys())
    # for word in sortedWords:
    #     print(word , invertedIndex[word] , sep='  ---->  ')
    # print(os.getcwd())
    os.chdir(parentDirectory)
    # print(os.getcwd())
    return sortedWords , invertedIndex , docIDToFiles


def getCommonDocID(phrase , invertedIndex , totalDocs):
    for e in phrase:
        if e not in invertedIndex:
            return []
    ans = set([x+1 for x in range(totalDocs)])
    for e in phrase:
        ans = ans.intersection(invertedIndex[e])
    return sorted(ans)
    

# enter filename
def saveInvertedIndex(invertedIndex):
    filename = 'InvertedIndex/invertedIndex@'+ str(time.time())+'.json'
    with open(filename , 'w') as savingFile:
        json.dump(invertedIndex , savingFile , indent=4 )






def getPhraseTest(words , invertedIndex , docsToIds):
    wordsStr = ' '.join(words)
    words =  wordsStr.translate(wordsStr.maketrans('', '', string.punctuation)).strip().lower().split()
    print(*words)
    totalDocs = len(docsToIds.keys())
    commonDocIdLists = getCommonDocID(words , invertedIndex , totalDocs)
    searchOption = 0
    while True:
        searchOption = int(input("Enter Search Option . \n1 -> Linear Search\n2 -> Binary Search\n3 -> Galloping Search\n : "))
        if 0<searchOption<4:
            break
    searchOptionDictionary = {}
    searchOptionDictionary[1] = nextLinearSearch
    searchOptionDictionary[2] = nextBinarySearch
    searchOptionDictionary[3] = nextGallopingSearch
    for docID in commonDocIdLists:
        postinglists = []
        for word in words:
            lst = invertedIndex[word][docID]
            postinglists.append(lst)
        ans = nextPhrase(postinglists , 0 , searchOptionDictionary[searchOption])
        if ans[0]!= float('inf'):
            print('Phrase found in %s between : ' %docsToIds[docID] , ans)




def getPhraseSearch(words , invertedIndex , docsToIds , searchChoice):
    wordsStr = ' '.join(words)
    words =  wordsStr.translate(wordsStr.maketrans('', '', string.punctuation)).strip().lower().split()
    print(*words)
    totalDocs = len(docsToIds.keys())
    commonDocIdLists = getCommonDocID(words , invertedIndex , totalDocs)
    searchOptionDictionary = {}
    searchOptionDictionary[1] = nextLinearSearch
    searchOptionDictionary[2] = nextBinarySearch
    searchOptionDictionary[3] = nextGallopingSearch
    answers = []
    for docID in commonDocIdLists:
        postinglists = []
        for word in words:
            lst = invertedIndex[word][docID]
            postinglists.append(lst)
        ans = nextPhrase(postinglists , 0 , searchOptionDictionary[searchChoice])
        if ans[0]!= float('inf'):
            answers.append([docsToIds[docID] , ans])
    print(len(answers))
    answers = sorted(answers , key = lambda x:x[0])
    return answers







def GenerateQueries():
    queriesPerDocument = 3
    queries = []
    parentDirectory = os.getcwd()
    corpusDirectory = os.path.join(parentDirectory , "CorpusDirectory")
    files = os.listdir(corpusDirectory)
    for file in files:
        filepath = os.path.join(corpusDirectory,file)
        with open(filepath,'r') as f:
            lines = f.readlines()
            modulo = len(lines)//queriesPerDocument
            for index,line in enumerate(lines):
                if (index+1)%modulo == 0:
                    words = line.translate(line.maketrans('', '', string.punctuation)).strip().split()
                    query_length = random.randint(5,10)
                    r1 = random.randint(0, 6)
                    queries.append(words[r1:r1+query_length])

    filepath = os.path.join(parentDirectory,'queries.txt')
    with open(filepath,'w') as f:
        for words in queries:
            query = ''
            for word in words:
                query = query + word+ ' '
            print(query)
            f.write(query+'\n')

    return queries

















def drawPlot(invertedIndex , docsToIds):
    queries = []
    with open('queries.txt', 'r') as opened:
        lines = opened.readlines()
        for line in lines:
            lineList = line.translate(line.maketrans('', '', string.punctuation)).strip().lower().split()
            queries.append(lineList)
    
    timeForLinearSearchOnQueries = []
    timeForBinarySearchOnQueries = []
    timeForGallopingSearchOnQueries = []
    
    sortedLengthQueries = {}
    for query in queries:
        l = len(query)
        if l in sortedLengthQueries:
            sortedLengthQueries[l].append(query)
        else:
            sortedLengthQueries[l] = [query]
    lengths = sorted(sortedLengthQueries.keys())
    for length in lengths:
        givenQueries = sortedLengthQueries[length]
        givenQueriesLength = len(givenQueries)

        print("\n\n *************************** For Linear Search with queries length %d ***************************" %length)
        start = time.time()
        for eq in givenQueries:
            getPhraseSearch(eq , invertedIndex , docsToIds , 1)
        stop = time.time()
        timeDiff = stop-start
        timeDiff /= givenQueriesLength

        timeForLinearSearchOnQueries.append(timeDiff)

        print("\n\n *************************** For Binary Search with queries length %d ***************************" %length)
        start = time.time()
        for eq in givenQueries:
            getPhraseSearch(eq , invertedIndex , docsToIds , 2)
        stop = time.time()
        timeDiff = stop-start
        timeDiff /= givenQueriesLength
        timeForBinarySearchOnQueries.append(timeDiff)

        print("\n\n *************************** For Galloping Search with queries length %d ***************************" %length)
        start = time.time()
        for eq in givenQueries:
            getPhraseSearch(eq , invertedIndex , docsToIds , 3)
        stop = time.time()
        timeDiff = stop-start
        timeDiff /= givenQueriesLength
        timeForGallopingSearchOnQueries.append(timeDiff)

    plt.title('Response Time VS Length of Queries')
    plt.plot(lengths , timeForGallopingSearchOnQueries ,color='red')
    plt.plot(lengths , timeForBinarySearchOnQueries ,color='blue')
    plt.plot(lengths , timeForLinearSearchOnQueries,color='green')


    plt.savefig('ComparisionAll.png', dpi=300, bbox_inches='tight')

    plt.show()


    max_len_post_list = list()
    response_time_linear = list()
    response_time_binary = list()
    response_time_galloping = list()
    twoQueries = ['This is','so free']
    for query in twoQueries:
        query = query.strip().lower().split()
        longest_posting_list1 = max([ len(document) for document in invertedIndex[query[0]].values()])
        longest_posting_list2 = max([ len(document) for document in invertedIndex[query[1]].values()])

        longest_posting_list = max(longest_posting_list2,longest_posting_list1)
        max_len_post_list.append(longest_posting_list)

        print("\n\n *************************** For Linear Search with queries length 2 ***************************")
        start = time.time()
        getPhraseSearch(eq , invertedIndex , docsToIds , 1)
        end = time.time()
        response_time_linear.append(end-start)

        print("\n\n *************************** For Binary Search with queries length 2 ***************************")
        start = time.time()
        result = getPhraseSearch(eq , invertedIndex , docsToIds , 2)
        end = time.time()
        response_time_binary.append(end-start)
        

        print("\n\n *************************** For Galloping Search with queries length 2 ***************************")
        start = time.time()
        result = getPhraseSearch(eq , invertedIndex , docsToIds , 3)
        end = time.time()
        response_time_galloping.append(end-start)
        

    print("Length of Posting List: ",max_len_post_list)
    print("Response Time Linear: ",response_time_linear)
    print("Response Time Binary: ",response_time_binary)
    print("Response Time Galloping: ",response_time_galloping)
    plt.title("Phrase Length of 2: Length of Posting list vs Response Time")
    plt.plot(max_len_post_list,response_time_linear,color='blue')
    plt.plot(max_len_post_list,response_time_binary,color='green')
    plt.plot(max_len_post_list,response_time_galloping,color='red')

    plt.savefig('twoQueries.png', dpi=300, bbox_inches='tight')
    plt.show()




def main():

    print("Assignment 3 of Information Retrieval ")

    sortedWords , invertedIndex , docIDToFiles = makeInvertedIndex()
    saveInvertedIndex(invertedIndex)
    GenerateQueries()
    drawPlot(invertedIndex , docIDToFiles)



if __name__=='__main__':
    main()