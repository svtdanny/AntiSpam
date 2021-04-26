import requests

res = requests.post('http://127.0.0.1:8000/rest-auth/login/', data={'username':'ddd', 'password':'ddd'})
key = res.json()['key']

# res = requests.post('http://127.0.0.1:8000/profile/sys_mail_lists/', headers={'Authorization': 'Token ' + key}, data={'username':"antispam"})
data = {'username': 'ddd', 'lastLearn': '0101', 'totalTime': '0202', 'VolumeInbox': 3, 'VolumeSpam': 4}
res = requests.put('http://127.0.0.1:8000/profile/sys_last_learn/', headers={'Authorization': 'Token ' + key}, data=data)
print (res.text)
res = requests.get('http://127.0.0.1:8000/profile/last_learn/', headers={'Authorization': 'Token ' + key})

print (res.text)

