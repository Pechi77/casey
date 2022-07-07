BOT_NAME = "case_research"

SPIDER_MODULES = ["case_research.spiders"]
NEWSPIDER_MODULE = "case_research.spiders"

# my sql data
MYSQL_DB = "case_research_traffic"
MYSQL_USERNAME = "admin"
MYSQL_PASSWORD = "admin"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'case_research (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    "case_research.pipelines.CaseResearchPipeline": 300,
    "case_research.pipelines.MySQLPipeline": 400,
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Adding Aut-throttle to avoid getting 403's
AUTOTHROTTLE_ENABLE = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 20
DOWNLOAD_DELAY = 2

# https://casesearch.courts.state.md.us/casesearch/inquiry-results.jsp?d-16544-p=1&lastName=A%25&filingDate=&filingEnd=7%2F6%2F2022&partyType=DEF&courtSystem=B&courttype=N&firstName=&site=TRAFFIC&searchTrialPersonAction=Search&searchtype=zuwnScB3grRM4sXvyZ%2FkQrgKF1xs%2BWCcHyeeAYDsyHoD1IHPhqRQSXEsSJJSKFj20fDgUB%2BrRxQO1uaNhxFo7mgBraOmbEorqYpqKOsWQNM%3D&filingStart=7%2F1%2F2022&company=N&middleName=&countyName=

# https://casesearch.courts.state.md.us/casesearch/inquiry-results.jsp?d-16544-p=1&lastName=A%25&filingDate=&filingEnd=7%2F6%2F2022&partyType=DEF&courtSystem=B&courttype=N&firstName=&site=TRAFFIC&searchTrialPersonAction=Search&filingStart=7%2F1%2F2022&company=N&middleName=&countyName=