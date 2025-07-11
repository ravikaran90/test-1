def twosum(arr,target):
    diction={}
    for i in range(len(nums)):
        compl=abs(target-nums[i])
        if compl in diction:
            return [diction[compl],i]
        diction[nums[i]]=i

def main():
    arr=[1,3,7,8,10,15]
    target=25
    indices=twosum(arr,target)
    print("Indices:",indices)

if __name__=="__main__":
    main()
