from controller.exceptions.exceptoins import PersonNotFoundError
from model.da.da import DataAccess
from model.entity.person import Person

person_da = DataAccess(Person)


class PersonBl:
    @staticmethod
    def save(person):
        return person_da.save(person)

    @staticmethod
    def edit(person):
        if person_da.find_by_id(person.id):
            return person_da.edit(person)
        else:
            raise PersonNotFoundError()

    @staticmethod
    def remove(id):
        person = person_da.find_by_id(id)
        if person:
            return person_da.remove(person)
        else:
            raise PersonNotFoundError()

    @staticmethod
    def find_all():
        person_list = person_da.find_all()
        if person_list:
            return person_list
        else:
            raise PersonNotFoundError()

    @staticmethod
    def find_by_id(id):
        person = person_da.find_by_id(id)
        if person:
            return person
        else:
            raise PersonNotFoundError()

    @staticmethod
    def find_by_family(family):
        person_list = person_da.find_by(Person.family == family)
        if person_list:
            return person_list
        else:
            raise PersonNotFoundError()
