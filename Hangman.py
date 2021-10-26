import random
from collections import Counter
  
someWords = '''appel banaan mango aardbei 
sinasappel druiven watermeloen papaya'''
  
someWords = someWords.split(' ')

word = random.choice(someWords)         
  
if __name__ == '__main__':
    print('Gok het woord, HINT: het is een fruit.')
      
    for i in word:
         
        print('_', end = ' ')        
    print()
  
    playing = True
     
    letterGuessed = ''                
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0: 
            print()
            chances -= 1
            print(f"kansen: {chances}")
  
            try:
                guess = str(input('Type letter om te proberen: '))
            except:
                print('Enter only a letter!')
                continue
  
            
            if not guess.isalpha():
                print('Schrijf alleen 1 letter')
                continue
            elif len(guess) > 1:
                print('Schrijf alleen ÉÉN letter')
                continue
            elif guess in letterGuessed:
                print('Je hebt dit letter al ingetypt.')
                continue
  
  
           
            if guess in word:
                k = word.count(guess) 
                for _ in range(k):    
                    letterGuessed += guess 
  
            
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end = ' ')
                    correct += 1
                
                elif (Counter(letterGuessed) == Counter(word)):  
                                                                
                    print("Het word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Gefeliciteerd, Je wint!')
                    break 
                    break 
                else:
                    print('_', end = ' ')
  
              
  
        # If user has used all of his chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('Jammer genoeg heb je verloren, probeer opniew...')
            print('het woord was {}'.format(word))
  
    except KeyboardInterrupt:
        print()
        print('Doei.')
        exit()