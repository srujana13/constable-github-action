class GQLQuery:
    queries = {'GET_REPO_FILES' : 'get_repo_files',
               'CHECK_VALID_REPO' : 'check_valid_repo',
               'GET_CLOSED_ISSUES': 'get_closed_issues'}

    def __init__(self, path=None):
        if not path:
            raise FileNotFoundError('No valid path provided')
        else:
            self.path = path

    def load(self, query_name):
        if query_name not in self.queries: raise FileNotFoundError('Not a valid query name. Refer GQLQuery.queries')
        return open(self.path + '{}.graphql'.format(self.queries[query_name])).read()