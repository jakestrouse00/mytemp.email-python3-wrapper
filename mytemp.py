import requests


def get_email(hash,email):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    r = requests.get(f'https://api.mytemp.email/1/inbox/check?inbox={email}&hash={hash}&sid=8635154&task=3&tt=5',
                     headers=header)
    response = r.json()
    emails = response['emls']
    return emails


def make_email(sid):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }

    r = requests.options(f'https://api.mytemp.email/1/inbox/create?sid={sid}&task=27&tt=3139', headers=header)
    payload = {"sid": sid, "task": 27, "tt": 3139}
    r = requests.post(f'https://api.mytemp.email/1/inbox/create?sid={sid}&task=27&tt=3139', json=payload,
                      headers=header)
    hash = r.json()['hash']
    email = r.json()['inbox']
    return hash, email