class Util(object):

    def distinct(list):

        max_length = len(list)

        x = y = 0

        while (x < max_length): #percorrer palavras
    
            y = x+1 #verificar a partir do proximo

            while (y < max_length): #percorrer palavras para comparação            

                if list[x] == list[y]: 
            
                    del list[y] #retirar copia
                    y+=-1
                    max_length +=-1
        
                y +=1
                
            x += 1 

    def list_words(txt):

        all_words = [] #lista de palavras do texto

        #Lendo todas palavras
        for line in txt:
            for word in str(line).split(" "):
                all_words.append(str(word).strip())

        return all_words

    def is_prime_number(number):
        
        dividers = 0

        for x in range(1,number+1):

            if(number % x == 0):
                dividers+=1

        if dividers > 2:
            return False
        else:
            return True    