# saved as Server.py
import  Pyro4
import  random
import  os


@Pyro4.expose
class Kerberos(object):
    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Tomorrow's lucky number is {1}.".format(name, random.randint(0, 1000))

    def sum(self, a, b):
        return "{0} + {1} = {2}".format(a, b, int(a) + int(b))

    # def sendfile(self, fname):
    #     if fname in os.listdir('./Server/'):
    #         print("Sending " + str(fname))
    #         return open('./Server/' + str(fname), "rb").read()
    #     else:
    #         return None
    #
    #
    # def listdir(self):
    #      return os.listdir('./Server/')