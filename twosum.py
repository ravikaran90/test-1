def twosum(nums,target):
    diction={}
    for i in range(len(nums)):
        compl=abs(target-nums[i])
        if compl in diction:
            return [diction[compl],i]
        diction[nums[i]]=i

def main():
    nums=[1,4,7,8,10,15]
    target=14
    indices=twosum(nums,target)
    print("Indices:",indices)

if __name__=="__main__":
    main()