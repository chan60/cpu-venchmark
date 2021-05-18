from selenium import webdriver as wd
driver = wd.Chrome(executable_path="./chromedriver.exe")
url = "https://www.cpubenchmark.net/high_end_cpus.html"
driver.get(url)
chart_list = driver.find_elements_by_css_selector("ul.chartlist li a span.prdname")

print(len(chart_list))
print(chart_list[5].get_attribute('innerHTML'))
