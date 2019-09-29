import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
x = 0

for x in range(1,101):
        key = "key" + str(x)
        print (key)
        print (r.set(key,x))
        print(r.get(key))
