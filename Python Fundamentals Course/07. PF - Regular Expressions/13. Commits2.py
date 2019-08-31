import re


class User:
    def __init__(self, name: str):
        self.name = name
        self.repos = []


class Repo:
    def __init__(self, name: str):
        self.name = name
        self.commits = []

    def total_adds_dels(self):
        count_adds = 0
        for commit in self.commits:
            count_adds += commit.additions

        count_dels = 0
        for commit in self.commits:
            count_dels += commit.deletions

        return f"Total: {count_adds} additions, {count_dels} deletions"


class Commit:
    def __init__(self, hash1: str, message: str, additions: int, deletions: int):
        self.hash1 = hash1
        self.message = message
        self.additions = additions
        self.deletions = deletions

    def __str__(self):
        return f"commit {self.hash1}: {self.message} ({self.additions} additions, {self.deletions} deletions)"


def create_user(name: str):
    return User(name)


def create_repo(name: str):
    return Repo(name)


def create_commit(hash1: str, message: str, additions: int, deletions: int):
    return Commit(hash1, message, additions, deletions)


def print_result(data_list: list):
    for user in sorted(data_list, key=lambda x: x.name):
        print(f"{user.name}:")
        for repo in sorted(user.repos, key=lambda x: x.name):
            print(f"  {repo.name}:")
            for commit in repo.commits:
                print(f"    {commit}")
            print(f"    {repo.total_adds_dels()}")


def main():
    pattern = r"https://github\.com/(?P<user>[A-Za-z0-9\-]+)/(?P<repo>[a-zA-Z-_]+)/commit/(?P<hash>[0-9a-f]{40}),(?P<message>[^(\n]+),(?P<add>[0-9]+),(?P<del>[0-9]+)"
    data_list = []
    while True:
        command = input()
        if command == "git push":
            break
        else:
            if re.fullmatch(pattern, command):
                string = re.fullmatch(pattern, command)
                if string.group('user') not in [obj.name for obj in data_list]:
                    data_list.append(create_user(string.group('user')))
                user_obj_name = next(user for user in data_list if string.group('user') == user.name)
                if string.group('repo') not in [repo.name for repo in user_obj_name.repos]:
                    user_obj_name.repos.append(create_repo(string.group('repo')))
                for repo in user_obj_name.repos:
                    if len(repo.commits) > 0 and repo.name == string.group('repo'):
                        repo.commits.append(create_commit(string.group('hash'),
                                                          string.group('message'),
                                                          int(string.group('add')),
                                                          int(string.group('del'))))

                    elif len(repo.commits) == 0 and repo.name == string.group('repo'):
                        repo.commits.append(create_commit(string.group('hash'),
                                                          string.group('message'),
                                                          int(string.group('add')),
                                                          int(string.group('del'))))
                        break

    print_result(data_list)


if __name__ == "__main__":
    main()
