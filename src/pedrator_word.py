from util import Util
class PedratorWord(object):

    ALPHABET = "qwtrbnvmczspkjgxdflh"

    LOVE_LETTERS = "wtpj"

    PASSION_LETTERS = "qrbnvmczskgxdflh"

    def is_preposition(self,word):
           
            if len(word) > 3:
                return False
    
            if word.count('h') > 0:
                return False

            for letter in self.LOVE_LETTERS:
                if word.endswith(letter):
                    return True
                
    def is_verb(self,word):
        
        verb = False
        first_person = False

        if len(word) >= 6:
                    
            for letter in self.PASSION_LETTERS:
                if word.endswith(letter):
                    verb = True
                    break

            for letter in self.LOVE_LETTERS:
                if word.startswith(letter):
                    first_person = True
                    break

        return (verb,first_person)

    def is_pretty(self,word):
        
        value = self.calculate(word)

        if value >= 623732 and value % 4 == 0:
            return True
        else: 
            return False

    def is_gorgeous(self,word):
        
        value = self.calculate(word)

        sum_digits = 0

        for x in str(value):
            sum_digits += int(x)

        return Util.is_prime_number(sum_digits)

    def sort(self,list):
              
        for x in range(len(list)):
            
            under = list[x] #apontando para o menor

            idx_under = x
            
            for y in range(x+1,len(list)):
                
                word_comp = list[y] #palavra a ser comparada

                for z in range(len(under)): 
                    
                    #Percorrendo letras
                    #Não permitir exceder o índice da palavra à ser comparada
                    
                    if self.letter_evaluator(word_comp[z]) == self.letter_evaluator(under[z]) and not z+1 == len(word_comp):
                        continue
                    
                    #Regras de ordenação

                    #Se a letra de word_comp for menor que under
                    if self.letter_evaluator(word_comp[z]) < self.letter_evaluator(under[z]):
                        under = word_comp
                        idx_under = y

                    #Se as letras foram iguais, estiver na ultima letra e a largura de word_comp for menor que under
                    if self.letter_evaluator(word_comp[z]) == self.letter_evaluator(under[z])  and \
                        (z+1 == len(word_comp) and len(word_comp) < len(under) ): 
                        
                        under = word_comp
                        idx_under = y
                     
                    break   
             
            temp = list[x]

            list[x] = list[idx_under]

            list[idx_under] = temp
            
    def calculate(self,word):
        total = 0
        digit_position = 0

        for x in word:
              
            total += self.letter_evaluator(x) * (20 ** digit_position)

            digit_position += 1

        return total
        
    def letter_evaluator(self,letter):
        return self.ALPHABET.find(letter)