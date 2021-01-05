import asyncio
from argparse import Namespace, ArgumentParser
from dbxdeploy.deploy.Deployer import Deployer
from consolebundle.ConsoleCommand import ConsoleCommand

class DeployCommand(ConsoleCommand):

    def __init__(
        self,
        deployer: Deployer
    ):
        self.__deployer = deployer

    def getCommand(self) -> str:
        return 'dbx:deploy'

    def getDescription(self):
        return 'Deploy to DBX'
    
    def configure(self, argumentParser: ArgumentParser):
        argumentParser.add_argument(dest='output', help='Target file path exported to local file once the command is done')

    def run(self, inputArgs: Namespace):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__deployer.deploy(inputArgs.output))
