from dataclasses import dataclass

@dataclass
class Record:
    id: int
    name: str
    email: str
    age: int

# Creating a record instance
record_instance = Record(id=1, name='Oporajita', email='oporajita@example.com', age=22)

# Accessing fields
print(f"ID: {record_instance.id}")
print(f"Name: {record_instance.name}")
print(f"Email: {record_instance.email}")
print(f"Age: {record_instance.age}")

# Modifying a field
record_instance.age = 23
print(f"Updated Age: {record_instance.age}")
