from game_engine.boardState import bgstate
masters = []
for move in ['1,1', '1,12', '1,17', '1,p', '17,1', '17,12', '17,17', '17,p', '19,1', '19,12', '19,17', '19,p', '1,1,R', '1,17,R', '1,19,R', '1,p,R', '12,1,R', '12,17,R', '12,18,R', '12,19,R', '12,p,R', '17,1,R', '17,17,R', '17,19,R', '17,p,R']:
    vals = [""]
    move = list(move)
    for i in move:
        if i != ",":
            vals[-1] += i
        else:
            vals.append("")
    masters.append(vals)
print(masters)


