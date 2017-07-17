import segwit_addr
import connectors

MAGIC_BTC_MAINNET = 0x03

MAGIC_BTC_TESTNET = 0x06

bech32 = segwit_addr

def txRefEncode(magic, blockHeight, txPos):
    shortId = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    shortId[0] = magic
    shortId[1] &= ~(1 << 0)

    shortId[1] |= (blockHeight & 0xF) << 1
    shortId[2] |= (blockHeight & 0x1F0) >> 4
    shortId[3] |= (blockHeight & 0x3E00) >> 9
    shortId[4] |= (blockHeight & 0x7C000) >> 14
    shortId[5] |= (blockHeight & 0x180000) >> 19

    shortId[5] |= (txPos & 0x7) << 2
    shortId[6] |= (txPos & 0xF8) >> 3
    shortId[7] |= (txPos & 0x1F00) >> 8



    result = bech32.bech32_encode("tx",shortId)
    finalResult = result[0: 3] + "-" + result[3: 7] + "-" + result[7:11] + "-" + result[
        11:15] + "-" + result[15:17]



    return finalResult

def txRefDecode(bech32Tx):
    stripped = bech32Tx.replace("-","")
    result = bech32.bech32_decode(stripped)
    buf = result[1]

    if buf[0] == MAGIC_BTC_MAINNET:
        chain = "mainnet"
    else:
        chain = "testnet"


    bStart = buf[1] >> 1 | buf[2] << 4 | buf[3] << 9 | buf[4] << 14
    b5 = (buf[5] & 0x03) << 19

    height = bStart | b5
    pos = (buf[5] & 0x1C) >> 2
    pos |= buf[6] << 3
    pos |= buf[7] << 8

    blockHeight = str(height)
    transactionPosition = str(pos)

    txid = connectors.getTxidFromBlockPosition(blockHeight,transactionPosition, chain)
    return txid

def txidToBech32(txid, chainname):
    position = connectors.getPositionFromTxid(txid,chainname)

    blockHeight = int(position[0])
    blockIndex = int(position[1])

    if chainname == "mainnet":
        magic = MAGIC_BTC_MAINNET
    else:
        magic = MAGIC_BTC_TESTNET

    encoded = txRefEncode(magic,blockHeight,blockIndex)

    return encoded



