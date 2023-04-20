#1. feladat

import unicodedata

input_list = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

users = []

for name in input_list:
    user = {
        'name': name,
        'email': name[1].lower() + '.' + name[0].lower() + '@company.hu',
        'password': name[0] + '123Start'
    }
    users.append(user)

print(users)

users.sort(key=lambda x: x['name'])

with open('nevek.txt', 'w') as file:
    for user in users:
        full_name = ' '.join(user['name'])
        email = ''.join(c
                        for c in unicodedata.normalize('NFKD', user['email'])
                        if not unicodedata.combining(c))
        password = user['name'][0] + '123Start'
        file.write(f'{full_name} {email} {password}\n')


#2.1 feladat
class Counter:

    def __init__(self, value=0, step=1):
        self._value = value
        self._step = step

    def increment(self):
        self._value += self._step

    def decrement(self):
        self._value -= self._step

    def set_value(self, value):
        self._value = value

    def set_step(self, step):
        self._step = step

    def get_value(self):
        print(self._value)


myCounter = Counter(10)
myCounter.increment()
myCounter.increment()
myCounter.get_value()
myCounter.set_step(5)
myCounter.decrement()
myCounter.get_value()
myCounter.set_value(100)
myCounter.increment()
myCounter.get_value()


#2.2 feladat
class ScoreCounter(Counter):

    def __init__(self, name, age, value=0, step=1):
        super().__init__(value, step)
        self.name = name
        self.age = age
        self.winner = False

    def increment(self):
        super().increment()
        if self._value >= 12:
            self.winner = True


myScoreCounter = ScoreCounter(34, 'Zsolt', 10)
myScoreCounter.increment()
myScoreCounter.get_value()
myScoreCounter.increment()
myScoreCounter.get_value()
print(myScoreCounter.winner)
