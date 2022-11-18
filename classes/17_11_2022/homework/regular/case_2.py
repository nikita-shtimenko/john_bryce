MONTH_SEASON = [
    "Winter", # January
    "Winter", # February

    "Spring", # March
    "Spring", # April
    "Spring", # May

    "Summer", # June
    "Summer", # July
    "Summer", # August

    "Autumn", # September
    "Autumn", # October
    "Autumn", # November

    "Winter" # December
]

dates = []
dates_season = []

for i in range(0, 10):
    date = input("Enter date (ex: 01.01.2000): ")

    dates.append(date)
    dates_season.append(MONTH_SEASON[int(date[3:5]) - 1])

for season in ["Winter", "Spring", "Summer", "Autumn"]:
    print(f"\nYou entered {dates_season.count(season)} date(s) in {season}.")
    
    for index, date_season in enumerate(dates_season):
        if date_season == season:
            print(f"- {dates[index]}")