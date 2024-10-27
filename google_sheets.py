import pygsheets

gc = pygsheets.authorize(service_account_file='path/to/key.json')

survey_url = 'https://docs.google.com/spreadsheets/d/1cNqBIzF_T8yZm5S1hj7E1MNVXQegVDVuJsUWVoDKIDw/'
sh = gc.open_by_url(survey_url)
print(sh)
