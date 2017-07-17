# txref-conversion-python
Python library to handle conversion between _TxRef &lt;-> TxID_ using the [Blockcypher API](https://www.blockcypher.com/dev/bitcoin/#introduction). 
Tested in Python3

Transaction References, TxRefs, are encoded in Bech32. To learn more about it, see [this BIP](https://github.com/veleslavs/bips/blob/Bech32_Encoded_TxRef/bip-XXXX-Bech32_Encoded_Transaction_Postion_References.mediawiki)

**Please note that this implementation is not yet compliant with the [Special Display Formats guidelines](https://github.com/veleslavs/bips/blob/Bech32_Encoded_TxRef/bip-XXXX-Bech32_Encoded_Transaction_Postion_References.mediawiki#special-display-formats) to handle Testnet operations.**

**Usage:**

- Add txidbech32.py to your imports: `import txidbech32`

- Use `txidbech32.txRefDecode( yourTxRefHere )` to retrieve a TxId from a bech32 encoded TxRef.

- Use `txidbech32.txidToBech32(yourTxIDHere, "mainnet"|"testnet" )`

See _examples.py_ for detailed usage examples and tests.
