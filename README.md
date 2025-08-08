# AutoUpdate
PYPI PROJECT
A Python package to automatically find software updates of your repositories in GitHub

[![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white)](https://discord.gg/qD8SXrRJbw) [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/ili.hazard) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://youtube.com/@iiihazard) 

[![Updated Badge](https://badges.pufler.dev/updated/Pytholearn/found_update)](https://github.com/Pytholearn/found_update)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)



how does it work:

Step 1:
Go to your desired repository and create a file named version (don't give it a .txt extension)
And write your code in that version.

<picture>
  <img alt="write your code in that version." src="https://cdn.discordapp.com/attachments/1268584313763401749/1268585830574719046/6jR45QP.png?ex=66acf61f&is=66aba49f&hm=15be35caa7a1b2af851cafc61f7e4423170b14bcc005139293cbe96ae9dcdbf8&">
</picture>

Step 2:
Right click on the raw option and copy the link

<picture>
  <img alt="Right click on the raw option and copy the link" src="https://cdn.discordapp.com/attachments/1268584313763401749/1268587064237228062/EvHRGqn.png?ex=66acf745&is=66aba5c5&hm=0c9e77f0c0eb9060fc2ad7fb98941b6ff2fe4cf16220c6cdfe4d591fc21b91bc&">
</picture>



Usage example:
```py
from autoupdate import *

autoupdate.set_url("https://raw.githubusercontent.com/Pytholearn/Proxy-Checker-2/refs/heads/main/version")
autoupdate.set_current_version("1.8.9")
autoupdate.set_download_link("https://github.com/Pytholearn/Proxy-Checker-2.git")

if not autoupdate.is_up_to_date():
    print("Would you like to update your tool?")
    choice = input("Enter (y/n): ")
    if choice == "y":
       autoupdate.update()
    else:
        pass

```

## FAQ

#### For Help: https://discord.gg/qD8SXrRJbw








