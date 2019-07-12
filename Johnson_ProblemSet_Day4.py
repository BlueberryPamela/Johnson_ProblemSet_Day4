# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:54:22 2019

@author: Tim
"""

import os
os.chdir('C:\\Users\\Tim\\Documents\\511_Exercise')


# ('cherbonnel-mi-tio_SP.txt','schloemp-tolle-koffer_DE.txt','eaton-boy-scouts_EN.txt', 'unknown-lang.txt')


def frequency_eval(language_file):
    with open(language_file, encoding='utf-8') as f:
        content = f.read()
    language = content.split()
    total_words = len(language)

    List = []
    for word in language:
        x = word.lower().strip("...--'¡¿^?!@#$+-*&")
        List.append(x)

    frequency = {}
    for word in List:
        if not word in frequency:
            frequency[word] = 0
        frequency[word] += 1

    for word in frequency.keys():
        frequency[word] = frequency[word]/total_words
    sorted_counts = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)
    most_frequent = dict(sorted_counts[:11])
    return(most_frequent)

print('Spanish\n', frequency_eval('cherbonnel-mi-tio_SP.txt'))
print('German\n', frequency_eval('schloemp-tolle-koffer_DE.txt'))
print('English\n', frequency_eval('eaton-boy-scouts_EN.txt'))
print('Unknown\n', frequency_eval('unknown-lang.txt',))

Spanish_table = (frequency_eval('cherbonnel-mi-tio_SP.txt'))
German_table = (frequency_eval('schloemp-tolle-koffer_DE.txt'))
English_table = (frequency_eval('eaton-boy-scouts_EN.txt'))
Unknown_table = (frequency_eval('unknown-lang.txt'))

s = 0
for word in Unknown_table.keys():
    ResultSPA = Spanish_table.get(word, 0)
    ResultUNK = Unknown_table.get(word, 0)
    OutSPA = abs(ResultSPA - ResultUNK)
    s = OutSPA + s
print(s)

g = 0
for word in Unknown_table.keys():    
    ResultGER = German_table.get(word, 0)
    OutGER = abs(ResultGER - ResultUNK)
    g = OutGER + g
print(g)    

e = 0
for word in Unknown_table.keys(): 
    ResultENG = English_table.get(word, 0)
    OutENG = abs(ResultENG - ResultUNK)
    e = OutENG + e

print('This is the difference between those sets:')
print(s, g, e)



#print('This is the difference:')
#print('Spanish', abs(OutSPA-ResultUNK))
#print('German', abs(OutGER-ResultUNK))
#print('English', abs(OutENG-ResultUNK))

#Spanish = abs(OutSPA-ResultUNK)
#German = abs(OutGER-ResultUNK)
#English = abs(OutENG-ResultUNK)
 
#for percentage in Spanish_table.values():
    #Spanish_percentages = percentage
    #print("Spanish percentages", percentage)

#for percentage in Unknown_table.values():
    #Unknown_percentages = percentage
   # print("Unknown percentages", percentage)

#for percentage in English_table.values():
    #English_percentages = percentage
    #print("Spanish percentages", percentage)
    
#for percentage in German_table.values():
    #German_percentages = percentage
    #print("Spanish percentages", percentage)
    
#DifferenceSPA = abs(Spanish_percentages - Unknown_percentages)
#print("Spanish difference:", DifferenceSPA)

#DifferenceENG = abs(English_percentages - Unknown_percentages)
#print("English difference:", DifferenceENG)

#DifferenceGER = abs(German_percentages - Unknown_percentages)
#print("German difference:", DifferenceGER)