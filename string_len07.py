def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    if len(s1)%2==1:
        a=s1
    else :
        a=""
    if len(s2)%2==1:
        b=s2
    else:
        b=""
    if len(s3)%2==1:
        c=s3
    else :
        c=""
    return "["+a+b+c+"]"
print(main("codes"," python"," coder"))