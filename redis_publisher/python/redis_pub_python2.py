#!/usr/bin/python

import redis

redisPort = 6379

channelName = 'redis_data';

hostname = '127.0.0.1'

message = 'This is a test message from python2 redis publisher.'

redisClient = redis.StrictRedis(host = hostname, port = redisPort, db = 0)

redisClient.publish(channelName, message)

print 'published test message to channel ['+channelName+']'

