import http_tools
import parser

maxRent = 1300
city = 'Utrecht'
pararius_query = "https://www.pararius.nl/huurwoningen/utrecht/0-1300"


def scrape_all():
    return 0


def scrape_pararius():
    response = http_tools.get_html_response(pararius_query)
    return parser.parse_pararius(response)

def scrape_woningnet():
    return 0


def scrape_marktplaats():
    return 0


def test():
    scrape_pararius()


if __name__ == "__main__":
    test()