import random
class Anna:
    def __init__(self, name='Anna',school=None, academy=None, rugby=None, cactus=None):
        self.name=Anna
        self.money=50
        self.gladness=50
        self.satiety=50
        self.school=school
        self.academy=academy
        self.rugby=rugby
        self.cactus=cactus
        self.water=100
    def get_school(self):
        self.money+=10
        self.gladness-=10
        self.satiety-=5
        self.mess+=5
    def eat(self):
        if self.satiety <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 50:
                self.satiety = 50
                return
            self.satiety += 5
            self.money -= 5
            self.mess += 5
    def shopping(self, manage):
        if manage == 'food':
                print('Купив їжу')
                self.money -= 5
                self.satiety+=10
        elif manage == 'delicacies':
                print('Ура!Смаколики')
                self.gladness += 10
                self.satiety += 2
                self.money -= 5
                self.mess += 0
    def school(self):
        self.money -= 5
        self.gladness -= 5
        self.satiety += 5
        self.mess += 0
    def academy(self):
        self.money -= 5
        self.gladness += 10
        self.satiety -= 2
        self.mess += 0
    def chill(self):
        self.money -= 2
        self.gladness += 15
        self.satiety +=5
        self.mess += 7
    def clean_room(self):
        self.money += 15
        self.gladness -=5
        self.satiety -=5
        self.mess -= 10
    def homework(self):
        self.money += 5
        self.gladness -= 5
        self.satiety -=2
        self.mess += 2
    def rugby(self):
        self.money +=10
        self.gladness +=15
        self.satiety -=10
        self.mess += 0
    def plant(self):
        if self.water > 50:
            print('Води достатньо')
        elif self.water < 50:
            print('Підляйте води')
            self.water -= 25
        elif self.water < 0:
            print('Рослинка засохла')
        self.money -= 1
        self.gladness += 3
        self.satiety -= 1
        self.mess += 2
    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f'{day:=^50}', '\n')
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = 'Home indexes'
        print(f'{home_indexes:^50}', '\n')
        print(f'Mess - {self.mess}')
    def is_alive(self):
        if self.gladness < 0:
            print('Дипресія...')
            return False
        elif self.satiety < 0:
            print('Голод...')
            return False
        elif self.mess < 0:
            print('Потонув у смітті...')
    def live(self):
        if self.is_alive() == False:
            return False
        self.days_indexes(day)
        dice = random.randint(1, 5)
        if self.satiety < 20:
            print('Я йду їсти')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print('Хочеться відпочити, але в будинку безлад тому я йдe прибирати')
                self.clean_home()
            else:
                print('Я відпочину')
                self.chill()
        elif self.water < 50:
            print('Йди поляй КАКТУС')
        elif dice == 1:
            print('Я відпочину')
            self.chill()
        elif dice == 2:
            print('Час працювати')
            self.work()
        elif dice == 3:
            print('я йдe прибирати')
            self.clean_home()
        elif dice == 4:
            print('Час смаколиків')
            self.shopping(manage='delicacies')
        elif dice == 5:
            print('Я йду поляю рослинку')
            self.to_plant()
class room:
    def __init__(self):
        self.mess=0
class Study:
    def __init__(self, school=None, academy=None, rugby=None):
        self.school=school
        self.academy=academy
        self.rugby=rugby
        cube = random.randit(1,3)
        if cube==1:
            print('Я піду в школу')
            self.school
        elif cube==2:
            print('Я піду в акдемію')
            self.academy
        elif cube==3:
            print('Я піду на регбі')
            self.rugby
anna=Anna(name='Anna')
for day in range(365):
    if anna.live==False:
        break