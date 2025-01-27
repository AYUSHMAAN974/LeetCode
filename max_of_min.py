str=input()
arr=list(map(int,str.split()))

def find_maxofmin(window,arr):
    start=0
    end=start+window
    arr1=[]
    while(end<len(arr)+1):
        arr1.append(min(arr[start:end]))
        start=start+1
        end=start+window
    return arr1   
       
window=1
new_arr=[]
while(window<=len(arr)):
    new_arr.append(max(find_maxofmin(window,arr)))
    window+=1

print(new_arr)