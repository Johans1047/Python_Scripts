"""
--- 
Data Format Problem
A company has a system that obtains all the information from its customers, it has a method to collect the data obtaining this format:
"Abel Murgas 25" Name last name Age, and the company want to change the format supported by the Database.
...
Important things:
1. Some customers have a middle name and maternal last name: "Abel Jazir Murgas Tapia 25"
2. Some customers write their first or last name in lower case: "abel jazir Murgas tapia 25"
3. Some clients do not put their age: "Abel Jazir Murgas Tapia"
The expected result:
The method must be able to change this format:
"
abel murgas tapia 25
Carmen Ortega 30
july ruiz
roberto lopez
Marta Campos" (str)
to:
[
    [1,Abel,Murgas,Tapia,25],
    [2, Carmen, Ortega, 30],
    [3, Julio, Ruiz, None],
    [4, Roberto, Lopez, None],
    [5,Marta, Campos, None]
] (list)
Validation:
1- Names and lastname must begin with a capital letter
2- If the client has no age, you must put None in the last position of the list
3- Each client must have a unique code
4- The client renders a vector inside the main list
¡Good luck!
Data example (use to test):
"""
clients_example = """Abel Murgas Tapia 25
Raul ortega martinez 10
paul Walker
martin Ruiz 100
carlos juan martinez castillo"""

result_expected = [
    ["Abel","Murgas","Tapia",25],
    ["Raul","Ortega","Martinez",10],
    ["Paul","Walker",None],
    ["Martin","Ruiz",100],
    ["Carlos","Juan","Martinez","Castillo", None]
]

def divide_sentences(clients):
    
    full_clients = clients
    phrases = full_clients.splitlines()
    
    return phrases

def divide_words(name): 
    full_name = name
    
    words = full_name.split()
    
    if not full_name[-1].isdigit() == True:
    
        words.append("None")
    
    return words
    
def capital_letter(word):
    words = word
    
    for wrd in words:# make uppercase
        
        if wrd[0].islower() == True:
        
            Upper_wrd = wrd[0].upper()
            
            wrd1 = wrd.replace(wrd[0],"")
            concatenate = Upper_wrd + wrd1
            
            words.insert(-1, concatenate)

    numbers = []
    
    for wrd in words:#take position
                
        if wrd[0].islower() == True:
            index_position = words.index(wrd)
            numbers.append(index_position)
            
    for number in range(len(numbers)):# delete leftovers
        
        del words[numbers[0]]

    return words
    
def age_verification(word):
    words = word
    
    if words[-1].isdigit() == False:
        words.append("None")
        
    if words[0] == "None":
        words.pop()
        
    if words[-1] == "None" and words[-2] == "None":
        words.pop()
        
    return words

def unique_code(word, number):
    words = word
    index_pos = number
    words.insert(0, index_pos)
    
    return words

def str_to_int(word):
    
    words = word
    
    if words[-1].isdigit() == True:
        num = words.pop()
        convert = int(num)
        words.append(convert)
        
    return words
    
def str_to_none(word):
    
    words = word
    
    if isinstance(words[-1], str) == True:
    
        del words[-1]
        convert = None
        words.append(convert)
   
    return words

clients = """
abel murgas tapia 25
Carmen Ortega 30
july ruiz
roberto lopez
Marta Campos"""

sentences = divide_sentences(clients)

sentence1 = sentences[1]
sentence2 = sentences[2]  
sentence3 = sentences[3]
sentence4 = sentences[4]
sentence5 = sentences[5]

results_expected = []

for i in range(1,6):
    
    function1 = divide_words(sentences[i])
    function2 = capital_letter(function1)
    function3 = age_verification(function2)
    function4 = unique_code(function3, i)
    function5 = str_to_int(function4)
    function6 = str_to_none(function5)
    results_expected.append(function6)
    
print(results_expected)  
    