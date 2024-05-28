BROWSERS_TOKEN = {
  'Edg/': 'Edge',
  'EdgA/': 'Edge',
  'Chrome/': 'Chrome',
  'CriOS/': 'Chrome',
  'Safari/': 'Safari',
  'Firefox/': 'Firefox',
}

DEVICES_TOKEN = {
  'Android': 'Android',
  'iPhone': 'iPhone',
  'Windows': 'Windows',
  'Macintosh': 'Macintosh',
  'Linux': 'Linux',
}

def parse_ua(string):
    browser = 'Other'
    device = 'Other'
    for TOKEN in BROWSERS_TOKEN:
        if TOKEN in string:
            browser = BROWSERS_TOKEN[TOKEN]
            break
    for TOKEN in DEVICES_TOKEN:
        if TOKEN in string:
            device = DEVICES_TOKEN[TOKEN]
            break
    return browser, device