

Jules BDD Automation Framework

Site tested: jules.app Design pattern used: page object model Methodology: behavior driven development

Libraries to install: pip install -U selenium pip install behave pip install behave-html-formatter pip install webdriver-manager

Run tests: behave -f html -o behave-report.html --tags=jules

Troubleshoot: a.IF pip doesn't work, try: py -m pip install selenium

b.If is still not working try: File -> Settings -> Click on Project: [project_name] -> Python Interpreter -> + look for 'selenium' -> Install Package Same for the rest

c.Click on 'Python Packages' Search and install packages
