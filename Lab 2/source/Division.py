# Consider numbers in the range of [1500, 2700]
for nums in range(1500,2700):
    # Numbers required from the resultant range should be divisible by 7 and 5
    if(nums% 7==0 and nums%5==0):
        # print the resultant output
        print(nums)
