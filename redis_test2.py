import redis

r = redis.StrictRedis(host='localhost', port=12984, db=0)
x = 0

for x in range(100,0,-1):
        key = "key" + str(x)
        print(key)
        print(r.get(key))
