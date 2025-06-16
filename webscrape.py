from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://mytimetable.mcmaster.ca/criteria.jsp")
    page.wait_for_selector("#welcomeTerms > div:nth-child(1)")
    summer = page.query_selector("#welcomeTerms > div:nth-child(1)")
    term = str(summer.inner_html())
    start = term.split('(')[1]
    number = start.split(')')[0]
    summer_url = "https://mytimetable.mcmaster.ca/criteria.jsp?term="+number

    print(number)
    fall = page.query_selector("#welcomeTerms > div:nth-child(2)")
    term = str(fall.inner_html())
    start = term.split('(')[1]
    number = start.split(')')[0]
    print(number)
    fall_url = "https://mytimetable.mcmaster.ca/criteria.jsp?term="+number

    winter = page.query_selector("#welcomeTerms > div:nth-child(3)")
    term = str(winter.inner_html())
    start = term.split('(')[1]
    number = start.split(')')[0]
    print(number)
    winter_url = "https://mytimetable.mcmaster.ca/criteria.jsp?term="+number
    page.goto(winter_url)
    print(page)

    browser.close()