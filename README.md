StateBot
========

A Mastodon bot that outputs information regarding the state of the network collected from collectd.

## Requirements

Requires the `Mastodon.py` python module which you can find under that name on pypi.

## Usage

To run the bot set the following environment variables:

1.  `collectdAddress` - The address of the collectd server
2.  `collectdPort` - The port of the collectd server

Then type the following command:

````
python3 StateBot.py
````