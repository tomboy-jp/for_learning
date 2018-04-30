import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://gihyo.jp/robots.txt")
rp.read()
rp.can_fetch('mybots', 'https://gihyo.jp/')
