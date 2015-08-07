from PinnacleSportsAPI.API import PinnacleSportsAPI

if __name__ == '__main__':
    api = PinnacleSportsAPI('DP804376', 'Hawks111!')
    sports_set = api.get_sports()

    # for sports in sports_set:
    #     print('%s - %s' % (sports.id, sports.name))

    sports = sports_set[28]

    league_set = api.get_leagues(sports.id)

    league = league_set[0]

    feed = api.get_feed(is_live=True)

    feed_sport = feed.feed_type.feed_sport_set[0]
    print(feed_sport.league_set[0].event_set[0].home_team.name)
