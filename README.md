# Breakout - Easy-mode HTTP tunnels + Transparent Proxifiers

Chang Tan
Lister Unlimited Cybersecurity Solutions, LLC.
changtan@listerunlimited.com

# Purpose

This app lets you create a locally-forwarded HTTP tunnel so you can run commands to external hosts from behind a network with restrictive firewall settings, for example if they left port 80 and 443 open and won't let you connect remotely to a server with port 22 (SSH).

After running this script/app, you can now perform SSH commands via the `tsocks proxychains ssh` command.


# Requirements

Install ncat, which is auto-installed by default by nmap from your apt repo
You will also need tsocks (transparent proxifier) and proxychains

`apt-get update && apt-get install -y nmap tsocks proxychains`

# Installation

1. Git clone this repo
2. Install prerequisites as mentioned above
3. Run

`python prison-breakout.py`

