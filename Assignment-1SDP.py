class High_Score:
    __instance = None
    score = 0
    
    def __new__(cls, score):
        if cls.__instance is None:
            cls.__instance = super(High_Score, cls).__new__(cls)
        return cls.__instance
    
    def __init__(self, score):
        self.score = score
    
    def view_highest(self):
        print(self.score)


score1 = High_Score(133)

print(score1)
print(score1.score)

score2 = High_Score(120)

print(score2)
print(score2.score)
print(score1 == score2)