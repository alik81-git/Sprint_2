class Employee:
    hourly_payment = 400  # Переменная класса для почасовой оплаты

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, hours=None, email=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)  # Возвращаем экземпляр класса

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)  # Возвращаем экземпляр класса

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment  # Изменяем переменную класса

    def salary(self):
        return self.hours * self.hourly_payment


# Пример использования
employee1 = Employee("Иван", hours=40)
print(f"Зарплата {employee1.name}: {employee1.salary()}")  # Вывод: Зарплата Иван: 16000

employee2 = Employee.get_hours("Петр", rest_days=2)
print(f"Зарплата {employee2.name}: {employee2.salary()}")  # Вывод: Зарплата Петр: 20000 (потому что hours = (7 - 2) * 8 = 40)

employee3 = Employee.get_email("Анна")
print(f"Email {employee3.name}: {employee3.email}")  # Вывод: Email Анна: Анна@email.com

Employee.set_hourly_payment(500)
print(f"Новая почасовая оплата: {Employee.hourly_payment}")  # Вывод: Новая почасовая оплата: 500

print(f"Зарплата {employee1.name} после изменения почасовой оплаты: {employee1.salary()}") # Вывод: Зарплата Иван после изменения почасовой оплаты: 20000
