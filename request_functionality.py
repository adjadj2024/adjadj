import asyncio
import datetime
import json
import threading
import time
import ast


import requests
import aiohttp
from random import randint, choice
from concurrent.futures import ThreadPoolExecutor

import logger
from constants import Constants
from database import Database

from logger import Logger


class Requests:
    def __init__(self):
        self.url = Constants.REQUEST_URL
        self.logger = Logger
        self.prize_mapper = {
            '206': '300K Symbol',
            '205': '500K Symbol',
            '204': '1mln Symbol',
            '1': '5mln Symbol',
            '2': '20mln Symbol',
            '3': 'Car Symbol',
            '35': '100000',
            '36': '1000000',
            '33': '50000',
            '34': '20000'
        }
        self.star_count_map = {
            '301': 1,
            '302': 3,
            '303': 5,
        }


    @staticmethod
    def random_request(url, payload, headers):
        for _ in range(10):
            box = randint(0, 19)
            payload['boxNum'] = f'{box}'
            requests.post(url=url, data=payload, headers=headers)

    async def request(self, count, user_list, user):
        self.check_server_availavlity(user[2].cget('text'))
        async with aiohttp.ClientSession() as session:
            tasks = []
            for one_user in user_list:
                task = asyncio.create_task(self.request_by_user(session=session, count=count, one_user=one_user))
                tasks.append(task)

            await asyncio.gather(*tasks)
    async def generator_for_count(self,start, count):
        for i in range(start, count):
            yield i

    async def request_by_user(self, session, count, one_user):
        for _ in range(count):
            box_num = randint(1, 20)
            payload = Constants.PAYLOAD
            payload['userID'] = one_user[2].cget('text')
            payload['boxNum'] = f'{box_num}'
            async with session.post(url=self.url, data=payload) as response:
                pass
                self.logger.info(f'fast request status code is {response.status} user is {one_user[2].cget("text")}')

    async def request_by_level(self, gamelevel, user):
        async with aiohttp.ClientSession() as session:
            box_num = 1
            payload = Constants.pyramid_payload
            payload['boxNum'] = f'{box_num}'
            payload['gameLevel'] = f'{gamelevel}'
            payload['userID'] = f"{user}"
            payload['hour'] = f'{datetime.datetime.now().hour}'
            # url = "https://google.com"
            url = Constants.REQUEST_URL
            headers = Constants.REQUEST_HEADERS
            async with session.post(url, data=payload, headers=headers) as resp:
                pass
                print(gamelevel)
    async def pyramid_fast(self, count, user_list, user):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for _ in range(count):
                print(f"Processing count {_ + 1}/{count}")
                for one_user in user_list:
                    task = asyncio.create_task(self.request_pyramid(session, one_user))
                    task2 = asyncio.create_task(self.box_request(session, one_user))
                    tasks.append(task)
                    tasks.append(task2)
                    await asyncio.sleep(0.02)
            await asyncio.gather(*tasks)

    async def box_request(self, session, user):
        user_num = user[2].cget('text')
        url = self.url
        box_payload = Constants.star_box_payload
        box_payload['userID'] = f'{user_num}'
        try:
            async with session.post(url, data=box_payload) as resp:
                pass
        except Exception as e:
            print(f"Error occurred for user {user_num}: {e}")

    async def request_pyramid(self,session, user):
        user_num = user[2].cget('text')
        for gamelevel in range(1, 6):
            box_num = choice([num for num in range(1, 6 - gamelevel + 1)])
            payload = Constants.pyramid_payload
            payload['boxNum'] = f'{box_num}'
            payload['gameLevel'] = f'{gamelevel}'
            payload['userID'] = f"{user_num}"
            payload['hour'] = f'{datetime.datetime.now().hour}'
            url = self.url
            headers = Constants.REQUEST_HEADERS
            box_payload = Constants.star_box_payload
            box_payload['userID'] = f'{user_num}'
            try:
                async with session.post(url, data=payload) as resp:
                    pass
            except Exception as e:
                print(f"Error occurred for user {user_num}: {e}")








    def get_prize_chance_count(self, user_id, user_hash):
        self.check_server_availavlity(user_id)
        payload = Constants.PRIZE_PAYLOAD
        payload['userID'] = user_id
        payload['userHash'] = user_hash
        headers = Constants.REQUEST_HEADERS
        response = requests.post(url=self.url, data=payload, headers=headers)
        self.logger.info(f'prize and chance checking request status code is {response.status_code}')
        return json.loads(response.content)

    def check_server_availavlity(self, user_id):
        headers = Constants.REQUEST_HEADERS
        while True:
            start = datetime.datetime.now()
            payload = Constants.PRIZE_PAYLOAD
            payload['userID'] = user_id
            response = requests.post(url=self.url, data=payload, headers=headers)
            if response.status_code == 200:
                end = datetime.datetime.now()
                delta = end - start
                if delta.seconds > 2:
                    self.logger.info(f'server is not available...')
                    continue
                else:
                    self.logger.info(f'server is available...')
                    break
            else:
                continue




    def get_chance_and_board(self, user):
        payload = Constants.PRIZE_PAYLOAD
        payload['userID'] = f'{user}'
        headers = Constants.REQUEST_HEADERS
        response = json.loads(requests.post(url=self.url, data=payload, headers=headers).content)
        spinids = response.get("SpinIds")
        chance_count = spinids.get('avialable_try')
        board = response.get('arrLive')
        chance_and_board = {
            'chance': int(chance_count),
            'board': board
        }
        return chance_and_board

    async def request_wheel(self, user_id,user_hash, count):
        box_payload = Constants.star_box_payload
        box_payload['userID'] = user_id
        box_payload['userHash'] = user_hash
        wheel_payload = Constants.WHEEL_PAYLOAD
        wheel_payload['userID'] = user_id
        wheel_payload['hour'] = datetime.datetime.now().hour
        wheel_payload['userHash'] = user_hash
        print(wheel_payload)
        print(box_payload)

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            tasks = []
            for i in range(int(count)):
                task_1 = session.post(url=self.url, data=wheel_payload)
                task_2 = session.post(url=self.url, data=box_payload)
                tasks.append(task_1)
                tasks.append(task_2)
                self.logger.info(f'{i + 1}/{count}')
                time.sleep(0.02)
            await asyncio.gather(*tasks)


    def request_wheel_for_all(self, user_list, count):
        for user in user_list:
            db = Database()
            id, user_id, user_hash, chance = db.get_one_user(user_id=user[2].cget('text'))

            asyncio.run(self.request_wheel(user_id=user_id,user_hash=user_hash,count=count))


    def request_slot_for_all(self, user_list, count):
        for user in user_list:
            db = Database()
            id,user_id, user_hash, chance = db.get_one_user(user[2].cget('text'))
            asyncio.run(self.request_slot(user_id=user_id, user_hash=user_hash,count=count))

    async def request_slot(self, user_id,user_hash, count):
        box_payload = Constants.star_box_payload
        box_payload['userID'] = user_id
        box_payload['userHash'] = user_hash
        slot_payload = Constants.SLOT_PAYLOAD
        slot_payload['userID'] = user_id
        slot_payload['hour'] = datetime.datetime.now().hour
        slot_payload['userHash'] = user_hash

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            tasks = []
            for i in range(int(count)):
                task_1 = session.post(url=self.url, data=slot_payload)
                task_2 = session.post(url=self.url, data=box_payload)
                tasks.append(task_1)
                tasks.append(task_2)
                self.logger.info(f'{i + 1}/{count}')
                time.sleep(0.02)
            await asyncio.gather(*tasks)





    def refresh_request(self, user):
        refresh_payload = Constants.REFRESH_PAYLOAD
        refresh_payload['userID'] = f"{user}"
        requests.post(url=self.url, headers=Constants.REQUEST_HEADERS, data=refresh_payload)

    def process_the_request(self,user_id, user_hash, count):
        data_history = Constants.DATA_HISTORY
        data_history['userHash'] = user_hash
        data_history['userID'] = user_id
        history_res = requests.post(url=self.url,data=data_history).json()
        star_count = int(history_res["count"]['starAmount'])
        o_json = history_res["liveOut"]['out']['o_json']
        o_json_dict = {}
        if o_json:
            o_json_dict = ast.literal_eval(o_json)

        for i in range(1, count + 1):
            for k in range(1, 6):
                if str(k) in o_json_dict:
                    print(f"Level {k} is already opened")
                    o_json_dict.pop(str(k))
                    continue
                print(f"Request Level --> {k}")
                data_bet = Constants.pyramid_payload
                data_bet['gameLevel'] = k
                data_bet['boxNum'] = randint(1, 6 - k)
                data_bet['userHash'] = user_hash
                data_bet['userID'] = user_id


                res = requests.post(url=self.url,data=data_bet).json()
                PrizeID = res["PrizeID"]
                if PrizeID in ['301', '302', '303']:
                    star_count += self.star_count_map[PrizeID]

                    if star_count >= 25:
                        data_star = Constants.star_box_payload
                        data_star['userHash'] = user_hash
                        data_star['userID'] = user_id
                        requests.post(url=self.url,data=data_star)
                        star_count = star_count - 25
                    break
                elif PrizeID in ['1', '2', '3']:
                    if PrizeID in ['3']:
                        exit(1)
        return "Done"

    def request_sync_pyramid(self, user_list, count):
        for user in user_list:
            db = Database()
            id, user_id, user_hash, chance = db.get_one_user(user[2].cget('text'))
            self.process_the_request(user_id, user_hash, count)


if __name__ == '__main__':
    start = datetime.datetime.now()
    obj = Requests()
    start_tict = obj.get_prize_chance_count(user_id='2852619')
