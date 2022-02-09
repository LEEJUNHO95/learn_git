import os

# 파일을 읽어오기
# open(파일경로, 모드), 모드 = r, w, a 가장 기본
# 파일경로는 상대경로와 절대경로로 구분
# 절대경로는 최상위 루트(root)부터 지정된 파일의 위치까지 명시 (전체경로)
# 상대경로는 프로그램이 구동되는 현위치에서 상대적으로 접근이 가능한 경로
# c에서는 경로구분을 \\로 구성해야했음
# 파이썬은 /를 지원함 (\\로 가능)
# c는 불러온 파일이 NULL인지 확인했어야함
# 파이썬은 불러오는 파일의 위치가 잘못되었다면 오류발생
# 파일의 open()과 close()는 항상 짝지어서 명시되어야함



# 2차인 리스트로 'o','x','S','F' 와 같은 공백이나, 줄내림 등을
# 모두 제거한 의미있는 문자들만 모아둔 2차원좌표의 지도 데이터구성
# [
#     [o,x,o,x,x,x,x,o,F],
#     [o,o,o,x,x,o,o,o,x],
#     [o,x,o,x,o,o,x,o,x],
#     [o,o,o,o,o,x,x,o,o],
#     [x,x,x,x,o,o,x,x,x],
#     [o,o,o,o,x,o,o,o,o],
#     [x,o,x,o,o,o,x,o,x],
#     [o,o,o,o,x,o,o,o,x],
#     [S,x,x,o,o,x,x,o,x],
# ]
tile_map = []

def load_map(path):

    # file = open('D:/source/level1.map', 'r', encoding='utf-8')
    file = open(path, 'r', encoding='utf-8')
    # print(file)

    load_map_datas = []

    # 파이썬에서는 파일의 끝을 빈문자열 = ''
    # 빈문자열을 참 or 거짓으로 구분할 수 있는 방법
    # 문자열의 길이를 구함 (문자의 갯수) (ex: len(문자열))
    # 비교연산자를 활용 (ex: 문자열 == '')
    # 자료형의 참과 거짓을 확인 (ex: not 문자열)
    while True:
        line = file.readline()
        # line의 값은 모두 불러오면 '' 빈문자열이
        # 출력된다는 사실을 이용해 반복을 중단
        # 문자열의 특성을 가지고 비교
        if line == '':
            break

        # line 내 줄내림 제거
        line = line.replace('\n','')

        # print()함수는 기본 줄내림 포함해서 출력한다
        # print(line, end='')
        # os.system('pause')

        # split() 은 기본 공백을 구분자로 분리
        tileListForRow = line.split()
        # print(tileListForRow)
        load_map_datas.append(tileListForRow)
    file.close()

    return load_map_datas

start_pos = (None, None)
finish_pos = (None, None)
player_pos = (None, None)

def check_start_finish():

    global start_pos
    global finish_pos

    row = 0
    col = 0

    # 더이상 나열이 불가한 최소 단위의 항목을 하나씩 가져옴
    for datas in tile_map:
        # 한번 반복에 최대 9개까지 출력
        for data in datas:
            # 최대 9번 반복
            # print(f'{row,col}', end=',')
            # 'S'와 'F'의 값과 일치하면 해당 위치를 각 값에 맞는 변수에 기억
            if data == 'S':
                start_pos = (row, col)
            
            if data == 'F':
                finish_pos = (row, col)
            
            col += 1

        row += 1
        col = 0


def display_map():

    # row = 0
    # col = 0

    # 더이상 나열이 불가한 최소 단위의 항목을 하나씩 가져옴
    for datas in tile_map:
        # 한번 반복에 최대 9개까지 출력
        for data in datas:
            # 최대 9번 반복
            # print(f'{row,col}', end=',')            
            print(data, end=' ')
            # col += 1

        print()
        # row += 1
        # col = 0


def validation(offset, base_pos, std_map_datas, valid_tiles):

#  std_map_datas
#     [o,x,o,x,x,x,x,o,F],
#     [o,o,o,x,x,o,o,o,x],
#     [o,x,o,x,o,o,x,o,x],
#     [o,o,o,o,o,x,x,o,o],
#     [x,x,x,x,o,o,x,x,x],
#     [o,o,o,o,x,o,o,o,o],
#     [x,o,x,o,o,o,x,o,x],
#     [o,o,o,o,x,o,o,o,x],
#     [S,x,x,o,o,x,x,o,x],

    # 나 = 플레이어 기준으로 얼마큼 움직이면 
    # 특정 방향의 위치(row,col)의 값을 구할수 있을지?
    # 플레이어의 위치가 (8,0), base_pos = player_pos
    # 플레이어기준 한칸 이동시 절대좌표 북 = (7,0),  남 = (9,0), 동 = (8,1), 서 = (8,-1)
    # 상대좌표 북 = (-1,0), 남 = (1,0), 동 = (0,1), 서 = (0, -1) == offset
    

    # 상대적 차이를 정의한 offset값과 
    # 기준위치(player_pos)간의 차이를 계산한 target_pos를 구한다
    target_pos = (base_pos[0]+offset[0], base_pos[1]+offset[1])
    target_row = target_pos[0]
    target_col = target_pos[1]


    tile = 'x'
    # target_pos의 위치가 유효한 위치인지 파악
    # 9x9의 크기를 갖는 지도데이터를 기준으로 하고있기에 row, col의 최소 최대 인덱스값은 0,8
    # 유효한 위치? (row >= 0 and row < 9 and col >= 0 and col < 9)
    if (target_row >= 0 and target_row < 9) and (target_col >= 0 and target_col < 9):
        # 유효하다고 판단된 지도데이터 기준 해당위치의 값을 읽어온다 (from tile_map[][])
        # 지도데이터 기준 해당위치의 값을 tile 이라고 명함
        # tile의 값은 'x' or 'o' or 'F' or 'S' 중 하나
        tile = std_map_datas[target_row][target_col]
    
    # valid_tiles = ('o', 'F', 'S')
    if tile in valid_tiles:
        return True

    return False



def checking_valid_seletions():
    # 4방향의 위치를 특정 (row, col) 좌표를 사용
    # R=(0,1), L=(0,-1), T=(-1,0), U=(1,0)
    # 초기 플레이어의 위치 (r=8,c=0)
    # 지도 데이터셋에서 특정위치의 값을 읽어와 그 값이 유효한지 파악

    # 임의위치에서 파악
    # player_pos = (4,4)
    # print(f'현재 플레이어 위치: {player_pos}')


    # 플레이어가 이동 가능한 방향에 대한 선택지를 반환해줄 리스트
    # selections 변수를 선언 빈리스트로 초기화
    selections = []

    # 상대좌표는 4방향 값이 고정되어있음
    # 북 = (-1,0), 남 = (1,0), 동 = (0,1), 서 = (0, -1) == offset
    if validation(
        base_pos=player_pos, std_map_datas=tile_map, valid_tiles=('o','F','S'),
        offset=(0,1),
    ):
        # print('동쪽 가능')
        directionDic = {
            'message':'동쪽으로 가능',
            'offset':(0,1),
        }
        selections.append(directionDic)
        # selections.append('동쪽으로 가능')

    if validation(
        base_pos=player_pos, std_map_datas=tile_map, valid_tiles=('o','F','S'),
        offset=(0,-1),
    ):
        # print('서쪽 가능')
        directionDic = {
            'message':'서쪽으로 가능',
            'offset':(0,-1),
        }
        selections.append(directionDic)
        # selections.append('서쪽으로 가능')

    if validation(
        base_pos=player_pos, std_map_datas=tile_map, valid_tiles=('o','F','S'),
        offset=(-1,0),
    ):
        # print('북쪽 가능')
        directionDic = {
            'message':'북쪽으로 가능',
            'offset':(-1,0),
        }
        selections.append(directionDic)
        # selections.append('북쪽으로 가능')

    if validation(
        base_pos=player_pos, std_map_datas=tile_map, valid_tiles=('o','F','S'),
        offset=(1,0),
    ):
        # print('남쪽 가능')
        directionDic = {
            'message':'남쪽으로 가능',
            'offset':(1,0),
        }
        selections.append(directionDic)
        # selections.append('남쪽으로 가능')

    return selections


# 플레이되는 동안 반복적으로 표시 및 처리될 공간
def run_loops():

    global player_pos

    while True:
        os.system('cls')
        print(f'현재 플레이어의 위치: {player_pos}')

        # 플레이어 중심으로 현위치에서 4방향 중(동,서,남,북) 
        # 갈 수 있는 방향을 파악하고 해당 선택지를 제공
        valid_selections = checking_valid_seletions()
        # valid_selections = [
        #    {
        #        'offset' : (x,x),
        #        'message' : ""
        #    }...
        # ]

        # 파악 된 갈 수 있는 방향을 선택지로 표시 및 플레이어 입력대기
        i = 1
        for selection in valid_selections:
            print(f'{i}.{selection["message"]}')
            # print(f'{i}.{selection}')
            i += 1

        # input()에서 사용자의 입력은 문자열로 반환됨
        # 그래서 숫자입력만 필요한 현재 경우 int()를 이용해 숫자로 변경
        selection_str = input('어느방향으로 가실겁니까?(숫자로만)\n')
        if not selection_str.isdigit():
            # print(f'잘못된 입력입니다!!! 다시입력해주세요')
            continue

        selected_num = int(selection_str)
        if selected_num <= 0 or selected_num > len(valid_selections):
            # print(f'잘못된 입력입니다!!! 다시입력해주세요')
            continue

        # selected_val = valid_selections[selected_num-1]
        # print(f'사용자가 선택한 번호의 값: {selected_val}')

        selection_dict = valid_selections[selected_num-1]
        offset = selection_dict["offset"]
        # print(f'사용자가 선택한 offset: {offset}')
        
        # 플레이어가 입력한 방향으로 플레이어를 이동
        player_pos = (player_pos[0] + offset[0], player_pos[1] + offset[1])
        # print(f'이동한 플레이어의 위치: {player_pos}')

        # # 이동 후의 위치가 도착지라면 플레이를 중단
        # if player_pos == finish_pos:
        #     return


# 플레이 시작전 준비
def prepares():

    # 지도 파일을 불러와 지도 데이터셋을 구성
    global tile_map
    tile_map = load_map('D:/source/level1.map')

    # 준비된 지도를 한번 출력 
    # (내부에 시작위치와 도착위치를 특정하는 코드 포함)
    # print(tile_map)
    # display_map()
    check_start_finish()

    # 플레이어의 시작위치를 지정
    global player_pos
    player_pos = start_pos #(8,0)
    # print(f'start player_pos: {player_pos}')

    # 플레이
    run_loops()


# ===========================
# 프로그램 시작
# ===========================

# 준비와 함께 시작
prepares()





