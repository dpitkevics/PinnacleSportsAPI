from PinnacleSportsAPI.API import PinnacleSportsAPI

if __name__ == '__main__':
    api = PinnacleSportsAPI('DP804376', 'Hawks111!')
    sports_set = api.get_sports()

    for sports in sports_set:
        print(sports.id)
        print(sports.name)
