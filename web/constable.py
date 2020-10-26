from getGithubData import Github
from datetime import datetime, timedelta

class Constable:
    def __init__(self, repo_name, owner, github_instance):
        self.repo_name = repo_name
        self.owner = owner
        self.github_instance = github_instance
        self.required_files = ['README.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'LICENSE', 'CITATION.md', '.gitignore']
    
    def get_score(self):
        score_dict = {}
        score = 0
        repo_files = self.github_instance.get_repo_files(self.repo_name)
        for repo_file in repo_files:
            if repo_file == 'README.md':
                score += 1
                score_dict['README.md'] = 1
            if repo_file == 'CONTRIBUTING.md':
                score += 1
                score_dict['CONTRIBUTING.md'] = 1
            if repo_file == 'CODE_OF_CONDUCT.md':
                score += 1
                score_dict['CODE_OF_CONDUCT'] = 1
            if repo_file == 'LICENSE':
                score += 1
                score_dict['LICENSE'] = 1
            if repo_file == 'CITATION.md':
                score += 1
                score_dict['CITATION.md'] = 1
            if repo_file == '.gitignore':
                score += 1
                score_dict['.gitignore'] = 1
        absent_files = [reqd_file for reqd_file in self.required_files if reqd_file not in repo_files]
        for absent_file in absent_files:
            if absent_file == 'README.md':
                score_dict['README.md'] = 0
            if absent_file == 'CONTRIBUTING.md':
                score_dict['CONTRIBUTING.md'] = 0
            if absent_file == 'CODE_OF_CONDUCT.md':
                score_dict['CODE_OF_CONDUCT'] = 0
            if absent_file == 'LICENSE':
                score_dict['LICENSE'] = 0
            if absent_file == 'CITATION.md':
                score_dict['CITATION.md'] = 0
            if absent_file == '.gitignore':
                score_dict['.gitignore'] = 0

        start_date = datetime.today() - timedelta(days=60)
        start_date = start_date.isoformat()        
        issues = self.github_instance.get_closed_issues(self.repo_name, self.owner, start_date)
        if issues > 1:
            score += 1
            score_dict['issues'] = 1
        score_dict['total_score'] = score
        return score_dict
    
    def get_grade(self, score):
        score = (score/7) * 100
        if score >= 95:
            grade = 'A+'
        if score >= 90 and score <= 94:
            grade = 'A'
        if score >= 85 and score <= 89:
            grade = 'B+'
        if score >= 80 and score <= 84:
            grade = 'B'
        if score >= 75 and score <= 79:
            grade = 'C+'
        if score >= 70 and score <= 74:
            grade = 'C'
        if score >= 65 and score <= 69:
            grade = 'D+'
        if score >= 60 and score <= 64:
            grade = 'D'
        else:
            grade = 'F'
        return grade
    