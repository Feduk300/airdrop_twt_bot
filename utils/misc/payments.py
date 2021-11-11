import sqlite3
import json
import requests

QIWI_TOKEN = "efb103afa270d8511bad2289b6f9bb79" # efb103afa270d8511bad2289b6f9bb79 - женя / паша - 5d6113d06761aa08c97aaa6e2a7c534d
QIWI_LOGIN = "79095073304"

def qiwi_check(comment, amount):
    database = Db()
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
    parameters = {'rows': '50', 'operation': 'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + QIWI_LOGIN + '/payments', params=parameters)
    payments = json.loads(h.text)
    try:
        for i in range(len(payments)):
            if payments['data'][i]["comment"] == str(comment):
                if database.check_payment(payments['data'][i]["txnId"]):
                    if payments['data'][i]["status"] == "SUCCESS":
                        if payments['data'][i]["sum"]["amount"] >= amount:
                            return payments['data'][i]["sum"]["amount"]
    except IndexError:
        return False


def check_bank_payment(amount):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
    parameters = {'rows': '50', 'operation': 'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + QIWI_LOGIN + '/payments', params=parameters)
    payments = json.loads(h.text)
    try:
        for i in range(len(payments)):
            if payments['data'][i]["sum"]["amount"] == amount:
                if database.check_payment(payments['data'][i]["txnId"]):
                    if payments['data'][i]["status"] == "SUCCESS":
                        return payments['data'][i]["sum"]["amount"]
    except IndexError:
        return False


class Db:  # Класс базы данных, не трогать
    def __init__(self):
        self.conn = sqlite3.connect("utils/misc/payments.db", check_same_thread=False)
        self.cur = self.conn.cursor()

    def check_payment(self, txnId):
        query = f"select txnId from payments where txnId = {txnId}"
        res = self.cur.execute(query).fetchone()
        if not res:
            self.insert_txnid(txnId)
            return True

    def insert_txnid(self, txnId):
        query = f"insert into payments(txnId) values ('{txnId}')"
        self.cur.execute(query)
        self.conn.commit()

database = Db()