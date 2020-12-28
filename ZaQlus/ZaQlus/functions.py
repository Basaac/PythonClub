"""
    Copyright (C) 2020  Basaac, piz2a

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import os
import random
import math


def shutdown():
    os.system('shutdown -s -t 0')


def pyramid(n, char: str = '*'):
    for i in range(1, n+1):
        print(char * i)


def poem():
    print("""죽는 날까지 하늘을 우러러
한 점 부끄럼이 없기를,
잎새에 이는 바람에도
나는 괴로워했다.
별을 노래하는 마음으로
모든 죽어 가는 것을 사랑해야지
그리고 나한테 주어진 길을
걸어가야겠다.

오늘 밤에도 별이 바람에 스치운다.""")


def easter_egg():
    import threading as th
    import movingscreen
    th.Thread(target=movingscreen.main).start()


functions = dict(
    s=input,  # 인풋
    p=print,  # 프린트
    i=int,  # 정수화
    c=str,  # 문자(열)화
    q=sys.exit,  # 코드 종료
    h=lambda: print('Hello World!'),  # 안녕 세계
    # d=shutdown,  # 컴퓨터 종료
    l=lambda: print('Copyright (C) 2020  Basaac, Piz2a. Under GPL 3.0 license'),  # 재미없는 약관
    r=random.random,  # 랜덤 소수 (0<x<1)
    d=math.floor,  # 버림
    u=math.ceil,  # 올림
    m=round,  # 반올림
    y=pyramid,  # 피라미드
    o=poem,  # 시
    e=easter_egg  # 이스터에그
)
