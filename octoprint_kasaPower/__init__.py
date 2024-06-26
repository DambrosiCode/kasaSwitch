import octoprint.plugin

import flask

import asyncio
from kasa import Discover, Credentials

async def switch(alias, username=None, password=None, change_state=True):

	creds = Credentials(username, password)

	found = await Discover.discover(credentials=creds)
	ipaddress = [i for i in found if found[i].alias==alias][0]

	dev = await Discover.discover_single(ipaddress, credentials=creds)
	if change_state:
		if dev.is_on:
			await dev.turn_off()
		else:
			await dev.turn_on()
		await dev.update()
	return dev.is_on


class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
		       octoprint.plugin.AssetPlugin,
		       octoprint.plugin.SimpleApiPlugin):
	def on_after_startup(self):
        	self._logger.info("Kasa alias is %s" % self._settings.get(["kasaAlias"]))
    
	def get_settings_defaults(self):
        	return dict(kasaAlias="")
    
	def get_template_configs(self):
        	return [
            		#dict(type="navbar", custom_bindings=False),
            		dict(type="settings", custom_bindings=False)
        	]

	def get_assets(self):
		return dict(
			js=["js/kasaPower.js"]
		)

	def get_api_commands(self):
		return dict(
			powerOn=[],
			powerCheck=[]
		)

	def on_api_command(self, command, data):
		self._logger.info('your command master...')
		self._logger.info(command)
		self._logger.info(data)
		if command == 'powerOn':
			self._logger.info('power switch')
			kasa_alias = self._settings.get(["kasaAlias"])

			is_on = asyncio.run(switch(kasa_alias))
			return flask.jsonify(switchOn=is_on)
		elif command=='powerCheck':
			self._logger.info('power check')
			kasa_alias = self._settings.get(["kasaAlias"])

			is_on = asyncio.run(switch(kasa_alias, change_state=False))
			return flask.jsonify(switchOn=is_on)


__plugin_name__ = "Kasa Power Switch" 
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
