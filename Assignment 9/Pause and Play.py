#remeber the high score prompt? Yeah, so take that and do a few thingS:
#1. make sure your high score saves to a text document called "highscore.txt"
#2. you can still hard code a high score, BUT 
#3. you need to check if the currently saved high score is in fact smaller than the proposed one
#if it is, overwrite the file with the new high score
#if it isnt, print out the current high score and challenge the user to try and beat it!
#(again, obviously no game has to be played here)




def main():
    file = "highscore.txt"
    proposed_score = 95

    f = open(file, "r")
    current_high_score = int(f.read())
    f.close()
    
    if proposed_score > current_high_score:
        f = open(file, "w")
        f.write(str(proposed_score))
        f.close()
        print(f"New high score! Your score of {proposed_score} beat the old high score.")
    else:
        print(f"The current high score is {current_high_score}. Try to beat it!")

main()
