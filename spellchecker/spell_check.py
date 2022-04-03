# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:36:29 2022

@author: diego
"""

from threading import Thread
from time import perf_counter
import textblob

def spellCheck(fileName):
    
    print('Start Checking...')
    #Using for loop
    count = 0
    
    with open(fileName) as file:
    
        for line in file:
            count += 1
            ArrWords = line.split()
            
            for word in ArrWords:
                word.lower()
                # print(word)
                w = textblob.TextBlob(word)
                w2 = w.correct()
                if w != w2:
                    print('Line{}: original Word {} - Suggested Word: {}'.format(count, w, w2))
    
    print('Checking completed')
    
    
start = perf_counter()

#Create the Threads
doc1 = Thread(target=spellCheck('textForTest.txt'))
doc2 = Thread(target=spellCheck('textForTestv2.txt'))

#start the Threads
doc1.start()
doc2.start()

#wait for the threads to complete
doc1.join()
doc2.join()

# with open('textForTest.txt') as file:
#     spellCheck(file)
# with open('textForTestv2.txt') as file:
#     spellCheck(file)
    
end = perf_counter()
# print('{} time consumed'.format(end-start) )
print(f'It took {end- start: 0.2f} second(s) to complete.')
                
       

