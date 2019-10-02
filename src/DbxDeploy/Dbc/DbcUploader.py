from base64 import b64encode
from databricks_api import DatabricksAPI
from DbxDeploy.Setup.Version.VersionInterface import VersionInterface
from requests.exceptions import HTTPError

class DbcUploader:

    def __init__(self, dbxProjectRoot: str, dbxApi: DatabricksAPI):
        self.__dbxProjectRoot = dbxProjectRoot
        self.__dbxApi = dbxApi

    def upload(self, dbcContent: bytes, version: VersionInterface):
        contentToUpload = b64encode(dbcContent).decode()

        try:
            self.__performUpload(contentToUpload, version)
        except HTTPError:
            self.__dbxApi.workspace.mkdirs(self.__dbxProjectRoot)
            self.__performUpload(contentToUpload, version)

        try:
            self.__dbxApi.workspace.delete(
                self.__dbxProjectRoot + '/_current',
                recursive=True,
            )
        except HTTPError:
            pass

        self.__dbxApi.workspace.import_workspace(
            self.__dbxProjectRoot + '/_current',
            format='DBC',
            content=contentToUpload
        )

    def __performUpload(self, contentToUpload, version):
        self.__dbxApi.workspace.import_workspace(
            version.getDbxVersionPath(self.__dbxProjectRoot),
            format='DBC',
            content=contentToUpload
        )
