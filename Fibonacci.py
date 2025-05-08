from time import time
from functools import lru_cache

class Fibonacci:


#questo è il metodo
    def calcola_elemento(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.calcola_elemento(n-1)+self.calcola_elemento(n-2)
#metodo con la cache per non calcolare 3000 volte la stessa cosa... fibonacci(2) per esempio
#verrà calcolato sia nel termine a sx che a dx... abbiamo bisogno di una cache

    def __init__(self):
        self.cache = {
            0: 0, #se ho 0 = il risultato è 0
            1: 1 #se ho 1 il risultato è 1
        } #dizionario che inizializiamo con 2 risultati

    def calcola_elemento_cache(self, n):
        if self.cache.get(n) is not None: #se n è presente nella cash returna il valore che sta nella cache
            return self.cache[n]
        else:#altrimenti devo calcolare il risultato e metterlo nella cache
            self.cache[n] = (self.calcola_elemento_cache(n-1) +
                             self.calcola_elemento_cache(n - 2))
            return self.cache[n]

#alternativa che riassume tutta la cosa sopra
    @lru_cache(maxsize=None)
    def calcola_elemento_lru(self,n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return (self.calcola_elemento_lru(n-1)+
                    self.calcola_elemento_lru(n-2))

if __name__ == '__main__':
    fib = Fibonacci() #se sei fuori dalla classe la devi inizializzare per poi usare i suoi metodi
    # start_time = time()
    # print(fib.calcola_elemento(40))
    # end_time = time()
    # print(f"Elapsed time: {end_time-start_time}")
    #
    # start_time = time()
    # print(fib.calcola_elemento_cache(40))
    # end_time = time()
    # print(f"Elapsed time cache: {end_time - start_time}")

    start_time = time()
    print(fib.calcola_elemento_lru(40))
    end_time = time()
    print(f"Elapsed time lru: {end_time - start_time}")