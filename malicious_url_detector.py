url = input('Enter the url: ').lower()

if url.startswith(('https://')): #  to check for http's'
    from urllib.parse import urlparse
    domain = urlparse(url).netloc 
    print(domain) #  www.example.test
    import socket #  module
    website=(domain) 
    IP_addres = socket.gethostbyname(website) #extracting ip address
    domain_name = socket.gethostbyaddr(website)[0] #checking ip address
    print("it is a valid url")
else:  
    print('its a malicious url')