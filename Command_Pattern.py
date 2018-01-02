#Command Design Pattern

import abc

#the class that stores and executes the commands
class OneWhoNeedsCommands:
    def __init__(self):
        self.commands=[]

    def add_command(self,c):
        self.commands.append(c)

    def run_commands(self):
        for x in self.commands:
            x.execute()

#abstract Command Class
class CommandAbstract(metaclass=abc.ABCMeta):
    def __init__(self,OneWhoExecutesCommands):
        self.OneWhoExecutesCommands=OneWhoExecutesCommands

    def execute(self):
        pass

#Actual command class that holds the Class that actually knows how to run command
class CommandActual(CommandAbstract):
    def execute(self):
        self.OneWhoExecutesCommands.runParticualCommand()

#one who knows how to execute particulair command
class OneWhoExecutesCommands():

    def runParticualCommand(self):
        print("okies OneWhoExecutesCommands ran Particual Command ")


if __name__=="__main__":
    o=OneWhoExecutesCommands()
    c=CommandActual(o)
    ow=OneWhoNeedsCommands()
    ow.add_command(c)
    ow.run_commands()



