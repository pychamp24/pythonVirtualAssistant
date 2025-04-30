from requests_html import HTMLSession
import speechToText

def weather():
    s = HTMLSession()
    query = "ghaziabad"
    url = f'https://www.google.com/search?q=weather+{query}&sca_esv=0ba5dac5fe5729a2&sxsrf=ADLYWIIeSLto-0e4UgTegUc2JejiquqBvA%3A1730568927143&ei=32ImZ5W8CPnL1e8P-vGimAM&ved=0ahUKEwjVp6XRl76JAxX5ZfUHHfq4CDMQ4dUDCA8&uact=5&oq=weather+{query}&gs_lp=Egxnd3Mtd2l6LXNlcnAiDXdlYXRoZXIgZGVsaGkyCBAAGIAEGLEDMg0QABiABBixAxhDGIoFMgoQABiABBhDGIoFMgUQABiABDIKEAAYgAQYQxiKBTIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEAAYgAQyCxAAGIAEGLEDGIMBSP4WUPQEWOsRcAB4ApABAJgB_gGgAfEHqgEFMC41LjG4AQPIAQD4AQGYAgWgAokFwgIEEAAYR5gDAIgGAZAGCJIHAzEuNKAH0CE&sclient=gws-wiz-serp'
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'})
    temp = r.html.find('span#wob_tm', first= True).text 

    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first= True).text

    discrip = r.html.find('#wob_dc', first=True).text

    return temp+" " + unit + " " + discrip