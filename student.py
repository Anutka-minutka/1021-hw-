import random
class Student:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.money=50
        self.alive=True

    def to_study(self):
        print('Час навчатися')
        self.progress+=0.12
        self.gladness-=3
        self.money+=25
    def to_sleep(self):
        print('Час спати')
        self.gladness+=3
        self.progress -= 0.5
        self.money -=5
    def to_chill(self):
        print('Час відпочити')
        self.gladness+=5
        self.progress-=0.1
        self.money -=10
    def to_earn(self):
        print('Час заробляти')
        self.gladness-=4
        self.progress-=0.5
        self.money+=35
    def is_alive(self):
        if self.progress<-0.5:
            print('Відрахували...')
            self.alive=False
        elif self.gladness<=0:
            print('Дипресія:(')
            self.alive = False
        elif self.progress>5:
            print('Закінчив екстерном')
            self.alive = False
        elif self.money<0:
            print('Закінчилися кошти за навчання')
            self.alive = False
    def end_of_day(self):
        print(f'Gladnes-{self.gladness}')
        print(f'Progress-{round(self.progress,2)}')
        print(f'Money-{self.money}')

    def live(self,day):
        day='Day+' +str(day) + 'of' + self.name + 'life'
        print(f'{day:=^50}')
        live_cube=random.randint(1,4)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        elif live_cube==4:
            self.to_earn()
        self.end_of_day()
        self.is_alive()

dan=Student(name='Dan')
for day in range(365):
    if dan.alive==False:
        break
    dan.live(day)


