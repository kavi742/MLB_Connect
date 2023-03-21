import statsapi

#input player name and print their current team
#make sure only one player is searched
playerName = input("enter player name : ")
for player in statsapi.lookup_player(playerName):
    teamID = player['currentTeam']
    print('{}'.format(player['currentTeam']))
for team in statsapi.lookup_team("tor"):
    print(team[0]['name'])
