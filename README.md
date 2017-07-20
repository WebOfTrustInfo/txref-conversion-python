# txref-conversion-python
Python library to handle conversion between _TxRef &lt;-> TxID_ using the [Blockcypher API](https://www.blockcypher.com/dev/bitcoin/#introduction). 
Tested in Python3

Transaction References, TxRefs, are encoded in Bech32. To learn more about it, see [this BIP](https://github.com/veleslavs/bips/blob/wip/bip-XXXX-Bech32_Encoded_Transaction_Postion_References.mediawiki)

** Tests **
- Run `python3 tests.py`
**Usage:**

- Add txidbech32.py to your imports: `import txidbech32`

- Use `txidbech32.txRefDecode( "yourTxRefHere" )` to retrieve a TxId from a bech32 encoded TxRef.

- Use `txidbech32.txidToBech32( "yourTxIDHere" , "mainnet | testnet" )`

See _examples.py_ and _tests.py_ for detailed usage examples.

[issue1]: https://img.shields.io/badge/issue-1-blue.svg
