# class로 기본 형태를 저장한 후 instance를 만든 class를 가져와서 형성함. / 혹은 내용 추가 (proche.color="Red")

class Car():
    wheels = 4
    doors = 4
    windows = 4
    sears = 4

# Method : class 안에 있는 함수.(def)
    def start(potato):
        print("I started")

proche = Car()
proche.start() 

    # Method를 실행할 때 argument를 주지 않았으나 argument가 주어졌다는 에러가 발생함.
    # Method의 첫번째 argument를 Method를 호출하는 instance 자신임(self)
    # Method의 첫번째 argument를 적어줘야 됨.

# 기본 Method들
# __str__ : instance를 print 했을 때 호출되는 Method / Method이름을 str형태로 전환해줌.
# __init__

class Cart():
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str(self):
        return f"Car with {self.wheels} wheels"




proche = Cart(color="green", price="$40")
print(proche.color, proche.price)

mini = Cart()
print(mini.color, mini.price)

# 객체지향 프로그래밍을 통해 기본 값을 미리 설정하고, 내가 만드는 instance에 원하는 argument들을 수정하면서 프로그래밍 해갈 수 있음.


# EXTEND

class Convertible(Car):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 부모 class의 Method를 Extend 하는 방법. super를 사용할 경우 부모 class의 Method에 접근할 수 있음.
        # super가 부모 class의 역할을 함. 
        # argument를 호출해줘야 잘 작동.
        self.time = kwargs.get("time",10)

    def take_off(self):
        return "taking off"

    def __str(self):
        return f"Car with no roof"
        zsdf




# 가져오고 싶은 class를 새로 만드는 class의 argument에 넣으면 새로 만드는 class는 가져온 class의 기능 모두 사용 가능.
# 이것을 다른 class로 확장, 혹은 다른 class가 기존 class를 inherit(상속)했다고 함.