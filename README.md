iProwlerGox
===========

This is a Python script which monitors the current ฿TC ticker price via the Mt.Gox 'ticker_fast' API.

Installation
------------

Install Python on your computer

Install the 'prowler' Python module with pip (pip install prowler) or easy_install (easy_install prowler)

Go to http://www.prowler.com/ and register an account

Login to your account there, go to the API Keys tab and click Current API Keys > Generate Key

Paste the API Key given into the file iprowlergox.conf

All done!

Usage
-----

python iprowlergox.py low high

e.g.
	python iprowlergox.py 45 55

You will receive iOS notifications in your Prowler client when the price breaches the thresholds set, and a further notification when it crosses that threshold in the opposite direction.

Taking the above example, if the price rose to 55.2 you would receive an iOS notification. If it subsequently dropped below 55, you would receive another notification.

Copyright (c) 2013 Jay Fenton, released under the MIT license.

BTC Donations (entirely voluntary): 1HTcfFx4j6cf49Xg8H6nxz5C8TYRasHmkw

