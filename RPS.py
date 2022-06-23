# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

play_order = {}

def player(prev_play, opponent_history=[]):
    
    
    steps = 3
    guess = 'R'
    
    opponent_history.append(prev_play)
    

    
    winnerPlays = {'R':'P','S':'R','P':'S'}
    
    
    if len(opponent_history) > steps:
                
    
        last_steps_2 = "".join(opponent_history[-(steps+1):])
        last_steps = "".join(opponent_history[-steps:])
        
        print(last_steps)
        
        if last_steps_2 in play_order.keys():
            play_order[last_steps_2] += 1
        else:
            play_order[last_steps_2] = 1
    
    
        potential_plays = [
            last_steps + "R",
            last_steps + "P",
            last_steps + "S",
        ]
        
        
        
        for i in potential_plays:
            if not i in play_order.keys():
                play_order[i] = 0
        
        print(potential_plays)
        print(play_order)
        prediction = max(potential_plays, key=play_order.get)[-1:]
        print(prediction)

        
        guess = winnerPlays[prediction]


    return guess
