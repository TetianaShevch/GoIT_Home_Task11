from address_book_class import AddressBook
from record_class import Record
from name_class import Name
from phone_class import Phone
from birthday_class import BirthDay


if __name__ == "__main__":
    
    ab = AddressBook()
    print('Name1')
    name1 = Name('Bill')
    phone1 = Phone('+3805012345670')
    birthday1 = BirthDay('21.07.1970')
    rec1 = Record(name1, phone1, birthday1)
    ab.add_record(rec1)
    assert isinstance(ab['Bill'].birthday, BirthDay)
    print(f"The {rec1.name}'s birthday will be after {rec1.days_to_birthday()} days")
        
    print('Name2')
    name2 = Name('Mary')
    # phone2 = Phone('05023456709')
    birthday2 = BirthDay('12.12.2003')
    rec2 = Record(name2, birthday=birthday2)
    ab.add_record(rec2)
    print(f"The {rec2.name}'s birthday will be after {rec2.days_to_birthday()} days")

    print('Name3')
    name3 = Name('John')
    phone3 = Phone('05023456709')
    birthday3 = BirthDay('28.08.2003')
    rec3 = Record(name3, phone3, birthday=birthday3)
    ab.add_record(rec3)
    new_phone3 = Phone('0976543645')
    rec3.add_phone(new_phone3)
    print(f"The {rec3.name}'s birthday will be after {rec3.days_to_birthday()} days")

    print('Name4')
    rec4 = Record(Name('Mike'), Phone('+380671233434'))
    ab.add_record(rec4)
    print(f"The {rec4.name}'s birthday will be after {rec4.days_to_birthday()} days")

    print('Name5')
    rec5 = Record(Name('Tom'), BirthDay('02.09.2018'))
    ab.add_record(rec4)
    new_phone5 = Phone('+380885436456')
    rec5.add_phone(new_phone5)
    print(f"The {rec4.name}'s birthday will be after {rec4.days_to_birthday()} days")
    
    # print('Name5')
    # name5 = Name('')
    # phone5 = Phone('1234567890')
    # birthday5 = BirthDay('27082003')
    # rec5 = Record(name5, phone5)
    # ab.add_record(rec5)
    # new_phone = Phone('789')
    # rec5.add_phone(new_phone)

    for i in ab:
        print(i)
        input('Press the button for continue')
    
   
    

    # new_phone = Phone('5778890')
    # rec.add_phone(new_phone)
    # mistaken_phone = Phone('789000')
    # rec.del_phone(mistaken_phone)
    # rec.del_phone(new_phone)
    # rec.add_phone(mistaken_phone)
    # rec.change_phone(mistaken_phone,new_phone)
