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
        if self.n > len(self.data):  
            self.n = len(self.data) 
        result = ""
        i = 0
        
        if self.counter < len(self.data):
            for record in self.data.values():  
                if i < self.counter//self.n * self.n:  # Щоб ітератор кожен раз видавав нові записи, не знайшла нічого кращого,
                    i += 1                             # ніж запустити пустий цикл стільки разів, скільки записів вже видано. 
                    continue                           # Прошу поради, як це зробити культурно саме зі словником.
                result += str(record)
                self.counter += 1
                if not self.counter % self.n:  
                    return result
                elif self.counter == len(self.data):  
                    return result
        else: 
            raise StopIteration
            
     
    def __iter__(self):
        return self
    
    
                    

            
        
    
    
        
    