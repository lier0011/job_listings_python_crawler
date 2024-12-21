import logging
import requests
import re
import json
import os
import csv

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
            ref["job_ad_date"] = self.normalize_date(_detail["displayDate"])
            ref["job_ad_expiry_date"] = self.normalize_date(_detail["expiryDate"])
            ref["job_location"] = _detail["displayLocationName"]
            ref["job_county_location"] = _detail["countyLocation"]
            ref["salary_from"] = _detail["salaryFrom"]
            ref["salary_to"] = _detail["salaryTo"]
            ref["remote_working_option"] = _detail["remoteWorkingOption"]
            ref["co_name"] = _json["profileName"]

            # eliminate double /
            _job_url = self.base_url + "/jobs/" + _json["url"]
            ref["job_url"] = re.sub(r"\/{1,}", "/", _job_url, re.DOTALL)

            job_listing.append(ref)

        # save the list in object
        self.job_listing = job_listing

    def normalize_date(self, date_text):
        # normalise the date
        norm_date = ""
        regex_date = r"\d{4}\-\d{1,2}\-\d{1,2}"
        res_date = re.search(regex_date, date_text)
        if res_date is not None:
            norm_date = res_date.group(0)

        return norm_date

    def write_csv(self, filename):
        """ function to write csv """
        # define the filename of target csv
        target_file = os.path.join(os.getcwd(), "data", filename)
        log.info("target file path: " + target_file)

        with open(target_file, "w") as file:
            # first, get the keys of the DICT element for the csv header
            fieldnames = self.job_listing[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            # now generate the csv rows
            for idx in range(0, len(self.job_listing)):
                writer.writerow(self.job_listing[idx])

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

    # write the output into csv
    filename = "_".join(["jobs", keywords.lower(), location.lower(), "list.csv"])
    p.write_csv(filename)

if __name__ == "__main__":
    main()
