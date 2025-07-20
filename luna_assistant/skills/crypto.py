from security import vault, consent, audit
from config import USER
try:
    from web3 import Web3
except ImportError:
    Web3 = None

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_KEY')) if Web3 else None

def handle(intent, entities):
    if intent == "add_wallet":
        password = input("Vault password: ")
        priv_key = input("Enter your Ethereum private key: ")
        vault.save_credential("eth_priv_key", priv_key, password)
        return "Wallet added to vault."
    if intent == "get_balance":
        password = input("Vault password: ")
        priv_key = vault.load_credential("eth_priv_key", password)
        if not priv_key:
            return "No wallet found or wrong password."
        acct = w3.eth.account.privateKeyToAccount(priv_key)
        balance = w3.eth.get_balance(acct.address)
        return f"ETH Balance: {w3.fromWei(balance, 'ether')} ETH"
    if intent == "send_eth":
        if not consent.require_consent("send ETH from your wallet"):
            return "Consent denied."
        password = input("Vault password: ")
        priv_key = vault.load_credential("eth_priv_key", password)
        if not priv_key:
            return "No wallet found or wrong password."
        acct = w3.eth.account.privateKeyToAccount(priv_key)
        to_addr = entities.get("to")
        amount = float(entities.get("amount", 0))
        tx = {
            'to': to_addr,
            'value': w3.toWei(amount, 'ether'),
            'gas': 21000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.get_transaction_count(acct.address)
        }
        signed = acct.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
        audit.log_action(f"Sent {amount} ETH to {to_addr}", USER)
        return f"Transaction sent: {tx_hash.hex()}"
    if intent == "swap_tokens":
        if not consent.require_consent("swap tokens using your wallet"):
            return "Consent denied."
        # Stub: integrate with Uniswap/1inch API here
        audit.log_action("Token swap (stub)", USER)
        return "Token swap executed (stub)."
    return "Unknown crypto command."