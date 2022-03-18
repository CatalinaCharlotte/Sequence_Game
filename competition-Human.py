import csv
import ast
import random
import sys


def calculate_winrate(humanlist, c1, c2, c3):
    roundscore = 10 - len(humanlist)
    origin_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    c1list = list(set(origin_list) - set(c1))
    c2list = list(set(origin_list) - set(c2))
    c3list = list(set(origin_list) - set(c3))
    winrate = []
    repair_winrate = []

    for human in humanlist:
        winnum = 0
        allnum = 0
        for x in c1list:
            for y in c2list:
                for z in c3list:
                    comp = [human, x, y, z]
                    winnumber = decidewinnumber(comp)
                    if human == winnumber:
                        winnum += 1
                        allnum += 1
                    else:
                        allnum += 1
        win_rate = 100 * winnum / allnum
        win_rate = round(win_rate, 2)
        winrate.append(win_rate)
        # repairrate = win_rate * roundscore / human
        # repair_winrate.append(repairrate)

    ratesum = 0
    for i in repair_winrate:
        ratesum += i

    print('Winning rate:' + str(winrate))
    # print('Repaired rate:' + str(repair_winrate))
    # print('Avg Repaired rate' + str(ratesum / len(humanlist)))


def playgame_human(p1, p2, p3, p4, desk, record_id, human_id):
    # play a game with human
    leveluppt = [20, 20, 20, 20, 40, 60, 80, 100, 100, 100, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 3600, 4000,
                 9999]
    sys.stdout.flush()
    record = []
    if p1['id'] in record_id:
        record.append(p1['id'])
    if p2['id'] in record_id:
        record.append(p2['id'])
    if p3['id'] in record_id:
        record.append(p3['id'])
    if p4['id'] in record_id:
        record.append(p4['id'])
    human_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    human_sequence = []

    print('******************** Match Start ********************\n')
    if p1['id'] not in human_id:
        print('player 1:' + all_level_list[p1['level']] + '  R:' + str(p1['R']) + '\n')
    else:
        print('player 1:' + all_level_list[p1['level']] + ' ' + str(p1['pt']) + '/' + str(
            leveluppt[p1['level']]) + '  R:' + str(p1['R']) + '(You)\n')
    if p2['id'] not in human_id:
        print('player 2:' + all_level_list[p2['level']] + '  R:' + str(p2['R']) + '\n')
    else:
        print('player 2:' + all_level_list[p2['level']] + ' ' + str(p2['pt']) + '/' + str(
            leveluppt[p2['level']]) + '  R:' + str(p2['R']) + '(You)\n')
    if p3['id'] not in human_id:
        print('player 3:' + all_level_list[p3['level']] + '  R:' + str(p3['R']) + '\n')
    else:
        print('player 3:' + all_level_list[p3['level']] + ' ' + str(p3['pt']) + '/' + str(
            leveluppt[p3['level']]) + '  R:' + str(p3['R']) + '(You)\n')
    if p4['id'] not in human_id:
        print('player 4:' + all_level_list[p4['level']] + '  R:' + str(p4['R']) + '\n')
    else:
        print('player 4:' + all_level_list[p4['level']] + ' ' + str(p4['pt']) + '/' + str(
            leveluppt[p4['level']]) + '  R:' + str(p4['R']) + '(You)\n')

    score = [0, 0, 0, 0]
    p1seq = p1['seq']
    p2seq = p2['seq']
    p3seq = p3['seq']
    p4seq = p4['seq']
    p1list = []
    p2list = []
    p3list = []
    p4list = []
    for i in range(len(p1seq)):
        sys.stdout.flush()
        print('---------------')
        print('Game Round ' + str(i + 1) + '\n')
        print('Score: [1]' + str(score[0]) + ' [2]' + str(score[1]) + ' [3]' + str(score[2]) + ' [4]' + str(
            score[3]) + '\n')
        print('Player 1 have used:' + str(p1list))
        print('Player 2 have used:' + str(p2list))
        print('Player 3 have used:' + str(p3list))
        print('Player 4 have used:' + str(p4list))
        print('Your left number:' + str(human_number) + '\n')
        if p1['id'] in human_id:
            calculate_winrate(human_number, p2list, p3list, p4list)
        if p2['id'] in human_id:
            calculate_winrate(human_number, p1list, p3list, p4list)
        if p3['id'] in human_id:
            calculate_winrate(human_number, p1list, p2list, p4list)
        if p4['id'] in human_id:
            calculate_winrate(human_number, p1list, p2list, p3list)

        if p1['id'] in human_id:
            p1num = -1
            while p1num not in human_number:
                sys.stdout.flush()
                try:
                    p1num = int(input('Select a number in your left number:\n'))
                except:
                    print('Input Error, please check.')
                    p1num = -1
            human_sequence.append(p1num)
            p1list.append(p1num)
            human_number.remove(p1num)
            sys.stdout.flush()
        else:
            p1num = p1seq[i]
            p1list.append(p1num)
        if p2['id'] in human_id:
            p2num = -1
            while p2num not in human_number:
                sys.stdout.flush()
                try:
                    p2num = int(input('Select a number in your left number:\n'))
                except:
                    print('Input Error, please check.')
                    p2num = -1
            p2list.append(p2num)
            human_sequence.append(p2num)
            human_number.remove(p2num)
            sys.stdout.flush()
        else:
            p2num = p2seq[i]
            p2list.append(p2num)
        if p3['id'] in human_id:
            p3num = -1
            while p3num not in human_number:
                sys.stdout.flush()
                try:
                    p3num = int(input('Select a number in your left number:\n'))
                except:
                    print('Input Error, please check.')
                    p3num = -1
            p3list.append(p3num)
            human_sequence.append(p3num)
            human_number.remove(p3num)
            sys.stdout.flush()
        else:
            p3num = p3seq[i]
            p3list.append(p3num)
        if p4['id'] in human_id:
            p4num = -1
            while p4num not in human_number:
                sys.stdout.flush()
                try:
                    p4num = int(input('Select a number in your left number:\n'))
                except:
                    print('Input Error, please check.')
                    p4num = -1
            p4list.append(p4num)
            human_sequence.append(p4num)
            human_number.remove(p4num)
            sys.stdout.flush()
        else:
            p4num = p4seq[i]
            p4list.append(p4num)

        winnum = decidewinnumber([p1num, p2num, p3num, p4num])
        if winnum == -1:
            continue
        else:
            if p1num == winnum:
                score[0] += (i + 1)
            elif p2num == winnum:
                score[1] += (i + 1)
            elif p3num == winnum:
                score[2] += (i + 1)
            else:
                score[3] += (i + 1)
        if max(score) >= 23:
            break

    if len(record) > 0:
        for rid in record:
            f = open(str(rid) + '.txt', 'a')
            f.write('*******************************\n')
            if p1['id'] not in human_id:
                f.write('player 1:' + str(p1['seq']) + '  id:' + str(p1['id']) + '  level:' + all_level_list[
                    p1['level']] + '  R:' + str(p1['R']) + '\n')
            else:
                f.write(
                    'player 1:' + str(tuple(human_sequence)) + '  id:' + str(p1['id']) + '  level:' + all_level_list[
                        p1['level']] + '  R:' + str(p1['R']) + '\n')
            if p2['id'] not in human_id:
                f.write('player 2:' + str(p2['seq']) + '  id:' + str(p2['id']) + '  level:' + all_level_list[
                    p2['level']] + '  R:' + str(p2['R']) + '\n')
            else:
                f.write(
                    'player 2:' + str(tuple(human_sequence)) + '  id:' + str(p2['id']) + '  level:' + all_level_list[
                        p2['level']] + '  R:' + str(p2['R']) + '\n')
            if p3['id'] not in human_id:
                f.write('player 3:' + str(p3['seq']) + '  id:' + str(p3['id']) + '  level:' + all_level_list[
                    p3['level']] + '  R:' + str(p3['R']) + '\n')
            else:
                f.write(
                    'player 3:' + str(tuple(human_sequence)) + '  id:' + str(p3['id']) + '  level:' + all_level_list[
                        p3['level']] + '  R:' + str(p3['R']) + '\n')
            if p3['id'] not in human_id:
                f.write('player 4:' + str(p4['seq']) + '  id:' + str(p4['id']) + '  level:' + all_level_list[
                    p4['level']] + '  R:' + str(p4['R']) + '\n')
            else:
                f.write(
                    'player 4:' + str(tuple(human_sequence)) + '  id:' + str(p4['id']) + '  level:' + all_level_list[
                        p4['level']] + '  R:' + str(p4['R']) + '\n')
            f.close()

    # Decide Rank
    rank = [0, 0, 0, 0]
    sort_score = []
    sort_score.extend(score)
    rank_now = 1
    while len(sort_score) > 0:
        sort_score.sort(reverse=True)
        maxs = sort_score[0]
        sameindex = []
        for i in range(len(score)):
            if score[i] == maxs:
                sameindex.append(i)
        while len(sameindex) > 0:
            winindex = random.randint(0, len(sameindex) - 1)
            rank[sameindex[winindex]] = rank_now
            rank_now += 1
            sameindex.remove(sameindex[winindex])
        while sort_score.count(maxs) > 0:
            sort_score.remove(maxs)
    # update level pt and R
    origin_R = [p1['R'], p2['R'], p3['R'], p4['R']]
    p1 = updateLevelPtR(p1, origin_R, rank[0], desk)
    p2 = updateLevelPtR(p2, origin_R, rank[1], desk)
    p3 = updateLevelPtR(p3, origin_R, rank[2], desk)
    p4 = updateLevelPtR(p4, origin_R, rank[3], desk)

    print('-------------- Match Over ---------------')
    print('Result:\n')
    print('Player 1----Score:' + str(score[0]) + '  Rank:' + str(rank[0]) + '\n')
    print('Player 2----Score:' + str(score[1]) + '  Rank:' + str(rank[1]) + '\n')
    print('Player 3----Score:' + str(score[2]) + '  Rank:' + str(rank[2]) + '\n')
    print('Player 4----Score:' + str(score[3]) + '  Rank:' + str(rank[3]) + '\n')
    print('********************************\n')

    if len(record) > 0:
        for rid in record:
            f = open(str(rid) + '.txt', 'a')
            f.write('Result:\n')
            f.write('Player 1----Score:' + str(score[0]) + '  Rank:' + str(rank[0]) + '\n')
            f.write('Player 2----Score:' + str(score[1]) + '  Rank:' + str(rank[1]) + '\n')
            f.write('Player 3----Score:' + str(score[2]) + '  Rank:' + str(rank[2]) + '\n')
            f.write('Player 4----Score:' + str(score[3]) + '  Rank:' + str(rank[3]) + '\n')
            f.write('*******************************\n')

    # os.system('pause')
    sys.stdout.flush()
    input('Press Enter to continue.')

    sys.stdout.flush()
    return p1, p2, p3, p4


def playgame(p1, p2, p3, p4, desk, record_id):
    # play a game
    sys.stdout.flush()
    record = []
    if p1['id'] in record_id:
        record.append(p1['id'])
    if p2['id'] in record_id:
        record.append(p2['id'])
    if p3['id'] in record_id:
        record.append(p3['id'])
    if p4['id'] in record_id:
        record.append(p4['id'])
    if len(record) > 0:
        for rid in record:
            f = open(str(rid) + '.txt', 'a')
            f.write('*******************************\n')
            f.write('player 1:' + str(p1['seq']) + '  id:' + str(p1['id']) + '  level:' + all_level_list[
                p1['level']] + '  R:' + str(p1['R']) + '\n')
            f.write('player 2:' + str(p2['seq']) + '  id:' + str(p2['id']) + '  level:' + all_level_list[
                p2['level']] + '  R:' + str(p2['R']) + '\n')
            f.write('player 3:' + str(p3['seq']) + '  id:' + str(p3['id']) + '  level:' + all_level_list[
                p3['level']] + '  R:' + str(p3['R']) + '\n')
            f.write('player 4:' + str(p4['seq']) + '  id:' + str(p4['id']) + '  level:' + all_level_list[
                p4['level']] + '  R:' + str(p4['R']) + '\n')
            f.close()
    score = [0, 0, 0, 0]
    p1seq = p1['seq']
    p2seq = p2['seq']
    p3seq = p3['seq']
    p4seq = p4['seq']
    for i in range(len(p1seq)):
        winnum = decidewinnumber([p1seq[i], p2seq[i], p3seq[i], p4seq[i]])
        if winnum == -1:
            continue
        else:
            if p1seq[i] == winnum:
                score[0] += (i + 1)
            elif p2seq[i] == winnum:
                score[1] += (i + 1)
            elif p3seq[i] == winnum:
                score[2] += (i + 1)
            else:
                score[3] += (i + 1)
        if max(score) >= 23:
            break
    # Decide Rank
    rank = [0, 0, 0, 0]
    sort_score = []
    sort_score.extend(score)
    rank_now = 1
    while len(sort_score) > 0:
        sort_score.sort(reverse=True)
        maxs = sort_score[0]
        sameindex = []
        for i in range(len(score)):
            if score[i] == maxs:
                sameindex.append(i)
        while len(sameindex) > 0:
            winindex = random.randint(0, len(sameindex) - 1)
            rank[sameindex[winindex]] = rank_now
            rank_now += 1
            sameindex.remove(sameindex[winindex])
        while sort_score.count(maxs) > 0:
            sort_score.remove(maxs)
    # update level pt and R
    origin_R = [p1['R'], p2['R'], p3['R'], p4['R']]
    p1 = updateLevelPtR(p1, origin_R, rank[0], desk)
    p2 = updateLevelPtR(p2, origin_R, rank[1], desk)
    p3 = updateLevelPtR(p3, origin_R, rank[2], desk)
    p4 = updateLevelPtR(p4, origin_R, rank[3], desk)
    if len(record) > 0:
        for rid in record:
            f = open(str(rid) + '.txt', 'a')
            f.write('Result:\n')
            f.write('Player 1----Score:' + str(score[0]) + '  Rank:' + str(rank[0]) + '\n')
            f.write('Player 2----Score:' + str(score[1]) + '  Rank:' + str(rank[1]) + '\n')
            f.write('Player 3----Score:' + str(score[2]) + '  Rank:' + str(rank[2]) + '\n')
            f.write('Player 4----Score:' + str(score[3]) + '  Rank:' + str(rank[3]) + '\n')
            f.write('*******************************\n')
    return p1, p2, p3, p4


def decidewinnumber(numlist):
    while len(numlist) > 0:
        maxnum = max(numlist)
        if numlist.count(maxnum) == 1:
            return maxnum
        else:
            while numlist.count(maxnum) > 0:
                numlist.remove(maxnum)
    return -1


def updateLevelPtR(player, originR, rank, desk):
    # update pt
    startpt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 4000]
    leveluppt = [20, 20, 20, 20, 40, 60, 80, 100, 100, 100, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 3600, 4000,
                 9999]
    achievept = [[30, 15], [60, 15], [75, 30], [90, 45]]  # 1st and 2nd from different desk
    lostpt = [0, 0, 0, 0, 0, 0, 0, 0, -15, -30, -45, -60, -75, -90, -105, -120, -135, -150, -165, -180]

    meanR = (originR[0] + originR[1] + originR[2] + originR[3]) / 4
    gametimes = player['1st'] + player['2nd'] + player['3rd'] + player['4th']

    if rank == 1:
        gametimes += 1
        player['1st'] += 1
        player['pt'] += achievept[desk][0]
        if player['pt'] >= leveluppt[player['level']]:
            player['level'] += 1
            player['pt'] = startpt[player['level']]
        player['R'] = updateR(player['R'], meanR, rank, gametimes)

    elif rank == 2:
        gametimes += 1
        player['2nd'] += 1
        player['pt'] += achievept[desk][1]
        if player['pt'] >= leveluppt[player['level']]:
            player['level'] += 1
            player['pt'] = startpt[player['level']]
        player['R'] = updateR(player['R'], meanR, rank, gametimes)
    elif rank == 3:
        gametimes += 1
        player['3rd'] += 1
        player['R'] = updateR(player['R'], meanR, rank, gametimes)
    else:
        gametimes += 1
        player['4th'] += 1
        player['pt'] += lostpt[player['level']]
        if player['pt'] < 0:
            if player['level'] <= 9:
                player['pt'] = 0
            else:
                player['level'] -= 1
                player['pt'] = startpt[player['level']]
        player['R'] = updateR(player['R'], meanR, rank, gametimes)
    return player


def updateR(playerR, meanR, rank, times):
    timesrepair = 0.2
    if times < 400:
        timesrepair = 1 - times * 0.002
    else:
        timesrepair = 0.2
    result = [30, 10, -10, -30]
    if meanR < 1500:
        mean = 1500
    else:
        mean = meanR
    Rrepair = (mean - playerR) / 40

    playerR += (timesrepair * (result[rank - 1] + Rrepair))

    playerR = int(playerR)
    return playerR


# setting
round_all = 1
players = []
all_level = {'10k': 0, '9k': 1, '8k': 2, '7k': 3, '6k': 4, '5k': 5, '4k': 6, '3k': 7, '2k': 8, '1k': 9, '1d': 10,
             '2d': 11, '3d': 12, '4d': 13, '5d': 14, '6d': 15, '7d': 16, '8d': 17, '9d': 18, '10d': 19, 'top': 20}
all_level_list = ['10k', '9k', '8k', '7k', '6k', '5k', '4k', '3k', '2k', '1k', '1d', '2d', '3d', '4d', '5d', '6d', '7d',
                  '8d', '9d', '10d', 'top']
normal = []
up = []  # >=1k R>=1500
upper = []  # >=4d R>=1800
top = []  # >=7d R>=2000
tenhou = []  # >=top, no game

distribute = []
humanid = [362881]
recordid = [362881]
human_this_round_play = False

# print('***********************Data Loading************************')
# # read players' profile
# with open('profile.csv', 'r') as profile:
#     csv_reader = csv.reader(profile)
#     title = 0
#     for listx in csv_reader:
#         if title == 0:
#             title += 1
#             continue
#         player = {}
#         player['id'] = int(listx[0])
#         player['seq'] = ast.literal_eval(listx[1])
#         player['level'] = all_level[listx[2]]
#         player['pt'] = int(listx[3])
#         player['R'] = int(listx[4])
#         player['1st'] = int(listx[5])
#         player['2nd'] = int(listx[6])
#         player['3rd'] = int(listx[7])
#         player['4th'] = int(listx[8])
#         players.append(player)
#     profile.close()

# for r in range(round):
while not human_this_round_play:
    print('*********************** Data Loading ************************')
    # read players' profile
    with open('profile.csv', 'r') as profile:
        csv_reader = csv.reader(profile)
        title = 0
        for listx in csv_reader:
            if title == 0:
                title += 1
                continue
            player = {}
            player['id'] = int(listx[0])
            player['seq'] = ast.literal_eval(listx[1])
            player['level'] = all_level[listx[2]]
            player['pt'] = int(listx[3])
            player['R'] = int(listx[4])
            player['1st'] = int(listx[5])
            player['2nd'] = int(listx[6])
            player['3rd'] = int(listx[7])
            player['4th'] = int(listx[8])
            players.append(player)
        profile.close()
    print('*********************** Match Searching ************************')
    for player in players:
        if player['level'] == 20:
            tenhou.append(player)
        elif player['level'] >= 16 and player['R'] >= 2000:
            top.append(player)
        elif player['level'] >= 13 and player['R'] >= 1800:
            upper.append(player)
        elif player['level'] >= 9 and player['R'] >= 1500:
            up.append(player)
        else:
            normal.append(player)

    distribute.append((len(normal), len(up), len(upper), len(top)))

    players.clear()
    desk = 0
    while desk <= 4:
        if desk == 0:
            playernumber = len(normal)
            print('normal desk:' + str(playernumber))
            if playernumber >= 4:
                random.shuffle(normal)
                # reverse = random.randint(0, 1)
                # if reverse == 0:
                #     normal.sort(key=lambda keys: keys['R'], reverse=True)
                # else:
                #     normal.sort(key=lambda keys: keys['R'], reverse=False)

            i = 0
            while i + 3 <= playernumber - 1:
                if normal[i]['id'] in humanid or normal[i + 1]['id'] in humanid or normal[i + 2]['id'] in humanid or \
                        normal[i + 3]['id'] in humanid:
                    human_this_round_play = True
                    p1, p2, p3, p4 = playgame_human(normal[i], normal[i + 1], normal[i + 2], normal[i + 3], desk,
                                                    recordid, humanid)
                else:
                    p1, p2, p3, p4 = playgame(normal[i], normal[i + 1], normal[i + 2], normal[i + 3], desk, recordid)
                players.append(p1)
                players.append(p2)
                players.append(p3)
                players.append(p4)
                i += 4
            while i <= playernumber - 1:
                players.append(normal[i])
                i += 1
            desk += 1
        if desk == 1:
            playernumber = len(up)
            print('up desk:' + str(playernumber))
            if playernumber >= 50000:
                random.shuffle(up)
                # reverse = random.randint(0, 1)
                # if reverse == 0:
                #     up.sort(key=lambda keys: keys['R'], reverse=True)
                # else:
                #     up.sort(key=lambda keys: keys['R'], reverse=False)
                i = 0
                while i + 3 <= playernumber - 1:
                    if up[i]['id'] in humanid or up[i + 1]['id'] in humanid or up[i + 2]['id'] in humanid or up[i + 3][
                        'id'] in humanid:
                        human_this_round_play = True
                        p1, p2, p3, p4 = playgame_human(up[i], up[i + 1], up[i + 2], up[i + 3], desk, recordid, humanid)
                    else:
                        p1, p2, p3, p4 = playgame(up[i], up[i + 1], up[i + 2], up[i + 3], desk, recordid)
                    players.append(p1)
                    players.append(p2)
                    players.append(p3)
                    players.append(p4)
                    i += 4
                while i <= playernumber - 1:
                    players.append(up[i])
                    i += 1
            else:
                i = 0
                while i <= playernumber - 1:
                    players.append(up[i])
                    i += 1
            desk += 1
        if desk == 2:
            playernumber = len(upper)
            print('upper desk:' + str(playernumber))
            if playernumber >= 5000:
                random.shuffle(upper)
                # reverse = random.randint(0, 1)
                # if reverse == 0:
                #     upper.sort(key=lambda keys: keys['R'], reverse=True)
                # else:
                #     upper.sort(key=lambda keys: keys['R'], reverse=False)
                i = 0
                while i + 3 <= playernumber - 1:
                    if upper[i]['id'] in humanid or upper[i + 1]['id'] in humanid or upper[i + 2]['id'] in humanid or \
                            upper[i + 3]['id'] in humanid:
                        human_this_round_play = True
                        p1, p2, p3, p4 = playgame_human(upper[i], upper[i + 1], upper[i + 2], upper[i + 3], desk,
                                                        recordid,
                                                        humanid)
                    else:
                        p1, p2, p3, p4 = playgame(upper[i], upper[i + 1], upper[i + 2], upper[i + 3], desk, recordid)
                    players.append(p1)
                    players.append(p2)
                    players.append(p3)
                    players.append(p4)
                    i += 4
                while i <= playernumber - 1:
                    players.append(upper[i])
                    i += 1
            else:
                i = 0
                while i <= playernumber - 1:
                    players.append(upper[i])
                    i += 1
            desk += 1
        if desk == 3:
            playernumber = len(top)
            print('top desk:' + str(playernumber))
            if playernumber >= 500:
                random.shuffle(top)
                # reverse = random.randint(0, 1)
                # if reverse == 0:
                #     top.sort(key=lambda keys: keys['R'], reverse=True)
                # else:
                #     top.sort(key=lambda keys: keys['R'], reverse=False)
                i = 0
                while i + 3 <= playernumber - 1:
                    if top[i]['id'] in humanid or top[i + 1]['id'] in humanid or top[i + 2]['id'] in humanid or \
                            top[i + 3]['id'] in humanid:
                        human_this_round_play = True
                        p1, p2, p3, p4 = playgame_human(top[i], top[i + 1], top[i + 2], top[i + 3], desk, recordid,
                                                        humanid)
                    else:
                        p1, p2, p3, p4 = playgame(top[i], top[i + 1], top[i + 2], top[i + 3], desk, recordid)
                    players.append(p1)
                    players.append(p2)
                    players.append(p3)
                    players.append(p4)
                    i += 4
                while i <= playernumber - 1:
                    players.append(top[i])
                    i += 1
            else:
                i = 0
                while i <= playernumber - 1:
                    players.append(top[i])
                    i += 1
            desk += 1
        if desk == 4:
            i = 0
            playernumber = len(tenhou)
            print('tenhou:' + str(playernumber))
            while i <= playernumber - 1:
                players.append(tenhou[i])
                i += 1
            desk += 1
        print('*********************** Data Saving ************************')
        with open('profile.csv', 'w', newline='') as profile:
            csv_writer = csv.writer(profile)
            csv_writer.writerow(('id', 'sequence', 'level', 'pt', 'R', '1st', '2nd', '3rd', '4th'))
            for p in players:
                csv_writer.writerow(
                    (p['id'], p['seq'], all_level_list[p['level']], p['pt'], p['R'], p['1st'], p['2nd'], p['3rd'],
                     p['4th']))
            profile.close()
        # if not human_this_round_play:
        #     r -= 1

    normal.clear()
    up.clear()
    upper.clear()
    top.clear()
    tenhou.clear()
    players.clear()
    print('*********************** Round Over ************************')

# with open('profile.csv', 'w', newline='') as profile:
#     csv_writer = csv.writer(profile)
#     csv_writer.writerow(('id', 'sequence', 'level', 'pt', 'R', '1st', '2nd', '3rd', '4th'))
#     for p in players:
#         csv_writer.writerow(
#             (p['id'], p['seq'], all_level_list[p['level']], p['pt'], p['R'], p['1st'], p['2nd'], p['3rd'], p['4th']))
#     profile.close()

# with open('distribute.csv', 'w', newline='') as dis:
#     csv_writer = csv.writer(dis)
#     for q in distribute:
#         csv_writer.writerow(q)
#     dis.close()
