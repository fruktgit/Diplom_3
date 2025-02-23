from faker import Faker


def generate_user_data():
    fake = Faker()
    return {
        "email": fake.email(),
        "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
        "name": fake.name()
    }

