import random

batter = raw_input("What is your name, batter?")

print "Next batter, " + batter + "!"

swing_hit = ["Strike","Single","Homerun","Double","Triple","Foul"]

no_swing = ["Strike", "Ball"]

pitch = ["4-seam Fastball","2-seam fastball (sinker)",
"2-seam fastball (runs)","Cut Fastball","Slider","Curveball","Slurve","Change-up","Split Finger","Knuckle ball"]

strike = 0
hit = False
ball = 0

while (strike < 3) and (hit == False) and (ball < 4):
    pitch_thrown = (random.choice(pitch))
    action_taken = raw_input(pitch_thrown + " is thrown. Did you swing? (yes or no)")
    
    if action_taken == "yes":
        swing_outcome = random.choice(swing_hit)
        if swing_outcome != "Strike" and swing_outcome != "Foul":
            print swing_outcome+"!"
            hit = True
        else:
            if swing_outcome == "Strike":
                strike+=1
                print swing_outcome + " " + str(strike) + "!"
            if swing_outcome == "Foul":
                if strike < 2:
                    strike+=1
                print swing_outcome + "!"
    elif action_taken == "no":
        no_swing_outcome = random.choice(no_swing)
        if no_swing_outcome == "Strike":
            strike+=1
            print no_swing_outcome + " " + str(strike) + "!"
        if no_swing_outcome == "Ball":
            ball+=1
            print no_swing_outcome + " " + str(ball) + "!"
    else:
        print "Please enter yes or no!"
		        
if strike == 3:
    print "You're out!"
    
if ball == 4:
    print "Walk to first base!"






