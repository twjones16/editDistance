from typing import Tuple, List


def edit_distance(s:str, t:str) -> int:
    def distance(i:int, j:int) -> int:
        if i == 0: return j  # distance(0, j) = j
        if j == 0: return i  # distance(i, 0) = i

        return min(
            1 + distance(i - 1, j - 1) if s[i-1] != t[j-1]
                                       else distance(i-1, j-1),
            1 + distance(i-1, j),  # delete
            1 + distance(i, j-1)   # insert
        )
    return distance(len(s), len(t))

from typing import List
def edit_distance_dp(s: str, t: str) -> List[List[int]]:
    dist = [[0] * (len(t) + 1) for _ in range(len(s)+1)]

    # fill in top row
    for j in range(len(t)+1): dist[0][j] = j

    # fill in left column
    for i in range(len(s)+1): dist[i][0] = i

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            dist[i][j] = \
            min(
                    1 + dist[i - 1][j - 1] if s[i-1] != t[j-1]
                                           else dist[i-1][j-1],
                    1 + dist[i-1][j],  # delete
                    1 + dist[i][j-1]   # insert
                )

    return dist


def align(s: str, t:str) -> Tuple[str,str,str]:

    def align(i: int, j: int, sa:str, ta:str, changes: str) -> Tuple[str,str,str]:

        edit = dist[i - 1][j - 1]
        delete = dist[i - 1][j]
        insert = dist[i][j - 1]
        minimum = min(insert, delete, edit)
        if  i ==0 or j ==0 :  # base case
            if i ==0 and j ==0 : # t and s are the same size
                return sa, ta, changes
            elif i>0 and j==0: # there are no more chacters in t, the strings are different lengths
                return s[:i] + sa, '-' * i + ta, ' ' * i + changes
            else: #there are no more characters in s
                return '-' * j + sa, t[:j] + ta, ' ' * j + changes
        #from a position i,j on the table if the minimum value is at i-1, j-1
        if edit == minimum:
            #add letters at that index
            sa = s[i - 1] + sa
            ta = t[j - 1] + ta
            #if the diagonal is the same
            if minimum == dist[i][j]: #characters are the same
                changes = ' ' + changes #no changes to show in changes string
            else: #diagonal is not the same so switch must be made
                changes = '*' + changes #add asterix to changes string
            return align(i - 1, j - 1, sa, ta, changes) #call function on new location
        elif delete == minimum:
            # make changes to sa and ta
            sa = s[i - 1] + sa
            ta = '-' + ta
            changes = ' ' + changes
            return align(i - 1, j, sa, ta, changes) #call function on new location
        else: #must be an insert
            #make changes to sa and ta
            sa = '-' + sa
            ta = t[j - 1] + ta
            changes = ' ' + changes
            return align(i, j - 1, sa, ta, changes)#call function on new location

    dist = edit_distance_dp(s, t)
    return align(len(s), len(t), "", "", "")


if __name__ == "__main__":

    #edit distance for repeal and treat
     list = (align("repeal", "treat"))
     print(list[0])
     print(list[1])
     print(list[2])

     print(" ")
    # edit distance for hipopotomoose  hippopotamus
     list2 = (align("hipopotomoose", "hippopotamus"))
     print(list2[0])
     print(list2[1])
     print(list2[2])
    
     print("")
    # edit distance for exponential  polynomial
     list3 = (align("exponential", "polynomial"))
     print(list3[0])
     print(list3[1])
     print(list3[2])





