'''
Definējiet operatoram [] atbilstošās metodes __getitem__() un __setitem__()
'''

class Polinom:
    def __init__(self, koefic = None, karta = None):
        if koefic != None:
             self.koefic = koefic
        elif koefic == None and karta != None:
             self.koefic = [1] * (karta + 1)
        else:
            self.koefic = []
        
    def __set__item(self, index, value):
        self.koef[index] = value
 
    def __get__item(self, index):
        return self.koef[index]

    def __str__(self):
        return str([str(el) for el in self.koefic])
    
    def str_pol(self):
        karta = len(self.koefic)
        string = ''
        for i in range(karta):
            if i != (karta - 1):
                if self.koefic[i] > 0:
                    string += '+' + str(self.koefic[i]) + 'x^' + str(karta - (i+1))
                elif self.koefic[i] < 0:
                    string += '-' + str(self.koefic[i]) + 'x^' + str(karta - (i+1))
                else:
                    continue
            else:
                string += str(self.koefic[-1])
        return string
            