import greeting
import config
import pars
import ex

def main():
    res = greeting.getTask()
    res = int(res)

    if res == 1:
        links = pars.getLinks(config.page_url, config.class_el)
        ex.saveLinks(links)

    if res == 2:
        pars.getContent()

if __name__ == "__main__":
    main()