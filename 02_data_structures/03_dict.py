"""
 딕셔너리(dict)
"""

# JSON 형식과 유사
# key-value 형태

user = {
    "name":"ㅇㅇㅇ",
    "age" : 20,
    "skills" : ["java","sql", "html/css", "js", "python"]
}

print(f"user : {user}")

print(f"이름 : {user['name']}")
print(f"스킬 : {user['skills']}")

print(f"연락처 : {user['phone']}")

print()
#get 사용 접근
print(f"이름 : {user.get('name')}")
print(f"스킬 : {user.get('skills')}")

print(f"연락처 : {user.get('phone')}")
# 존재하지 않는 경우 None 반환
print(f"연락처 : {user.get('phone', '없음')}")
print()

#변경
user['email'] = 'sara947@naver.com'
print(f"{user}")

user['age'] = 40
print(f"user - {user}")

del user['age']
print(f"user - {user}")
"""
del user['phone']
print(f"user - {user}")
"""

# 탐색
for key in user:
    print(f"key: {key} / value: {user[key]}")

for k,v in user.items():
    print(f"key:{k} / value: {v}")
print()

print(f"키 목록: {list(user.key())}")
print(f"밸류 목록 : {list(user.values())}")
print(f"items() : {list(user.items())}")
