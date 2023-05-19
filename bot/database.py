import pymongo, os, pyrogram, asyncio, json
from pymongo import MongoClient
from bot import db, collection, Config, LOGS, queue,data, list_handler, words


ffmpeg = "-map 0 -c:v libx265 -pix_fmt yuv420p -x265-params 'no-info=1' -crf 29 -preset medium -map_metadata -1 -tag:v hvc1 -c:a libfdk_aac -vbr 1 -ac 2 -profile:a aac_he_v2 -movflags +faststart -threads 0"

async def adduser(message):
  if collection.find_one({'_id' : int(message.from_user.id)}):
   LOGS.info("YES")
  else:
   post = {'_id' : int(message.from_user.id), 'ffmpeg' : ffmpeg, 'mode' : 'video'}
   x = collection.insert_one(post)

async def setffmpeg(message, ffmpeg1):
  collection.update_one({'_id': int(message.from_user.id)}, {'$set': {'ffmpeg': ffmpeg1}})

async def getffmpeg(message):
  dic = collection.find_one({'_id' : int(message.from_user.id)})
  ffmpeg = dic['ffmpeg']
  return ffmpeg

async def getffmpeg1(message):
  dic = collection.find_one({'_id' : int(message)})
  ffmpeg = dic['ffmpeg']
  return ffmpeg


async def uploadtype(message):
  dic = collection.find_one({'_id' : int(message.from_user.id)})
  mode = dic['mode']
  return mode


async def uploadtype1(message):
  dic = collection.find_one({'_id' : int(message)})
  mode = dic['mode']
  return mode

async def setmode(message, mode):
  collection.update_one({'_id': int(message.from_user.id)}, {'$set': {'mode': mode}})

async def napana():
  queries = queue.find({})
  for query in queries:
   que = str(query["message"])
   b = json.loads(que)
   if not query["_id"] in list_handler:
    list_handler.append(query["_id"])
   if not b in data:
    data.append(b)
