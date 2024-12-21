class JobPortal():
    def __init__(self):
        """ constructor """
        pass

    def fetch(self):
        """ fetch the portal """
        pass

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
    p.fetch()
    p.parse()

    # write the output into csv
    p.write_csv()

if __name__ == "__main__":
    main()
