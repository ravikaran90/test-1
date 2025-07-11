def twosum(arr,target):
    diction={}
    for i in range(len(arr)):
        compl=abs(target-arr[i])
        if compl in diction:
            return [diction[compl],i]
        diction[arr[i]]=i

def main():
    arr=[1,2,7,8,10,15]
    target=12
    indices=twosum(arr,target)
    print("Indices:",indices)

if __name__=="__main__":
    main()
