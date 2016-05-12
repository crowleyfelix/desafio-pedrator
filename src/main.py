from util import Util
from pedrator_word import PedratorWord

"""
- Contar preposições
- Contar verbos
- Contar verbos na primeira pessoa
- Listar todas as palavras distintas e ordenar pelo alfabeto pedrator
- Contar números bonitos distintos
- Contar números lindos distintos

"""

file = open("pedrator.txt") #arquivo texto em pedrator
log = open("log.txt",'w')

txt = file.readlines() #texto em pedrator

pedrator_words = Util.list_words(txt)

pw = PedratorWord()

c_prepositions = c_verbs = c_verbsfirstperson = 0

for x in pedrator_words:

    if pw.is_preposition(x):
        c_prepositions += 1
    else:
        verb, fperson = pw.is_verb(x)
     
        if verb:
            c_verbs +=1

            if fperson:
                c_verbsfirstperson +=1 


Util.distinct(pedrator_words)
pw.sort(pedrator_words)  

c_prettys = c_gorgeous = 0

for x in pedrator_words:
    
  if pw.is_pretty(x):
      c_prettys += 1
  
  if pw.is_gorgeous(x):
      c_gorgeous +=1

log.writelines("Preposições: {0}\n".format(c_prepositions))
log.writelines("\nVerbos: {0}\n".format(c_verbs))
log.writelines("\nVerbos em primeira pessoa: {0}\n".format(c_verbsfirstperson)   )
log.writelines("\nBonitos: {0}\n".format(c_prettys))
log.writelines("\nLindos: {0}\n".format(c_gorgeous))
log.writelines("\nVocabulário:\n")
       
for x in pedrator_words:
  log.writelines("{0} \n".format(x))

log.close()


