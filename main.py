import random
class Cat:
    def __init__(self,name):
        self.name=name
        self.gladness=10
        self.caress=5
        self.sleep=5
        self.alive=True
#gladness=chill;progress=caress=to_caress
    def to_caress(self):
        print('Час погладити мене')
        self.caress+=1
        self.gladness+=1
        self.sleep-=1
    def to_sleep(self):
        print('Час спати')
        self.caress-=1
        self.gladness+=1
        self.sleep+=1
    def to_gladness(self):
        print('Час посміятися')
        self.caress+=1
        self.sleep-=1
        self.gladness+=1
    def is_alive(self):
        if self.gladness<-1:
            print('Причина:дипресія:(')
            self.alive = False
        elif self.caress<=0:
            print('Причина:не гладили:(')
            self.alive = False
        elif self.sleep<=0:
            print('Причина:мало сну')
            self.alive = False
    def end_of_day(self):
            print(f'Gladnes-{self.gladness}')
            print(f'Progress-{round(self.caress, 2)}')
    def live(self, day):
        day = 'Day+' + str(day) + 'of' + self.name + 'life'
        print(f'{day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_caress()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_gladness()
        self.end_of_day()
        self.is_alive()
sharik=Cat(name='Sharik')
for day in range(365):
    if sharik.alive==False:
        break
    sharik.live(day)
