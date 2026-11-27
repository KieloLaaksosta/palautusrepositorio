END_GAME_SCORE = 4

class TennisGame:        
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.p1_name:
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
    def _get_end_game_name(cls, p1_score, p2_score):
        if p1_score > p2_score:
            if p1_score == p2_score + 1:
                return "Advantage player1"
            else:
                return "Win for player1"
        else:
            if p2_score == p1_score + 1:
                return "Advantage player2"
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
        if self.p1_score == self.p2_score:
            return TennisGame._get_tie_name(self.p1_score)
        elif self.p1_score >= END_GAME_SCORE or self.p2_score >= END_GAME_SCORE:
            return TennisGame._get_end_game_name(self.p1_score, self.p2_score)
        else:
            self.p1_score_name = TennisGame._get_score_name(self.p1_score)
            self.p2_score_name = TennisGame._get_score_name(self.p2_score)
            
            return f"{self.p1_score_name}-{self.p2_score_name}"
