
"""
接口自动化----requests库模拟用户登陆

此处用github的api地址进行实践

"""

import requests

url = 'https://api.github.com/user'

# res = requests.get(url)

# 运行结果为：需要用户验证
# {'message': 'Requires authentication', 'documentation_url': 'https://developer.github.com/v3/users/#get-the-authenticated-user'}


res = requests.get(url,auth=('shangpf1','spf123456'))
print(res.json())


"""
运行结果为：

{'login': 'shangpf1', 'id': 33996099, 'node_id': 'MDQ6VXNlcjMzOTk2MDk5', 'avatar_url': 'https://avatars2.githubusercontent.com/u/33996099?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/shangpf1', 'html_url': 'https://github.com/shangpf1', 'followers_url': 'https://api.github.com/users/shangpf1/followers', 'following_url': 'https://api.github.com/users/shangpf1/following{/other_user}', 'gists_url': 'https://api.github.com/users/shangpf1/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/shangpf1/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/shangpf1/subscriptions', 'organizations_url': 'https://api.github.com/users/shangpf1/orgs', 'repos_url': 'https://api.github.com/users/shangpf1/repos', 'events_url': 'https://api.github.com/users/shangpf1/events{/privacy}', 'received_events_url': 'https://api.github.com/users/shangpf1/received_events', 'type': 'User', 'site_admin': False, 'name': None, 'company': None, 'blog': '', 'location': None, 'email':
None, 'hireable': None, 'bio': None, 'public_repos': 19, 'public_gists': 0, 'followers': 0, 'following': 0, 'created_at': '2017-11-26T06:09:38Z', 'updated_at': '2019-05-06T09:04:08Z', 'private_gists': 0, 'total_private_repos': 0, 'owned_private_repos': 0, 'disk_usage': 5183, 'collaborators': 0, 'two_factor_authentication': False, 'plan': {'name': 'free', 'space': 976562499, 'collaborators': 0, 'private_repos': 10000}}

"""