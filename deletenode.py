def deleteKey(head_ref, key):
  
    
    temp = head_ref
    prev = None
  
    while (temp != None and temp.data == key):
        head_ref = temp.next  
        temp = head_ref         
  
    
    while (temp != None):
  
     
        while (temp != None and temp.data != key):
            prev = temp
            temp = temp.next
  

        if (temp == None):
            return head_ref
  
       
        prev.next = temp.next
  
        
        temp = prev.next
    return head_ref