import re
import string
import subprocess
import requests

versionslist = []
for lineofhtml in (requests.get("https://www.python.org/ftp/python/").text).split("\n"):
    lineofhtml = re.sub("  .*", "", str(lineofhtml))
versionsunpruned = re.findall('(?<=f=")(.*?)(?=\\")', str(lineofhtml))
    if versionsunpruned == [] or versionsunpruned == ["../"]:
        continue
    else:
        versionsunpruned = versionsunpruned[0]
    for letter in string.ascii_letters:
        if letter in versionsunpruned:
            valid = False
            break
        else:
            valid = True
    if valid:
        versionslist.append(versionsunpruned)


highestVersion = versionslist[-1].replace("/", "")
subprocess.call(
    f'curl -L -O https://www.python.org/ftp/python/{highestVersion}/Python-{highestVersion}.tar.xz && tar -xvf Python-{highestVersion}.tar.xz && cd Python-{highestVersion} && echo "Configuring Python Version {highestVersion}" && ./configure && echo "Making" && make && sudo make install',
    shell=True,
)

sys.exit(f"Done Installing Python {highestVersion}")
