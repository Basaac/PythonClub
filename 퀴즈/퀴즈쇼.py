import random
import time

input('아무 버튼이나 누르세요:')
time.sleep(1)
s = 0

def asasas():
    asdf = input('다시하시겠습니까?(예,아니오)')
    if asdf == '예':
        random.choice(functions)()
    else:
        print('프로그램을 종료합니다.')
        exit()

def a():
        global s
        print('수학')

        ab = input('1. 119243 + 139805 =') #1번문제
        if ab == '256048':
            print('정답')
            print('점수 + 1')
            s += 1
        else:
            print('오답(정답은 256048)')
        time.sleep(0.5)
        ac = input('2. 890432 - 284324 =') #2번문제
        if ac == '606108':
            print('정답')
            s += 1
        else:
            print('오답(정답은 606108)')
        time.sleep(0.5)
        ad = input('3. 292 x 371 =') #3번문제
        if ad == 108332:
            print('정답')
            s += 1
        else:
            print('오답(정답은 108332)')
        time.sleep(0.5)
        print('당신의 점수는 !!')
        time.sleep(3)
        print(s,'점')
        asasas()

def b():
        global s
        print('과학')

        ba = input('1.물이 어는점은 몇도 일까?(숫자만 입력)') #1번문제
        if ba == '0':
            print('정답')
            print('점수 + 1')
            s += 1
        else:
            print('오답(정답은 0)')
        time.sleep(0.5)
        bb = input('2.물이 끓는점은 몇도 일까?(숫자만 입력)') #2번문제
        if bb == '100':
            print('정답')
            s += 1
        else:
            print('오답(정답은 100)')
        time.sleep(0.5)
        bc = input('3.철이 녹는 온도는 몇도 일까?(숫자만 입력)') #3번문제
        if bc == '1535':
            print('정답')
            s += 1
        else:
            print('오답(정답은 1535)')
        time.sleep(0.5)
        print('당신의 점수는 !!')
        time.sleep(3)
        print(s,'점')
        asasas()

def c():
        global s
        print('역사')

        ca = input('1.훈민정음을 만든 사람은?') #1번문제
        if ca == '세종대왕'or'이도':
            print('정답')
            print('점수 + 1')
            s += 1
        else:
            print('오답(정답은 세종대왕 또는 이도)')
        time.sleep(0.5)
        cb = input('2.조선의 1대 왕의 본명은?') #2번문제
        if cb == '이성계':
            print('정답')
            s += 1
        else:
            print('오답(정답은 이성계)')
        time.sleep(0.5)
        cc = input('3.춘추 삼국시대에 세 나라 중에 신라,고구려 말고 어떤 나라가 있었을까?') #3번문제
        if cc == '백제':
            print('정답')
            s += 1
        else:
            print('오답(정답은 백제)')
        time.sleep(0.5)
        print('당신의 점수는 !!')
        time.sleep(3)
        print(s,'점')
        asasas()

def d():
        global s
        print('국어')

        da = input('1.다음중 맞는 단어를 고르시오(빈털털이,빈털터리)') #1번문제
        if da == '빈털터리':
            print('정답')
            print('점수 + 1')
            s += 1
        else:
            print('오답(정답은 빈털터리)')
        time.sleep(0.5)
        db = input('2.다음중 맞는 단어를 고르시오(들어내다,드러내다)') #2번문제
        if db == ' 들어내다':
            print('정답')
            s += 1
        else:
            print('오답(들어내다)')
        time.sleep(0.5)
        dc = input('3.다음중 맞는 단어를 고르시오(해님,햇님)') #3번문제
        if dc == '해님':
            print('정답')
            s += 1
        else:
            print('오답(정답은 해님)')
        time.sleep(0.5)
        print('당신의 점수는 !!')
        time.sleep(3)
        print(s,'점')
        asasas()

def e():
        global s
        print('영어')

        ea = input('1.사과를 영어로 하면?') #1번문제
        if ea == 'apple':
            print('정답')
            print('점수 + 1')
            s += 1
        else:
            print('오답(정답은 apple)')
        time.sleep(0.5)
        eb = input('2.과소평가하다를 영어로 하면?') #2번문제
        if eb == 'underestimation':
            print('정답')
            s += 1
        else:
            print('오답(정답은 underestimation)')
        time.sleep(0.5)
        ec = input('3.새가 사는곳을 영어로 하면?') #3번문제
        if ec == 'nest':
            print('정답')
            s += 1
        else:
            print('오답(정답은 nest)')
        time.sleep(0.5)
        print('당신의 점수는 !!')
        time.sleep(3)
        print(s,'점')
        asasas()
        


functions = [a, b, c, d, e]
random.choice(functions)()


