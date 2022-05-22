oldsep = input()
string = input().split(oldsep)
newsep = input()
print(*string, sep=newsep)