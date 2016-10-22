import xmlsoccer

xmls = xmlsoccer.XmlSoccer(api_key = "CJLWGIFMFFDGRIXTRUFZHLFXPNDQAKSONGUOPRIZCKVAHDIERJ" , use_demo=True)

fixtures = xmls.call_api(method='GetPlayoffFixturesByLeagueAndSeason',league='Scottish Premier League')

print(fixtures)
