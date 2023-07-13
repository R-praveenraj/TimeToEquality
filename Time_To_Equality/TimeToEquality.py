#Given an integer array A of size N. In one second, you can increase the value of one element by 1.
#Find the minimum time in seconds to make all elements of the array equal

def TimeToEquality(A):
    maxi=float('-inf')
    for i in A:
        if maxi<i:
            maxi=i
    time=0
    for i in A:
        total=maxi-i
        time+=total
    return time
    


A = [2, 4, 1, 3, 2]
print(TimeToEquality(A))