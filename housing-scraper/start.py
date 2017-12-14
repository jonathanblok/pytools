import database_connector
import scraper
import notifier
import validator


def main():
    while 1:
        entrylist = scraper.scrape_all()

        for entry in entrylist:
            if validator.is_unique(entry):
                database_connector.store(entry)
                notifier.notify(entry)


if __name__ == "__main__":
    main()
