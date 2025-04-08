"""
Implementación básica de un Filtro de Bloom.
Esta implementación utiliza múltiples funciones hash simples para determinar la existencia de un elemento.
"""

import math
import mmh3  # Asegúrate de instalarlo con "pip install mmh3"

class BloomFilter:
    def __init__(self, items_count, fp_prob):
        """
        items_count: cantidad estimada de elementos a almacenar.
        fp_prob: probabilidad deseada de falsos positivos.
        """
        self.size = self.get_size(items_count, fp_prob)
        self.hash_count = self.get_hash_count(self.size, items_count)
        self.bit_array = [0] * self.size

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1

    def check(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

    @staticmethod
    def get_size(n, p):
        """
        n : int - número de elementos
        p : float - probabilidad de falsos positivos
        return: tamaño de la bit array
        """
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)

    @staticmethod
    def get_hash_count(m, n):
        """
        m : int - tamaño de la bit array
        n : int - número de elementos
        return: cantidad de funciones hash necesarias
        """
        k = (m/n) * math.log(2)
        return int(k)
