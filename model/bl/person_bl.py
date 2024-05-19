from model.da.da import DataAccess
from model.entity.person import Person

person_da = DataAccess(Person)


class PersonBl:
    @staticmethod
    def save(person):
        return person_da.save(person)

    @staticmethod
    def edit(person):
        return person_da.edit(person)

    @staticmethod
    def remove(id):
        return person_da.remove(id)

    @staticmethod
    def find_all():
        return person_da.find_all()

    @staticmethod
    def find_by_id(id):
        return person_da.find_by_id(id)

    @staticmethod
    def find_by_family(family):
        return person_da.find_by(Person.family == family)
