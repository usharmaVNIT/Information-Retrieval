# UJJWAL SHARMA
# BT18CSE021
# usharma@students.vnit.ac.in



def computePiArray(pattern):
    length = 0 # length of the previous longest prefix suffix
    # Longest prefix suffix -> lps = piArray
    piArray = [0]*len(pattern)
    piArray[0] = 0 # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < len(pattern):
        if pattern[i]== pattern[length]:
            length += 1
            piArray[i] = length
            i += 1
        else:
            if length != 0:
                length = piArray[length-1]

                # Also, note that we do not increment i here
            else:
                piArray[i] = 0
                i += 1
    return piArray





def KMPAlgorithm(pattern, text):

    # Preprocess the pattern (calculate lps[] array)
    piArray = computePiArray(pattern)
    print(piArray)

    i = 0 # index for txt[]
    j = 0
    ans = []
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            ans.append(i-j)
            j = piArray[j-1]

        # mismatch after j matches
        elif i < len(text) and pattern[j] != text[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = piArray[j-1]
            else:
                i += 1
    return ans


def main():
    text = input("Enter Text : ")
    pattern = input("Enter Pattern : ")
    # print(text)
    # print(pattern)
    ans = KMPAlgorithm(pattern , text)
    if len(ans)==0:
        print("Does not found a match")
        return 0
    for i in ans:
        print("Pattern found at %d index" %i)
        print("\t",*text , '   <-- Text ')
        spaces = ' '*i + pattern
        print('\t',*spaces , '   <-- Pattern')
    return 0

if __name__ == "__main__":
    main()
