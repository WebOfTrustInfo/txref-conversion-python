import segwit_addr
import connectors

MAGIC_BTC_MAINNET = 0x03

MAGIC_BTC_TESTNET = 0x06

CHAIN_MAINNET = "mainnet"
CHAIN_TESTNET = "testnet"

TXREF_BECH32_HRP_MAINNET = "tx"
TXREF_BECH32_HRP_TESTNET = "txtest"

bech32 = segwit_addr





def txRefEncode(chain, blockHeight, txPos):
    shortId = None
    nonStandardShortId = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    standardShortId = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    nonStandard = False
    if chain == CHAIN_MAINNET:
        magic = MAGIC_BTC_MAINNET
        prefix = TXREF_BECH32_HRP_MAINNET
        shortId = standardShortId
    else:
        magic = MAGIC_BTC_TESTNET
        prefix = TXREF_BECH32_HRP_TESTNET
        nonStandard = True
        shortId = nonStandardShortId

    if(nonStandard and (blockHeight > 0x1FFFFF or txPos > 0x1FFF or magic > 0x1F)) or (nonStandard and (blockHeight > 0x3FFFFFF or txPos > 0x3FFFF and magic > 0x1F)):
        return None

    """

    """
    shortId[0] = magic
    shortId[1] &= ~(1 << 0)

    shortId[1] |= (blockHeight & 0xF) << 1
    shortId[2] |= (blockHeight & 0x1F0) >> 4
    shortId[3] |= (blockHeight & 0x3E00) >> 9
    shortId[4] |= (blockHeight & 0x7C000) >> 14

    if nonStandard:
        shortId[5] |= ((blockHeight & 0xF80000) >> 19)
        shortId[6] |= ((blockHeight & 0x3000000) >> 24)

        shortId[6] |= ((txPos & 0x7) << 2)
        shortId[7] |= ((txPos & 0xF8) >> 3)
        shortId[8] |= ((txPos & 0x1F00) >> 8)
        shortId[9] |= ((txPos & 0x3E000) >> 13)

    else:
        shortId[5] |= ((blockHeight & 0x180000) >> 19)
        shortId[5] |= ((txPos & 0x7) << 2)
        shortId[6] |= ((txPos & 0xF8) >> 3)
        shortId[7] |= ((txPos & 0x1F00) >> 8)

    result = bech32.bech32_encode(prefix,shortId)

    breakIndex = len(prefix)+1
    finalResult = result[0: breakIndex] + "-" + \
                  result[breakIndex: breakIndex+4] + "-" + \
                  result[breakIndex+4:breakIndex+8] + "-" + \
                  result[breakIndex+8:breakIndex+12] + "-" + \
                  result[breakIndex+12:len(result)]



    return finalResult

def txRefDecode(bech32Tx):
    stripped = bech32Tx.replace("-","")
    result = bech32.bech32_decode(stripped)
    buf = result[1]
    nonStandard = False

    if buf[0] == MAGIC_BTC_MAINNET:
        chain = "mainnet"
    else:
        chain = "testnet"
        nonStandard = True



    bStart = buf[1] >> 1 | buf[2] << 4 | buf[3] << 9 | buf[4] << 14

    blockHeight = 0
    blockIndex = 0

    if(nonStandard):
        blockHeight = bStart | (buf[5] << 19)
        blockHeight |= ((buf[6] & 0x03) << 24)

        blockIndex = (buf[6] & 0x1C) >> 2
        blockIndex |= (buf[7] << 3)
        blockIndex |= (buf[8] << 8)
        blockIndex |= (buf[9] << 13)
    else:
        blockHeight = bStart | ((buf[5] & 0x03) << 19)
        blockIndex = (buf[5] & 0x1C) >> 2
        blockIndex |= (buf[6] << 3)
        blockIndex |= (buf[7] << 8)


    blockHeight = blockHeight
    blockIndex = blockIndex

    decoded = [0,0,0]
    decoded[0] = blockHeight
    decoded[1] = blockIndex
    decoded[2] = chain

    return decoded


def txidToBech32(txid, chainname):
    position = connectors.getPositionFromTxid(txid,chainname)
    blockHeight = int(position[0])
    blockIndex = int(position[1])
    encoded = txRefEncode(chainname,blockHeight,blockIndex)

    return encoded

def bech32ToTxid (bech32Tx):

    decoded = txRefDecode(bech32Tx)

    blockHeight = str(decoded[0])
    transactionPosition = str(decoded[1])
    chain = str(decoded[2])

    txid = connectors.getTxidFromBlockPosition(blockHeight, transactionPosition, chain)
    return txid





def examples():
    print("Example1, testnet")

    print(txidToBech32("f8cdaff3ebd9e862ed5885f8975489090595abe1470397f79780ead1c7528107", "testnet"))
    print("txtest1-xyv2-xzyq-qqm5-tyke")

    print(" ")

    print("Example2, mainnet")
    print(txidToBech32("016b71d9ec62709656504f1282bb81f7acf998df025e54bd68ea33129d8a425b","mainnet"))
    print("tx1-rk63-uvxf-9pqc-sy")

    print("Example3, testnet")
    print(bech32ToTxid("txtest1-xyv2-xzyq-qqm5-tyke"))
    print("f8cdaff3ebd9e862ed5885f8975489090595abe1470397f79780ead1c7528107")

    print(" ")

    print("Example4, mainnet")

    print(bech32ToTxid("tx1-rk63-uvxf-9pqc-sy"))
    print("016b71d9ec62709656504f1282bb81f7acf998df025e54bd68ea33129d8a425b")

#examples()