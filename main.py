"""Написать функцию, которая на вход принимает номер блока и выводит данные о
транзакциях из очередного блока, учитываем, что в блоке их может не быть

в сети Акаш есть вот такой блок https://www.mintscan.io/akash/blocks/11260637

доступные rest можно посмотреть тут https://chains.cosmos.directory/akash

в текущем задании нужно из response выдернуть данные по пути data.txs,
данные лежат в base64, то есть понадобится метод base64.b64decode()"""
import base64

import requests


def get_block_data(height: int) -> list[bytes] | None:
    """Get a list of block transactions."""
    response = requests.get(url=f'https://akash-rest.publicnode.com/cosmos/base/tendermint/v1beta1/blocks/{height}')
    if txs_b64 := response.json().get('block').get('data').get('txs'):
        return list(map(lambda i: base64.b64decode(i), txs_b64))


get_block_data(11260637)
