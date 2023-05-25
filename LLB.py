def binary_search(arr,target):
    low=0
    high=len(arr)-1
    
    while(low<=high):
        mid=(low+high)//2
        
        if arr[mid]==target:
            return mid
        
        
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
            
            
            #example
            
            arr=input("enter the sorted array").split()
            arr=[int(num) for num in arr]
        
            target=int(input("enter the sorted number"))
            result=binary_search(arr,target)
                 
if result!= -1:
                 print("element found")
else:
                 print("element not found")
                 
                             
     
  
