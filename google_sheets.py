import pygsheets

gc = pygsheets.authorize(service_account_file='path/to/key.json')

survey_url = 'https://docs.google.com/spreadsheets/d/1LVt17F4_7z_8gEz9DR51eBI4mNLxfiFnIcgCuHRe1D4/'
sh = gc.open_by_url(survey_url)
