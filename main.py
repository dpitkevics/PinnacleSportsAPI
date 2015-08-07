from PinnacleSportsAPI.API import PinnacleSportsAPI

if __name__ == '__main__':
    api = PinnacleSportsAPI('DP804376', 'Hawks111!')
    sports_set = api.get_sports()

    sports = sports_set[0]

    league_set = api.get_leagues(sports.id)

    league = league_set[0]
