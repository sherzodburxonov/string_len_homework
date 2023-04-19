def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    x=len(s)
    index=x//2
    if x%2==1:
        f=s[index]
    else :
        f=s[index-1: index+1]
    return f
print(main("cool"))