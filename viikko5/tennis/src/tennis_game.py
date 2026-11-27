class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score = self.p1_score + 1
        else:
            self.p2_score = self.p2_score + 1

    @classmethod
    def _get_tie_name(cls, score):
        if score == 0:
            return "Love-All"
        elif score == 1:
            return "Fifteen-All"
        elif score == 2:
            return "Thirty-All"
        else:
            return "Deuce"
      
    @classmethod  
    def _get_end_game_name(cls, score_diff):
        if score_diff == 1:
            return "Advantage player1"
        elif score_diff == -1:
            return "Advantage player2"
        elif score_diff >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
    @classmethod
    def _get_score_name(cls, score):
        match score:
            case 0: return "Love"
            case 1: return "Fifteen"
            case 2: return "Thirty"
            case 3: return "Forty"
            case _: raise ValueError(score)

    def get_score(self):
        score = ""

        if self.p1_score == self.p2_score:
            score = TennisGame._get_tie_name(self.p1_score)
        elif self.p1_score >= 4 or self.p2_score >= 4:
            score_diff = self.p1_score - self. p2_score
            score = TennisGame._get_end_game_name(score_diff)
        else:
            self.p1_score_name = TennisGame._get_score_name(self.p1_score)
            self.p2_score_name = TennisGame._get_score_name(self.p2_score)
            
            score = f"{self.p1_score_name} - {self.p2_score_name}"

        return score
