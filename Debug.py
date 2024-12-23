#全局变量
has_key = False  # 玩家是否有钥匙
lives = 3 #初始生命值为3
first = 0
def input_maze():
    maze=[]
    """用户输入自定义迷宫，返回二维列表表示迷宫"""
    print("请输入迷宫地图（#代表墙, .代表空地, S代表起点, E代表终点, K代表钥匙）：")
    print("请按行输入地图，或输入 'done' 结束输入：")
    #begin 按行读入迷宫地图，构建迷宫地图列表矩阵maze
    while True:
        user_input = str(input().split("\n")).strip("['']").replace(" ", "")
        if user_input == "done":
            break
        else:
            maze.append(user_input)
    # end

    # 验证迷宫是否有起点和终点
    if not validate_maze(maze):
        print("迷宫必须有起点(S)和终点(E)，请重新输入。")
        maze.clear()  # 清空迷宫重输入
        input_maze()
    return maze 

"""验证迷宫是否包含起点和终点"""

def validate_maze(maze):
    start_exist = any('S' in row for row in maze)
    end_exist = any('E' in row for row in maze)
    return start_exist and end_exist

"""找到起点、终点的位置"""
def find_start_exit_pos(maze): 
    # begin
    y = 0
    for i in maze:
        x = 0
        for j in i:
            if j == "S":
                start_pos = (x, y)
            elif j == "E":
                exit_pos = (x, y)
            x += 1
        y += 1
    return start_pos, exit_pos

    # end
    
"""打印当前迷宫和玩家位置"""
def print_maze(maze,player_pos): 
    # begin
    x = player_pos[0]
    y = player_pos[1]
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if y == i and x == j:
                print("P", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()
    print()   
    # end 

"""根据玩家的输入移动玩家位置:
   如果移动位置合法，则玩家移动到新位置；
   如果移动位置撞墙，则玩家回复到移动前的位置，同时玩家生命值减一，提示：撞墙了！当前生命值为{lives}
   如果玩家的生命值为0了，则提示：你用尽了所有生命，游戏结束，用exit()语句退出游戏"""
def move_player(maze,directionlst,now_pos):
    ''' maze 游戏当前的地图矩阵\n
        directionlst玩家移动走步的列表\n
        now_pos玩家当前的位置玩家生命值\n
        请注意这个lives变量时global类型的\n
        before_pos 开始移动前的玩家的位置\n
    '''
    global lives 
    before_pos=tuple(now_pos)
    for dr in directionlst: 
        #begin
        now_pos = list(now_pos)
        if dr == 'w':
            now_pos[1] -= 1
        elif dr == 's':
            now_pos[1] += 1
        elif dr == 'a':
            now_pos[0] -= 1
        elif dr == 'd':
            now_pos[0] += 1
        #end 
        else:
            print("无效的移动指令，请输入 'w', 'a', 's', 'd' 来移动。")
            return

    # 如果按照directionlst内容移动的位置有效，则看下是否获取到key，并返回新移动到的位置now_pos；否则就面临着撞墙提示，和生命值减一操作
    if is_valid_move(now_pos,maze):
        get_key(maze,now_pos)
        return now_pos
    else:
        lives-=1
        print(f"撞墙了！当前生命值为{lives}")
        if lives<=0 :
            print("你用尽了所有生命，游戏结束")
            exit()
        print("无法移动到该位置！已回到上一次的位置。")
        return list(before_pos)

"""检查位置是否有效（未越界并且不是墙）"""
def is_valid_move(position,maze):
    # begin
    if maze[position[1]][position[0]] == "#":
        return False
    else:
        return True
    #end

"""根据游戏地图和玩家位置，判定玩家是否获取钥匙"""
def get_key(maze,new_pos):
    # begin
    global has_key
    global first
    if maze[new_pos[1]][new_pos[0]] == "K":
        has_key = True
        first = 1
        return has_key
    else:
        return False

    #end



def main():
    # 输入自定义迷宫
    map_maze = input_maze()  
    start_pos,exit_pos=find_start_exit_pos(map_maze)  # 找到起点,终点位置  
    before_pos=start_pos
    now_pos=None 
    print("迷宫已生成，目标是从 S 走到E，要求先拿到K，才可以打开出口大门，成功的走出迷宫。")

    # 游戏主循环
    while True:
        global first
        print_maze(map_maze,before_pos)
        print("请输入移动方向 w 上, a 左, s 下, d 右：",end="")
        move = input().strip().lower()
        print(move,end="\n")
        now_pos=move_player(map_maze,move,before_pos)
        if tuple(now_pos)==exit_pos and has_key:
            print("恭喜你！成功走出了迷宫！")
            break
        if now_pos!=exit_pos and has_key and first == 1:
            print("你找到了钥匙！")
            first = 0
        if tuple(now_pos)==exit_pos and not has_key :
            now_pos = before_pos
            print("你需要钥匙才能进入终点！")
            print("已经退回上一步位置！")
        before_pos=now_pos

# 运行游戏
if __name__ == "__main__":
    main()