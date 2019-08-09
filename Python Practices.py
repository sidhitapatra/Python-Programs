#Write a function that computes the volume of a sphere given its radius.
def vol(s):
	return (4/3)*(22/7)*s**3
  
## Check 
vol(2)
-------------------------------------------------------------------------------

#Write a function that checks whether a number is in a given range (inclusive of high and low)

#Method 1: Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    return num in range(low, high+1)
    

ran_check(3,1,10)


#Method 2: Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num in range(low, high+1):
        print(f'{num} is in the range between {low} and {high}')


# Check
ran_check(5,2,7)

-------------------------------------------------------------------------------
#Method1: Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(d):
    up = 0
    low = 0
    e=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for x in d:
        for y in e:
            if x==y:
                up +=1
            elif x ==y.lower():
                low +=1
    print(f'Original String :  {d}')           
    print(f'No. of Upper case characters :  {up}')
    print(f'No. of Lower case Characters :  {low}')

# Check
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

#Method 2: Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(c):
    d={'upp':0, 'low':0}
    for x in c:
        if x.isupper():
            d['upp'] +=1
        elif x.islower():
            d['low'] +=1
            
    print('Original String :  {}'.format(c))           
    print('No. of Upper case characters :  {}'.format(d['upp']))
    print('No. of Lower case Characters :  {}'.format(d['low']))

# Check
s = 'Hi Adi'
up_low(s)
-------------------------------------------------------------------------------

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    return set(l)

# Check   
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

-------------------------------------------------------------------------------

#Write a Python function to multiply all the numbers in a list.
def multiply(lst):
    prod = 1
    for x in lst:
        prod *=x
    return prod
    
# Check
multiply([1,2,3,-4])
-------------------------------------------------------------------------------

#Write a Python function that checks whether a passed in string is palindrome or not.
def palindrome (s):
    return s==s[::-1]
    
# Check
palindrome('helleh')

palindrome('malayalam')

palindrome('adi')

-------------------------------------------------------------------------------
#Write a Python function to check whether a string is pangram or not.
def ispangram(str):
    a= string.ascii_lowercase
    for x in str:
        for y in a:
            if x.lower()==y:
                a=a.replace(y,"")
    return len(a)==0   

# Check
ispangram("The quick brown fox jumps over the lazy dog")

ispangram('vhgdf')






