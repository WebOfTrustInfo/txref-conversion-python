import urllib.request
import json


def webRequest(urlData):
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    JSON_object = json.loads(data.decode(encoding))

    return JSON_object




def getTxidFromBlockPosition(blockHeight,transactionPosition, network):
    if network == "testnet":
        network_path = "btc/test3"
    else:
        network_path = "btc/main"

    urlData = "https://api.blockcypher.com/v1/" + network_path + "/blocks/" + blockHeight + "?txstart=" + transactionPosition + "&limit=1"
    block = webRequest(urlData)
    return block["txids"][0]



def getTransactionFromTxid(txid, network):
    if network == "testnet":
        network_path = "btc/test3"
    else:
        network_path = "btc/main"
    urlData = "https://api.blockcypher.com/v1/" + network_path + "/txs/" + txid + "?limit=500"
    transaction = webRequest(urlData)

    return transaction

def getPositionFromTxid(txid, network):
    transaction = getTransactionFromTxid(txid, network)
    blockHeight = str(transaction["block_height"])
    blockIndex = str(transaction["block_index"])

    position = [blockHeight,blockIndex]

    return position

