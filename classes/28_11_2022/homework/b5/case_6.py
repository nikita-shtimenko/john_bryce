def main():
    my_cities = {
        2008:
        {
            'Germany': ['Berlin', 'Munich'],
            'France' : ['Paris','Leon','Bordeaux']
        },
        2009: 
        {
            'China': ['Hong Kong', 'Shanghai','Beijing'],
            'Japan': ['Nagoya','Toyokawa','Yatomi'],
            'Mexico': ['Tijuana','Ecatepec']
        },
        2010: 
        {
            'Germany': ['Berlin', 'Dusseldorf'],
            'France': ['Paris', 'Nice', 'Bordeaux'],
            'Japan': ['Tokyo','Toyokawa','Yatomi']
        }
    }

    print(getCitiesVisitedYears(my_cities))
    return 1

def getCitiesVisitedYears(visited_cities_data: dict) -> dict:
    result = dict()

    for year, year_countries_data in visited_cities_data.items():
        for country_cities in year_countries_data.values():
            for city in country_cities:
                
                if city not in result.keys():
                    result[city] = [year]
                else:
                    result[city].append(year)

    return result

if __name__ == '__main__':
    main()