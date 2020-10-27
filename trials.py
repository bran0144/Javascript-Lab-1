"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_numbers = []

    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers


def get_odd_indices(items):
    indices_nums=[]

    for item in items:
        index= items.index(item)

        if index%2 !=0:
            indices_nums.append(item)
    return indices_nums



def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f'{i}. {item}')
        i += 1


def get_range(start, stop):
    const_nums = []
    x=range(start,stop-1)

    for i in x:
        const_nums.append(i)
    return const_nums


def censor_vowels(word):
    
    no_vowels = ""

    for letter in word:
        if letter in 'aeiou':
            letter ='*'
        no_vowels=no_vowels + "" +letter
    return no_vowels


# def snake_to_camel(string):
#     camel_case = ""
#     lst = string.split('_')
#     for item in lst:
#         camel_case= camel_case+ "" + item[0].upper()+""+item[1,len(item)-1]
   
#     return camel_case
        
def snake_to_camel(string):
    camelcase = ""
    lst = string.split('')

    for word in lst:

        word2=word.replace(word[0],word[0].upper())
        camel_case+=word2

    return camel_case



def longest_word_length(words):
    longest = len(words[0])
    
    for word in words:
        if longest <len(word):
            longest=len(word)
          
    return longest    
        

def truncate(string):
    result = ""
    last=string(len(string)-1)

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            result=result+(string[i])
     
            
    return f'{result}{last}'




#  for (const char of string) {
#     if (result.length === 0 || char !== result[result.length - 1]) {
#       result.push(char);
#     }
#   }

def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code


items=[5,8,2,12,5]
# output_all_items(items)

# print(get_all_evens(items))

# print(get_odd_indices(items))
# print_as_numbered_list(items)
# print(get_range(1, 6))
# print(censor_vowels("Hello World"))
# print(snake_to_camel("Hello World"))
# print(longest_word_length(["hello","hi","g","worlddd"]))
print(truncate("aaaabbbbccdda"))

