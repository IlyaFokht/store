from random import randint

class Dot:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x},{self.y})"

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Стреляете за доску"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Стрелял уже в эту клетку"

class BoardWrongShipException(BoardException):
    pass

class Ship:
    def __init__(self,bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range (self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x,cur_y))
        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

class Board:
    def __init__(self, hid=False, size=None):
        self.hid = hid
        self.size = size
        self.count = 0
        self.field = [["0"]*size for _ in range (size)]
        self.busy = []
        self.ships = []

    def add_ship(self,ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|"
        for i,row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

    def out(self,d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self,d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Ship destroyed")
                    return False
                else:
                    print("Ship wounded")
                    return True

        self.field[d.x][d.y]="."
        print("Miss")
        return False

    def begin(self):
        self.busy=[]

class Player:
    def __init__(self,board,enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class Ai(Player):
    def ask(self):
        d = Dot(randint(0, 9),randint(0,9))
        print (f"Computer's turn {d.x+1} {d.y+1}")
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input("Your turn").split()
            if len(cords) != 2:
                print("Input 2 coordinates")
                continue
            x, y = cords
            if not (x.isdigit()) or not (y.isdigit()):
                print("Input digits")
                continue

            x, y = int(x), int(y)

            return Dot(x-1, y-1)

class Game:
    def __init__(self, size=10,):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = False

        self.ai = Ai(co,pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        board = Board(size= self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts +=1
                if attempts>2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0,1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def greet(self):
        print("-------------------")
        print("  Приветствуем вас ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):
        num = 0
        while True:
            print("-"*20)
            print("User desk")
            print(self.us.board)
            print("-"*20)
            print("Computer desk")
            print(self.ai.board)
            if num % 2 ==0:
                print("-"*20)
                print("User turn")
                repeat = self.us.move()
            else:
                print("-"*20)
                print("Ai turn")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 10:
                print("-"*20)
                print("User win")
                break

            if self.us.board.count == 10:
                print("-"*20)
                print("Ai win")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

g = Game()
g.start()