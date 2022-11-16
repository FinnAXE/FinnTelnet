from telnetlib import Telnet

print('''
          _____   ____   ____   ____
        /  ___/  /   /  /    |/    /
       /  /__   /   /  /          /  __    __
      /  ___/  /   /  /   /|     /  /  | /  /
     /  /     /   /  /   / |    /  /  /|   /
    /__/     /___/  /___/  |___/  /__/ |__/                                             
-Finn, a product created by Claudio Lo Preiato 
-Finmeccanic Calabria S.R.L 
 ''')

print('[+] input the IP address you want to connect (WARNING! only telnet connection)\n')

def main():
    ip = input()
    try:
        with Telnet(ip, 23) as tn:
            tn.interact()
    except:
        print('!!! Failed to connect or connection closed on the IP address')
    finally:
        print('[+] input the IP address you want to connect \n')
        main()
main()
