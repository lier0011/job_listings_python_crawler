import logging
import requests

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class JobPortal():
    def __init__(self):
        """ constructor """
        self.base_url = "https://www.reed.co.uk"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        log.info("initialise job portal: " + self.base_url)

    def fetch(self, key, loc):
        """ Scrape the portal """
        log.info("starting to scrape the job platform")

        # check passed args
        query_url = ""
        if key != "" and loc != "":
            log.info("both args passed, key: {} + loc: {}".format(key, loc))
            query_url = "/jobs?keywords={}&location={}&proximity=10".format(key, loc)
        else:
            raise Exception("no args (keywords + location) passed")

        # call the URL
        self.url = self.base_url + query_url
        log.info("fetching url " + self.url)

        # save response into object
        self.response = requests.get(self.url, headers=self.headers)
        log.info("status_code: " + str(self.response.status_code))

    def parse(self):
        """ parse the information """
        pass

    def write_csv(self):
        """ write data into csv """
        pass

def main():
    # initialise job portal
    p = JobPortal()
    print(p)

    # scrape the job information
    keywords = "Python"
    location = "Blackpool"
    p.fetch(keywords, location)
    print(p.response)
    pass
    p.parse()

    # write the output into csv
    p.write_csv()

if __name__ == "__main__":
    main()
