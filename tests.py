import unittest
import txidbech32

lib = txidbech32

class txidBech32Tests(unittest.TestCase):


    def setUp(self):
        self.lib = lib

    def tearDown(self):
        self.lib = None


    def test_positionToTxref_1(self):
        blockHeight = 0
        txPos = 0

        txref = lib.txRefEncode(lib.CHAIN_MAINNET , blockHeight, txPos)
        expected = "tx1-rqqq-qqqq-qmhu-qk"
        self.assertEqual(expected,txref)


    def test_positionToTxref_2(self):
        blockHeight = 1
        txPos = 0

        txref = lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos)
        expected = "tx1-rzqq-qqqq-uvlj-ez"
        self.assertEqual(expected,txref)

    def test_positionToTxref_3(self):
        blockHeight = 2097151
        txPos = 1000

        txref = lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos)
        expected = "tx1-r7ll-lrar-a27h-kt"

        self.assertEqual(expected,txref)


    def test_positionToTxref_4(self):
        blockHeight = 2097151
        txPos = 8191

        txref = lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos)
        expected = "tx1-r7ll-llll-khym-tq"
        self.assertEqual(expected,txref)

    def test_positionToTxref_5(self):
        blockHeight = 466793
        txPos = 2205

        txref = lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos)
        expected = "tx1-rjk0-u5ng-4jsf-mc"
        self.assertEqual(expected,txref)

    def test_positionToTxref_6(self):
        blockHeight = 467883
        txPos = 2355

        txref = lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos)
        expected = "tx1-rk63-uvxf-9pqc-sy"
        self.assertEqual(expected, txref)

    def test_positionToTxref_7(self):
        blockHeight = 2097151
        txPos = 1000

        txref = lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos)
        expected = "tx1-r7ll-lrar-a27h-kt"
        self.assertEqual(expected,txref)

    def test_positionToTxref_8(self):
        blockHeight = 2097151
        txPos = 8191

        txref = lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos)
        expected = "tx1-r7ll-llll-khym-tq"
        self.assertEqual(expected,txref)

    def test_positionToTxref_9(self):
        blockHeight = 2097151
        txPos = 0

        txref = lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos)
        expected = "tx1-r7ll-lrqq-vq5e-gg"
        self.assertEqual(expected, txref)

    def test_positionToTxref_10(self):
        blockHeight = 0
        txPos = 8191

        txref = lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos)
        expected = "tx1-rqqq-qull-6v87-r7"
        self.assertEqual(expected, txref)

    #testnet
    def test_positionToTxref_11(self):
        blockHeight = 467883
        txPos = 2355

        txref = lib.txRefEncode(lib.CHAIN_TESTNET, blockHeight, txPos)
        expected = "txtest1-xk63-uqvx-fqx8-xqr8"
        self.assertEqual(expected, txref)

    def test_positionToTxref_12(self):
        blockHeight = 0
        txPos = 0

        txref = lib.txRefEncode(lib.CHAIN_TESTNET, blockHeight, txPos)
        expected = "txtest1-xqqq-qqqq-qqkn-3gh9"
        self.assertEqual(expected, txref)

    def test_positionToTxref_13(self):
        blockHeight = 1152194
        txPos = 1

        txref = lib.txRefEncode(lib.CHAIN_TESTNET, blockHeight, txPos)
        expected = "txtest1-xyv2-xzyq-qqm5-tyke"
        self.assertEqual(expected, txref)


    #testDecode
    def test_decodef_1(self):
        blockHeight = 0
        txPos = 0

        result = (lib.txRefDecode(lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos)))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decodef_2(self):
        blockHeight = 1
        txPos = 0

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decodef_3(self):
        blockHeight = 2097151
        txPos = 1000

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decodef_4(self):
        blockHeight = 2097151
        txPos = 8191

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decodef_5(self):
        blockHeight = 466793
        txPos = 2205

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decodef_6(self):
        blockHeight = 467883
        txPos = 2355

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decodef_7(self):
        blockHeight = 2097151
        txPos = 1000

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decodef_8(self):
        blockHeight = 2097151
        txPos = 8191

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decodef_9(self):
        blockHeight = 2097151
        txPos = 0

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decode_10(self):
        blockHeight = 0
        txPos = 8191

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_MAINNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    # testnet
    def test_decode_11(self):
        blockHeight = 467883
        txPos = 2355

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_TESTNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decode_12(self):
        blockHeight = 0
        txPos = 0

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_TESTNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    def test_decode_13(self):
        blockHeight = 1152194
        txPos = 1

        result = lib.txRefDecode(lib.txRefEncode(lib.CHAIN_TESTNET, blockHeight, txPos))
        self.assertEqual(blockHeight, result[0])
        self.assertEqual(txPos, result[1])

    #
    # End to end
    #

    def test_end2end_1(self):
        txref = lib.txidToBech32("f8cdaff3ebd9e862ed5885f8975489090595abe1470397f79780ead1c7528107","testnet")
        expected = "txtest1-xyv2-xzyq-qqm5-tyke"

        self.assertEqual(expected,txref)

    def test_end2end_2(self):
        txref = lib.txidToBech32("016b71d9ec62709656504f1282bb81f7acf998df025e54bd68ea33129d8a425b", "mainnet")
        expected = "tx1-rk63-uvxf-9pqc-sy"

        self.assertEqual(expected, txref)

    def test_end2end_3(self):
        txid = lib.bech32ToTxid("txtest1-xyv2-xzyq-qqm5-tyke")
        expected = "f8cdaff3ebd9e862ed5885f8975489090595abe1470397f79780ead1c7528107"
        self.assertEqual(expected, txid)

    def test_end2end_4(self):
        txid = lib.bech32ToTxid("tx1-rk63-uvxf-9pqc-sy")
        expected = "016b71d9ec62709656504f1282bb81f7acf998df025e54bd68ea33129d8a425b"

        self.assertEqual(expected, txid)

if __name__ == '__main__':
    unittest.main()
