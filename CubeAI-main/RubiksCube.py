# class RubiksCube():
#     # variables to keep track of the colors
#     Red = 'R'
#     Orange = 'O'
#     Yellow = 'Y'
#     Green = 'G'
#     Blue = 'B'
#     White = 'W'

#     # 
#     face_one = 1
#     face_two = 2
#     face_three = 3
#     face_four = 4
#     face_five = 5
#     face_six = 6


MOVES = {

    "U": [2,  0,  3,  1, 20, 21,  6,  7,  4,  5, 10, 11, 12, 13, 14, 15,  8,  9, 18, 19, 16, 17, 22, 23],
    "U'": [1,  3,  0,  2,  8,  9,  6,  7, 16, 17, 10, 11, 12, 13, 14, 15, 20, 21, 18, 19,  4,  5, 22, 23],
    "R": [0,  9,  2, 11,  6,  4,  7,  5,  8, 13, 10, 15, 12, 22, 14, 20, 16, 17, 18, 19,  3, 21,  1, 23],
    "R'": [0, 22,  2, 20,  5,  7,  4,  6,  8,  1, 10,  3, 12, 9, 14, 11, 16, 17, 18, 19, 15, 21, 13, 23],
    "F": [0,  1, 19, 17,  2,  5,  3,  7, 10,  8, 11,  9, 6,  4, 14, 15, 16, 12, 18, 13, 20, 21, 22, 23],
    "F'": [0,  1,  4,  6, 13,  5, 12,  7,  9, 11,  8, 10, 17, 19, 14, 15, 16,  3, 18,  2, 20, 21, 22, 23],
    "D": [0,  1,  2,  3,  4,  5, 10, 11,  8,  9, 18, 19, 14, 12, 15, 13, 16, 17, 22, 23, 20, 21,  6,  7],
    "D'": [0,  1,  2,  3,  4,  5, 22, 23,  8,  9,  6,  7, 13, 15, 12, 14, 16, 17, 10, 11, 20, 21, 18, 19],
    "L": [23,  1, 21,  3,  4,  5,  6,  7,  0,  9,  2, 11, 8, 13, 10, 15, 18, 16, 19, 17, 20, 14, 22, 12],
    "L'": [8,  1, 10,  3,  4,  5,  6,  7, 12,  9, 14, 11, 23, 13, 21, 15, 17, 19, 16, 18, 20,  2, 22,  0],
    "B": [5,  7,  2,  3,  4, 15,  6, 14,  8,  9, 10, 11, 12, 13, 16, 18,  1, 17,  0, 19, 22, 20, 23, 21],
    "B'": [18, 16,  2,  3,  4,  0,  6,  1,  8,  9, 10, 11, 12, 13,  7,  5, 14, 17, 15, 19, 21, 23, 20, 22],

}

'''
sticker indices:
       0  1
       2  3
16 17  8  9   4  5  20 21
18 19  10 11  6  7  22 23
       12 13
       14 15
face colors:
    0
  4 2 1 5
    3
moves:
[ U , U', R , R', F , F', D , D', L , L', B , B']

'''

class RubiksCube:

    def __init__(self, string="WWWW RRRR GGGG YYYY OOOO BBBB", moves=[], parent=None, depth=0, f=0):
        self.state = self.cleanState(string)
        self.moves = moves
        self.parent = parent
        self.depth = depth
        self.f = f

    
    def cleanState(self, state):
        state = state.replace(" ", "")
        state = state.upper()

        if len(state) != 24:
            raise ValueError("Invalid state, must have exactly 24 squares")
        
        colors = ["W", "R", "G", "Y", "O", "B"]
        for color in colors:
            if state.count(color) != 4:
                raise ValueError("Invalud state, Incorrect number of colors")
        
        return state
    

    def __str__(self):
        s = self.state
        cubeStr = "   {}{}      \n".format(s[0], s[1])
        cubeStr += "   {}{}      \n".format(s[2], s[3])
        cubeStr += "{}{} {}{} {}{} {}{}\n".format(
            s[16], s[17], s[8], s[9], s[4], s[5], s[20], s[21])
        cubeStr += "{}{} {}{} {}{} {}{}\n".format(
            s[18], s[19], s[10], s[11], s[6], s[7], s[22], s[23])
        cubeStr += "   {}{}      \n".format(s[12], s[13])
        return cubeStr + "   {}{}      \n".format(s[14], s[15])
    

    def printSequence(self, moves):
        s1 = str(self)
        n = 0
        for move in moves:
            n += 1
            if n == 3:
                n = 0
                print(s1)
                self.state = self.applyMove(self.state, move)
                s1 = str(self)
                continue
            self.state = self.applyMove(self.state, move)
            s2 = str(self)
            s1 = "\n".join([" ".join(s3) for s3 in zip(s1.split("\n"), s2.split("\n"))])
            print(s1)
    

    def isSolved(self):
        for i in range(0, len(self.state), 4):
            side = self.state[i:i+4]
            if side.count(side[0]) != 4:
                return False
        return True
    

    def equals(self, cube):
        return self.norm(self.state) == self.norm(cube.state)
    

    def clone(self):
        return self.state
    

    def applyMovesStr(self, alg):
        state = self.clone()

        for move in alg.split():
            state = self.applyMove(state, move)
        return state
    

    def applyMove(self, state, move):
        if move not in MOVES.keys():
            raise valueError("Invalid move")


            perm = MOVES[move]
            state = "".join([state[i] for i in perm])
            return state
    
    def norm(self, state):
        state = self.cleanState(state)
        opps = {"O": "R", "G": "B", "Y": "W", "R": "O", "B": "G", "W": "Y"}

        s0, s1, s2 = state[10], state[12], state[19]
        o0, o1, o2 = opps[s0], opps[s1], opps[s2]

        mapping = {s0: "G", s1: "Y", s2: "O", o0: "B", o1: "W", o2: "R"}

        normState = ""
        for s in state:
            normState += mapping[s]
        return normState

    def shuffle():
        return null


    def print(self):
        print(str(self))
    

    def main():
        RubiksCube.print(self)
        
        print("Hello")
    

    if __name__ == "__main__":
        main()

