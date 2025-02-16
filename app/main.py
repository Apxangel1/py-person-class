class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = []

    for person in people:
        classy_person = Person(person.get("name"), person.get("age"))

        if (person.get("wife")
                and (person.get("wife") in Person.people)):

            classy_person.wife = Person.people[person["wife"]]
            Person.people[person["wife"]].husband = classy_person

        elif (person.get("husband")
              and (person.get("husband") in Person.people)):

            classy_person.husband = Person.people[person["husband"]]
            Person.people[person["husband"]].wife = classy_person

        persons_list.append(classy_person)

    return persons_list
