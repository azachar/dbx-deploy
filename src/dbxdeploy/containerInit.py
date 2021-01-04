from injecta.config.YamlConfigReader import YamlConfigReader
from injecta.container.ContainerInterface import ContainerInterface
from injecta.package.pathResolver import resolvePath
from pyfony.Kernel import Kernel
from pyfonybundles.loader import pyfonyBundlesLoader
from dbxdeploy.DbxDeployBundle import DbxDeployBundle

def initContainer(appEnv) -> ContainerInterface:
    bundles = [*pyfonyBundlesLoader.loadBundles(), DbxDeployBundle.autodetect()]

    kernel = Kernel(
        appEnv,
        resolvePath('dbxdeploy') + '/_config',
        bundles,
        YamlConfigReader()
    )

    return kernel.initContainer()
