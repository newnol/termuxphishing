import os
#termux
os.system('pkg install git -y')
#linux
os.system('sudo apt install git -y')
#place the tool
os.system('''
cd
mkdir hack
cd hack
mkidr phishing
cd phishing
''')
#download for all tools
os.system('''
git clone https://github.com/htr-tech/nexphisher
git clone https://github.com/htr-tech/zphisher
git clone https://github.com/techchipnet/CamPhish
''')
