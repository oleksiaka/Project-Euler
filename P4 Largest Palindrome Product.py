# Finds the largest palindrome made from the product of 2 x digit numbers

def Palindrome(x):
    LargestPalindrome = 0
    for i in range(10**(x-1),10**x):
        for j in range(10**(x-1),10**x):
            product = str(i * j)
            
            if len(product) % 2 == 0:
                half = len(product) / 2
                half = int(half)
                x1 = product[0:half]
                x2 = product[half:len(product)]
                x3 = x2[::-1]

                if x1 == x3:
                    if int(product) > LargestPalindrome:
                        LargestPalindrome = int(product)

    return LargestPalindrome           
                
print(Palindrome(3))       
