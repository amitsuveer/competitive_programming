import sys

def game_result(game:dict):
    
    num_shots = game['num_shots']
    shot_cord = game['shots']
    
    if num_shots != len(shot_cord):
        return     
    
    p1_deployment, p2_deployment = game['p1'], game['p2']
    
    # player-1 is always starting the game
    is_p1 = True
    for shot_id, shot in enumerate(shot_cord):
        if is_p1:
            # player-1 is attacking
            if shot in p2_deployment:
                #print(f'P1: {shot} - hit')
                #print(f'p2_deployment before hit = {p2_deployment}')
                idx = next(i for i, val in enumerate(p2_deployment) if val == shot)
                #print(f'hit-p2 at index = {idx}')        
                p2_deployment.pop(idx)
                #print(f'p2_deployment after hit = {a}')
            else:
                # p1 missed, toggle the turn
                #print(f'P1: {shot} - missed')
                is_p1 ^= 1                
        else:
        #elif is_p2:
            # player-2 is attacking
            if shot in p1_deployment:
                #print(f'P2: {shot} - hit')
                #print(f'p1_deployment before hit = {p1_deployment}')
                idx = next(i for i, val in enumerate(p1_deployment) if val == shot)
                #print(f'hit-p1 at index = {idx}')        
                p1_deployment.pop(idx)
                #print(f'p1_deployment after hit = {a}')
            else:
                # p2 missed, toggle the turn
                #print(f'P2: {shot} - missed')
                is_p1 ^= 1                

    # end for!
    
    if len(p1_deployment):
        # p1 didn't loos, check for draw
        print('draw') if len(p2_deployment) else print('player one wins')
    elif len(p2_deployment):
        # p2 didn't loos, check for draw
        print('draw') if len(p1_deployment) else print('player two wins')        
    else:
        print('draw')
        


if __name__ == '__main__':
    
    lines = sys.stdin.readlines()

    ship='#'
    cases = int(lines[0])

    case_cnt, map_h, map_w, num_shots = 0, 0, 0, 0

    dict_cases = {}
    for c in range(cases):
        game_details = {}

        case_cnt += 1    
        case_name = f'Case {case_cnt}'
        line_idx = case_cnt + map_h + map_w + num_shots

        map_w, map_h, num_shots = (lines[line_idx]).split()
        map_w, map_h, num_shots = int(map_w), int(map_h), int(num_shots)

        # Deployment player - 1
        ship_cords_p1 = []
        for h in  range(map_h):
            line_idx += 1        
            y = map_h - h - 1
            row = lines[line_idx]
            # get ship location in row and append 
            # with previously found location 
            if ship in row:
                x_indices = [i for i, x in enumerate(row) if x==ship]
                cords = [(x, y) for x in x_indices]
                for loc in cords:
                    ship_cords_p1.append(loc)

        # Deployment player - 2
        ship_cords_p2 = []
        for h in  range(map_h):
            line_idx += 1        
            y = map_h - h - 1
            row = lines[line_idx]
            # get ship location in row and append 
            # with previously found location 
            if ship in row:
                x_indices = [i for i, x in enumerate(row) if x==ship]
                cords = [(x, y) for x in x_indices]
                for loc in cords:
                    ship_cords_p2.append(loc)

        # Shots details
        shots_cords = []
        for s in range(num_shots):
            line_idx += 1
            x, y = lines[line_idx].split()
            shots_cords.append((int(x), int(y)))

        # Fill-in map and shots info
        #game_details['map_w'] = int(map_w)
        #game_details['map_h'] = int(map_h)
        game_details['num_shots'] = int(num_shots)
        game_details['p1'] = ship_cords_p1
        game_details['p2'] = ship_cords_p2
        game_details['shots'] = shots_cords

        dict_cases[case_name] = game_details



    for case, game in dict_cases.items():
        #print(case)
        game_result(game)