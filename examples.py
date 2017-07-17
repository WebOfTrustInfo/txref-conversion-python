import txidbech32


#tests and usage examples for:
#   - Retrieving a TxId from a bech32 encoded TxRef
#   - Retrieving a Txref from a TxID∑

def tests():

    # TEST A: Correct operation in the Testnet
    # 1 - get a TxId (transaction id) from a correct Bech32 encoded TxRef
    correctBech32_1 = "tx1-xyv2-xxqq-fpmp-u0"
    testTxid_1 = txidbech32.txRefDecode(correctBech32_1)

    # 2 - get a TxRef (encoded in Bech32) from a correct TxId
    correctTxid_1 = "f8cdaff3ebd9e862ed5885f8975489090595abe1470397f79780ead1c7528107"
    testBech32_1 = txidbech32.txidToBech32(correctTxid_1,"testnet")

    # 3 - verify that the outputs of the txidbech32 libraty calls equal the expected and correct outputs
    if testTxid_1 == correctTxid_1 and testBech32_1 == correctBech32_1:
        print ("Testnet Test: SUCCESS")
    else:
        print("Testnet Test: FAIL :(")


    # TEST B: Correct operation in the Mainnet
    # 1 - get a TxId (transaction id) from a correct Bech32 encoded TxRef
    correctBech32_2 = "tx1-rk63-uvxf-9pqc-sy"
    testTxid_2 = txidbech32.txRefDecode(correctBech32_2)

    # 2 - get a TxRef (encoded in Bech32) from a correct TxId
    correctTxid_2 = "016b71d9ec62709656504f1282bb81f7acf998df025e54bd68ea33129d8a425b"
    testBech32_2 = txidbech32.txidToBech32(correctTxid_2, "mainnet")

    # 3 - verify that the outputs of the txidbech32 libraty calls equal the expected and correct outputs
    if testTxid_2 == correctTxid_2 and testBech32_2 == correctBech32_2:
        print("Mainnet Test: SUCCESS")
    else:
        print("Mainnet Test: FAIL :(")

tests()