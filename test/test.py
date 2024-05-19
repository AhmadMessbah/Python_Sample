from model.entity.book import Book
from model.da.da import DataAccess
from model.entity.person import Person

person_da = DataAccess(Person)
book_da = DataAccess(Book)



# book_writer = Person(None, "ahmad", "messbah")
# person_da.save(book_writer)
# print(book_writer)

# print(person_da.remove(300))
# print(book_writer.id)

person = person_da.find_by_id(2)
print(person)

book = Book(None, "Python12", person)
print(book)


book_da.save(book)
print(book)


# print(person_da.find_all())
# print(person_da.find_by_id(2))
# print(person_da.find_by(Person.id > 3))
