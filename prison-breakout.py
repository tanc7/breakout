#!/usr/bin/python
#coding=utf-8
import os, socket, sys, operator, threading, subprocess, re

os.system('clear')
print "Breakout, easy-mode HTTP tunneling using ncat and local port forwarding\nHelps in being able to run commands behind restrictive Wi-Fi network firewalls"

def popen_background(cmd):
    p = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o = p.stdout.read()
    o = str(o.encode('utf-8')).strip().rstrip()

    return o

def bash_cmd(cmd):
    cmd = cmd.splitlines()
    for line in cmd:
        subprocess.call(cmd, shell=True, executable='/bin/bash')
    return

def check_ncat():
    query = "ncat --listen --proxy-type http 127.0.0.1 443"
    cmd = "ps aux | egrep -i ncat"
    output = popen_background(cmd)
    if re.search(query, output):
        pass
    else:
        bash_cmd(query + " &")
        print "Local HTTP Proxy created on localhost, port 443"
    return

def check_proxychains_conf():
    cmd = "cat /etc/proxychains.conf  | egrep -vi \# | awk 'NF'"
    output = popen_background(cmd)
    # lines = output.splitlines()
    query = ""
    if re.search(query, output):
        pass
    else:
        bash_cmd("echo 'http 127.0.0.1 443 >> /etc/proxychains.conf'")
        print "Line added to let proxychains proxify your traffic to port 443"
    return

def main():
    check_ncat()
    check_proxychains_conf()
    commands = """ps aux | egrep -i ncat
    netstat -antp | egrep -i 443
    tsocks proxychains ssh -NfD root@localhost""".strip().rstrip()
    bash_cmd(commands)
    print "\n\n\nFinished, you can now prepend any command to have it routed through HTTPS with the 'tsocks proxychains command'\n\n\nChang Tan\nLister Unlimited Cybersecurity Solutions, LLC"

    return
main()
