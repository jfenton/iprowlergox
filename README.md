iProwlerGox
===========

This is a Python script which monitors the current ฿TC ticker price via the Mt.Gox 'ticker_fast' API, and sends notifications to your iPhone/iPad device using the Prowler service.

Installation
------------

1) Install Python

2) Install the 'prowler' and 'simplejson' Python modules with pip or easy_install

```pip install prowler simplejson
or
easy_install prowler simplejson```

3) Go to http://www.prowler.com/ and register an account

4) Login to your account there, go to the API Keys tab and click Current API Keys > Generate Key

5) Paste the API Key given into the file iprowlergox.conf

All done!

Usage
-----

```python iprowlergox.py 45 55```

Where 45 and 55 are the low and high watermarks respectively that you want to use. The script checks the ticker price at Gox every 5 seconds at present.

You will receive iOS notifications in your Prowler client when the price breaches the thresholds set, and a further notification when it crosses that threshold in the opposite direction i.e. if the price were 54 and then rose to 55.2, you would receive your first iOS notification. If it subsequently dropped below 55, you would receive another notification.

License
-------

Copyright (c) 2013 Jay Fenton, released under the MIT license.

BTC Donations (entirely voluntary): 1HTcfFx4j6cf49Xg8H6nxz5C8TYRasHmkw

