def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=0
    while i<len(list1):
        if list1[0]==list1[i]:
            x=True
        else:
            return False
        i+=1
    
    return x
    
print(main([1,1,1,1,1]))