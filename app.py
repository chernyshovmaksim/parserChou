import modules.config
import modules.pars
import modules.ex
import eel


def main():
    eel.init('interface')

    @eel.expose
    def getAction(param):
        return param

    eel.start('app.html', size=(700, 300))


if __name__ == "__main__":
    main()
