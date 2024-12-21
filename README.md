# job_listings_python_crawler

## INTRO
This program takes keywords and location as input parameter and do the job search on the 
job platform reed.co.uk. The result is provided as a csv file in the data subdirectory.

These are some screenshots:
* starting the program
![image](https://github.com/user-attachments/assets/34b283c0-cfe4-4403-9083-f730675beae1)

* csv output
![image](https://github.com/user-attachments/assets/a52f2230-480d-4c08-b439-7f3979b46bde)


## SYNTAX
To run the program:
<pre>python3 main.py [keywords] [location]</pre>

For example if we want to search for Typist in Manchester
<pre>python3 main.py Typist Manchester</pre>  

If the keywords contains whitespace than you have to escape it using quotation mark
<pre>python3 main.py "IT Support" Blackpool</pre>

## DESCRIPTION 

A coursera project to showcase how to scrape job listings from a popular job search platform.
At first, I thought I want to scrape the data from de.indeed.com. I did some research, analysis
and simple tests using curl on cli, just to check if I can access the website easily.
Unfortunately, I always got HTTP 403 forbidden. Hence I decided to access other alternative, reed.co.uk. 

Relevant information are going to be extracted, such as: job titles, companies, locations, job descriptions, etc.

Link to coursera Project: https://www.coursera.org/projects/scrape-job-postings-data-analyst

Here are the steps to do which I copied from coursera for this project:  

* Setup our development environment
* Understand the basics of web scraping
* Analyze the website structure of our job search platform
* Write the Python code to extract job data from our job search platform
* Save the data to a CSV file
* Test our web scraper and refine our code as needed



