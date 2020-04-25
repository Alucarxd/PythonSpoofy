import dns.resolver 


def main():
    try:
        objetivo = dns.resolver.query("archirow.com","MD")
        for x in objetivo:
            print(x)
    except:
        print("No pude conseguir informacion")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit