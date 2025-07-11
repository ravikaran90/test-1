def twosum(arr,t):
    diction={}
    for i in range(len(arr)):
        compl=abs(t-arr[i])
        if compl in diction:
            return [diction[compl],i]
        diction[arr[i]]=i

def main():
    arr=[1,2,7,8,10,15]
    t=18
    indices=twosum(arr,t)
    print("Indices:",indices)

if __name__=="__main__":
    main()
