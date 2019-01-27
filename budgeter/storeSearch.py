def findStore(listOfStores,whatToFind):
    return findStoreHelper(listOfStores,0,len(listOfStores),whatToFind)
    
def findStoreHelper(myList,left,right, x):
    if(right>=left):
        mid=int(left + (right - left)/2)
        
        if x==myList[mid]:
            return True
        
        elif x>myList[mid] :
                return findStoreHelper(myList,mid+1,right,x)

        elif x<myList[mid]:
            return findStoreHelper(myList,left,mid-1,x)
        
    else:
        return False

'''
Test
arr=[1,2,3,45,6,7,8]
j=findStore(arr,0,len(arr),4);
print(j)

arr=[1,2,3,45,6,7,8]
j=findStore(arr,0,len(arr),45);
print(j)
'''



arr=[9,12,3,45,6,17,8]

x=findStore(arr,44)
print(x)


        
