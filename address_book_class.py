from collections import UserDict
from record_class import Record

class AddressBook(UserDict):
    def __init__(self, n = 3):
        self.counter = 0
        self.n = n
        super().__init__()
    
    def add_record(self, record = Record):
        self.data[record.name.value] = record 
        print(f'Contact of {record.name.value} was added')

    def __next__(self):
        if self.n <= 0:
            raise ValueError("Number of printed lines must be positive")
        elif self.n > len(self.data):  
            self.n = len(self.data) 
        result = ""
        print(self.counter)
        if self.counter < len(self.data):
            for record in self.data.values():  
                # while i < self.counter//self.n * self.n:
                #     print(i)
                #     continue
                result += str(record)
                self.counter += 1
                if not self.counter % self.n:  
                    print('!!!', result)
                    return result
                elif self.counter == len(self.data):  # условие для хвоста
                    print('???', result)
                    return result
        else: 
            raise StopIteration
            
     
    def __iter__(self):
        return self
    
    
                    

            
        
    
    
        
    