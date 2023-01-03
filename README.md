# cloudflare_bypass_driver
chrome driver that wait until pass cloudflare imua challenge

# Dependency
selenium

undetected-chromedriver

```pip install selenium undetected-chromedriver```

# How to use
```python
from cloudflare_bypass_driver import Chrome

driver = Chrome(max_retry=3)
driver.get("https://nowsecure.nl/", bypass=True)
```

use ```max_retry``` to decide maximum times of challenge. default value is 3

if ```bypass``` value is True, driver.get() waits until IMUA challenge success. else it acts as normal chromedriver.

other options are same as undetected-chromedriver
