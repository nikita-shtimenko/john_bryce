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

    print(getVisitedCities(my_cities))
    return 1

def getVisitedCities(visited_cities_data: dict) -> set[str]:
    result = set()

    for country_data in visited_cities_data.values():
        for cities_data in country_data.values():
            for city in cities_data:
                result.add(city.capitalize())

    return result

if __name__ == '__main__':
    main()