import os
d = f"{os.environ['USERPROFILE']}/PYDIARY"
os.mkdir(f"{d}")
os.mkdir(f"{d}/loginfolder")
os.mkdir(f"{d}/기록")
e = open(f"{d}/loginfolder/log.txt", "w")
py = open(f"{os.environ['USERPROFILE']}/desktop/DIARY.py", "w")
py.write('''import os
from datetime import datetime
a = input('회원가입은 a, 로그인은 b')
if a == 'a':
    b = input('ID')
    c = input('password')
    bbb = ((open(f"{os.environ['USERPROFILE']}/PYDIARY/loginfolder/log.txt", "r").read()), '')
    e = open(f"{os.environ['USERPROFILE']}/PYDIARY/loginfolder/log.txt", "w")
    try:
        os.mkdir(f"{os.environ['USERPROFILE']}/PYDIARY/" + b)
    except FileExistsError:
        print('이미 있는 아이디입니다. 다시 시도해 주십시오.')
    aaaa = open(f"{os.environ['USERPROFILE']}/PYDIARY/{b}/기록.txt", 'w')
    e.write(bbb[0] + b + '/' + c + ', ')
    e.close()
    aaaa.close()
elif a == 'b':
    b = input('ID')
    c = input('password')
    e = open(f"{os.environ['USERPROFILE']}/PYDIARY/loginfolder/log.txt", "r")
    aa = e.read()
    li = aa.split(', ')
    if (b + '/' + c) in li:
        print('log in sucsessed')
        d = input('1.일기쓰기 2.일기확인')
        if d == '1':
            date = (str(datetime.now()))[0:10]
            day = input('요일')
            sentense = input('일기')
            ccc = ((open(f"{os.environ['USERPROFILE']}/PYDIARY/" + b + '/' + "기록.txt", "r").read()), '')
            f = open(f"{os.environ['USERPROFILE']}/PYDIARY/" + b + '/' + "기록.txt", "w")
            f.write(ccc[0] + date + '/' + day + '/' + sentense + '====')
            f.close()
        elif d == '2':
            se = input('일기 쓴 달(yyyy-mm)')
            li = str(open(f"{os.environ['USERPROFILE']}/PYDIARY/" + b + '/' + "기록.txt", "r").read()).split('====')
            x = 1
            aaa = []
            for i in li:
                if i[0:7] == se:
                    y = str(x)
                    if len(i) > 18:
                        print(y + '. ' + i[0:18] + '.....')
                    else:
                        print(y + '. ' + i)
                    x += 1
                    aaa.append(i)
            z = int(input('몇번 일기를 볼겁니까?'))
            print(aaa[z-1])
    else:
        print('log in failed')''')
e.close()
py.close()
    
