import orm, asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop,user='root',password='',db='awesome')
    u = User(name='222',email='1111.com',passwd='12345',image='44444')
    await u.save()


async def find(loop):
    await orm.create_pool(loop,user='root',password='',db='awesome')
    rs = await User.findAll()
    print('查找测试： %s' % rs)





loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()