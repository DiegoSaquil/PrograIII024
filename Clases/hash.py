class HashTable:
    def __init__ (self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.hash_table[index]:
            print("Colisión detectada en el índice", index)
            # Resolver la colisión
            while self.hash_table[index]:
                index = (index + 1) % self.size
                print("Corrigiendo colisión en el índice", index)
        self.hash_table[index].append((key, value))

    def display(self):
        for index, element in enumerate(self.hash_table):
            print(index, end=" ")
            if element:
                for pair in element:
                    print("-->", pair, end=" ")
            print()


def main():
    size = int(input("Ingrese el tamaño de la tabla hash: "))
    hash_table = HashTable(size)

    print("Ingrese los elementos (llave, valor):")
    for _ in range(size):
        key = int(input("Llave: "))
        value = input("Valor: ")
        hash_table.insert(key, value)

    print("\nTabla hash final:")
    hash_table.display()


if __name__ == "_main_":
    main()