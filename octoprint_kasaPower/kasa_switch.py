class KasaSwitch(alias, username, password):
        def __init__(self):
                self.alias = alias
                self.creds = Credentials(username, password)

        async def get_ip(self):
                found = await Discover.discover(credentials=self.creds)
                ipaddress = [i for i in found if found[i].alias==self.alias][0]
                dev = await Discover.discover_single(ipaddress, credentials=self.creds)
                return dev

        async def change_state(self):
                dev = await get_ip()
                if dev.is_on:
                        await dev.turn_off()
                else:
                        await dev.turn_on()
                await dev.update()

        async def is_switch_on(self):
                dev = await get_ip()
                return dev.is_on
