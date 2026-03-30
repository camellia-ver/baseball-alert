import requests
import os
from base64 import b64encode
from nacl import encoding, public

def is_token_valid():
    access_token = os.environ['KAKAO_ACCESS_TOKEN']

    response = requests.get(
        'https://kapi.kakao.com/v1/user/access_token_info',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    return response.status_code == 200

def refresh_access_token():
    response = requests.post(
        'https://kauth.kakao.com/oauth/token',
        data={
            'grant_type': 'refresh_token',
            'client_id': os.environ['KAKAO_REST_API_KEY'],
            'client_secret': os.environ['KAKAO_CLIENT_SECRET'],
            'refresh_token': os.environ['KAKAO_REFRESH_TOKEN']
        }
    )

    data = response.json()
    return data

def update_github_secret(secret_name, secret_value):
    gh_token = os.environ['GH_TOKEN']
    gh_repo = os.environ['GH_REPO']

    # public key 가져오기
    key_response = requests.get(
        f'https://api.github.com/repos/{gh_repo}/actions/secrets/public-key',
        headers={
            'Authorization': f'token {gh_token}',
            'Accept': 'application/vnd.github+json'
        }
    )

    key_data = key_response.json()
    public_key = public.PublicKey(key_data['key'].encode(), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = b64encode(sealed_box.encrypt(secret_value.encode())).decode()

    # secret 업데이트
    requests.put(
        f'https://api.github.com/repos/{gh_repo}/actions/secrets/{secret_name}',
        headers={
            'Authorization': f'token {gh_token}',
            'Accept': 'application/vnd.github+json'
        },
        json={
            'encrypted_value': encrypted,
            'key_id': key_data['key_id']
        }
    )

def ensure_valid_token():
    if not is_token_valid():
        print("토큰 만료됨. 재발급 시작...")
        data = refresh_access_token()
    
        # 새 access_token 업데이트
        new_access_token = data['access_token']
        update_github_secret('KAKAO_ACCESS_TOKEN', new_access_token)
        os.environ['KAKAO_ACCESS_TOKEN'] = new_access_token
        print('access_token 갱신 완료!')

        # refresh_token도 새로 발급된 경우 업데이트
        if 'refresh_token' in data:
            new_refresh_token = data['refresh_token']
            update_github_secret('KAKAO_REFRESH_TOKEN', new_refresh_token)
            os.environ['KAKAO_REFRESH_TOKEN'] = new_refresh_token
            print("refresh_token 갱신 완료!")
    else:
        print("토큰 유효함!")