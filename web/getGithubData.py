from gql import gql, Client, AIOHTTPTransport
from gqlquery import GQLQuery
import config

class Github:
    def __init__(self, auth_token):
        transport = AIOHTTPTransport(url="https://api.github.com/graphql", 
                    headers={'Authorization': 'token {}'.format(auth_token)})
        self.client = Client(transport=transport, fetch_schema_from_transport=True)
        self.gql_query = GQLQuery(config.DIR_PATH + "/queries/")

    def get_repo_files(self, repo_name):
        query = self.gql_query.load(query_name='GET_REPO_FILES')
        result = self.client.execute(gql(query), variable_values={"name": repo_name})
        file_names = [file['name'] for file in result['viewer']['repository']['object']['entries']]
        return file_names
    
    def check_valid_repo(self, repo_name):
        query = self.gql_query.load(query_name='CHECK_VALID_REPO')
        result = self.client.execute(gql(query), variable_values={"name": repo_name})
        valid = True if result['viewer']['repository'] else False
        return valid

    def get_closed_issues(self, repo_name, owner, start_date):
        query = self.gql_query.load(query_name='GET_CLOSED_ISSUES')
        result = self.client.execute(gql(query), variable_values={"repo": repo_name, "owner": owner, "start_date": start_date})
        issues = result['repository']['issues']['totalCount']
        return issues
        