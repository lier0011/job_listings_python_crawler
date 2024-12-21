import logging
import requests
import re
import json

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
        """ parse the information and save as LIST of DICTIONARY """
        # this is the json I found from the webiste
        snippet_pattern = r"(\{\"jobDetail\":\s*\{.*?\}.*?\})"
        result = re.findall(snippet_pattern, self.response.text, re.DOTALL)

        # prepare an empty LIST of jobs
        job_listing = []
        # now extract the job info into DICT
        for item in result:
            _json = json.loads(item)
            _detail = _json["jobDetail"]

            ref = {}
            ref["job_id"] = _detail["jobId"]
            ref["job_title"] = _detail["jobTitle"]
            ref["job_ad_date"] = _detail["displayDate"]
            ref["job_ad_expiry_date"] = _detail["expiryDate"]
            ref["job_location"] = _detail["displayLocationName"]
            ref["job_county_location"] = _detail["countyLocation"]
            ref["salary_from"] = _detail["salaryFrom"]
            ref["salary_to"] = _detail["salaryTo"]
            ref["remote_working_option"] = _detail["remoteWorkingOption"]
            ref["co_name"] = _json["profileName"]
            ref["job_url"] = "base_url" + "/jobs" + _json["url"]

            job_listing.append(ref)

        # save the list in object
        self.job_listing = job_listing

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

    # parse the content
    p.parse()
    print(p.job_listing)
    pass

    # write the output into csv
    p.write_csv()

if __name__ == "__main__":
    main()
