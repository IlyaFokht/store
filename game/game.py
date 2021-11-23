field=[['-'] * 3 for _ in range(3)]
def show_field(f):
    print('  0 1 2')

    for i in range (len(field)):
        print(str(i),*field[i])

def users_input(f):
    while True:
        place=input("input coordinates:").split()
        if len(place)!=2:
            print("input 2 coordinates")
            continue

        if not (place[0].isdigit() and place[1].isdigit()):
            print('input digits')
            continue
        x,y=map(int,place)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print("out of range")
            continue
        if f[x][y]!='-':
            print("place busy")
            continue
        break
    return x,y
def win_v1(f,user):
    def check_line(a1,a2,a3,user):
        if a1==user and a2==user and a3==user:
            return True
    for n in range(3):
        if check_line(f[n][0],f[n][1],f[n][2],user) or \
           check_line(f[0][n], f[1][n], f[2][n], user) or \
           check_line(f[0][0], f[1][1], f[2][2], user) or \
           check_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False


count=0
while True:
    if count==9:
        print("draw")
        break
    if count%2==0:
        user='x'
    else:
        user='0'
    show_field(field)
    x,y=users_input(field)
    field[x][y]=user
    if win_v1(field,user):
        print(f"winner is {user}")
        show_field(field)
        break
    count+=1