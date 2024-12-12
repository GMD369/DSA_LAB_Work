from HashTable import HashTable

def word_counter(filepath):
    hashTable=HashTable(128)
    with open(filepath, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                current_count=hashTable.search_key(word)
                hashTable.update_key(word,1 if current_count==0 else 1)

        for i in range(hashTable.HashTable_size()):
            for node in hashTable.table[i]:
                if node:
                    print(f"{node.key}:{node.value}")


filepath='word.txt'
word_counter(filepath)