from asyncio import sleep
from .. import loader, utils

def register(cb):
	cb(MozgoebkaMod())
	
class MozgoebkaMod(loader.Module):
	"""Заебет мозги любому""
	strings = {'name': 'Мозгоебка'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
		
	async def выебатьcmd(self, message):
		""".выебать <колличество> <реплай на того, кого заебать>"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("<b>А кого заёбывать-то?</b>")
			return
		id = reply.sender_id
		args = utils.get_args(message)
		count = 50
		if args:
			if args[0].isdigit():
				if int(args[0]) < 0:
					count = 50
				else:
					count = int(args[0])
		txt = '<a href="tg://user?id={}">{}</a>'
		await message.edit(txt.format(id, "Скажи спасибо Никли"))
		for _ in range(count):
			await sleep(0.3)
			msg = await message.client.send_message(message.to_id, txt.format(id, "Мозгоебка:3"), reply_to=message)
			if not msg.is_reply:
				await msg.edit("<b>Остановлено!</b>")
				break
			await sleep(0.3)
			await msg.delete()
				
			
