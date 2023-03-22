class NBAPredictor:
    @staticmethod
    def predictWinner(team1Stats, team2Stats):
        # Calculate each team's total score based on their stats
        team1Score = NBAPredictor.calculateScore(team1Stats)
        team2Score = NBAPredictor.calculateScore(team2Stats)
        
        # Compare the scores to predict the winner
        if team1Score > team2Score:
            winningScore = team1Score
            return f"Team 1 is predicted to win! ({winningScore} points)"
        elif team2Score > team1Score:
            winningScore = team2Score
            return f"Team 2 is predicted to win! ({winningScore} points)"
        else:
            # If the scores are tied, return the team with the higher score in points as the winner
            if team1Stats["Points"] > team2Stats["Points"]:
                winningScore = team1Score
                return f"Team 1 is predicted to win! ({winningScore} points)"
            else:
                winningScore = team2Score
                return f"Team 2 is predicted to win! ({winningScore} points)"
    
    @staticmethod
    def calculateScore(stats):
        # Assign a weight to each statistic (these weights can be adjusted as needed)
        pointsWeight = .8
        reboundsWeight = .25
        assistsWeight = .3
        stealsWeight = .5
        blocksWeight = .5
        
        # Calculate the score based on the weighted stats
        score = stats["Points"] * pointsWeight \
                + stats["Rebounds"] * reboundsWeight \
                + stats["Assists"] * assistsWeight \
                + stats["Steals"] * stealsWeight \
                + stats["Blocks"] * blocksWeight
        
        return score
    
    @staticmethod
    def getTeamStats(teamNum):
        print(f"Enter stats for Team {teamNum}:")
        points = float(input("Points: "))
        rebounds = float(input("Rebounds: "))
        assists = float(input("Assists: "))
        steals = float(input("Steals: "))
        blocks = float(input("Blocks: "))
        ortg = float(input("Offensive Rating: "))
        drtg = float(input("Defensice Rating: "))
        
        return {"Points": points, "Rebounds": rebounds, "Assists": assists, "Steals": steals, "Blocks": blocks}
    
    @staticmethod
    def printWinningScore(team1Stats, team2Stats):
        winner = NBAPredictor.predictWinner(team1Stats, team2Stats)
        if "Team 1" in winner:
            winningScore = NBAPredictor.calculateScore(team1Stats)
        else:
            winningScore = NBAPredictor.calculateScore(team2Stats)
        print(f"The winning team's calculated score is {winningScore}.")


team1Stats = NBAPredictor.getTeamStats(1)
team2Stats = NBAPredictor.getTeamStats(2)

winner = NBAPredictor.predictWinner(team1Stats, team2Stats)

print(winner)

NBAPredictor.printWinningScore(team1Stats, team2Stats)
