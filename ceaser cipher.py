logo=""" 
                                                                               88             88                                 
                                                                               ""             88                                 
                                                                                              88                                 
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba,  ,adPPYba, 8b,dPPYba,     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" a8P_____88 88P'   "Y8    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  8PP""""""" 88            8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I "8b,   ,aa 88            "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"'  `"Ybbd8"' 88             `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                  88                                             
                                                                                  88                                             """
print(logo)
    
def caeser(text,shift,decision):
    output=""
    if decision=='decode':
        shift*=-1
    for i in text:
        if i not in alphabet:
            output+=i
        else:    
            position=alphabet.index(i)+shift
            position%=len(alphabet)
            output+=alphabet[position]    
    print(f"the {decision}d text {output}") 

condition=True
while(condition):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decision=input("-->Encode or Decode\n").lower()
    text=input("-->Enter the text\n").lower()
    shift=int(input("-->Enter the number of shifts\n"))    
    caeser(text,shift,decision)    
    resut=input("-->Enter YES to continue or NO to exit\n").lower()
    if resut=='yes':
        condition=True
    else:
        condition=False
        print("GoodBye!")    