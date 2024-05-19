from model.bl.person_bl import PersonBl
from model.entity.person import Person
from model.tools.decorators import exception_handling


class PersonController:
    @staticmethod
    @exception_handling
    def save(name, family, status=True):
        person = Person(None, name, family, status)
        return True, PersonBl.save(person)

    @staticmethod
    @exception_handling
    def edit(id, name, family, status=True):
        person = Person(id, name, family, status)
        return True, PersonBl.edit(person)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, PersonBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, PersonBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, PersonBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_family(family):
        return True, PersonBl.find_by_family(family)
