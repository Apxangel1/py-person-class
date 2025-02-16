class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = []

    for person in people:
        classy_person = Person(person["name"], person["age"])

        if (("wife" in person)
                and (person["wife"] is not None)
                and (person["wife"] in classy_person.people)):

            classy_person.wife = classy_person.people[person["wife"]]
            Person.people[person["wife"]].husband = classy_person

        elif (("husband" in person)
              and (person["husband"] is not None)
              and (person["husband"] in classy_person.people)):

            classy_person.husband = classy_person.people[person["husband"]]
            Person.people[person["husband"]].wife = classy_person

        persons_list.append(classy_person)

    return persons_list
