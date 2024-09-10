# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20389440"))
    API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
    BOT_TOKEN = getenv("BOT_TOKEN", "6523760901:AAEdPrDJXZTOmZS3G7MxFidl_HrBXyyTmRQ")
    SESSION_STRING = getenv("SESSION_STRING", "BQD6zg0AVuRfNFV9JWiyh1dEGyvkeRuvotQ1rOUetrRVW9V-YU1Yqro5X4157xNXKxQX6DWeERYzvOINFEPa69uftD53il6OnCEdPBvZZB6bqkcZ0wVXHjMPa5FYG4HMic05tP4RQaPYhMwMU4WnFleH23TId-7y5C0_RphoDRDpyzyegpfpjM59rLU8ll_0jcuNjjckNZ2IVrvpZ0oCjY23eGd5MY1RT9bWBDhrwCrYsFY0O-R_MT5XSzlcn79NdXtZwvn-2xeaEaV0EeMgkoed_WarZYAjDgw6JKvBpJ6gEbZlPmCMjsSqys9paP31ojSHMi-dsOZ9wfcP6DQ8hsI-zLvsbQAAAAGNfGbLAA")
    SUDO = list(map(int, getenv("SUDO", "5798247275").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")

cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
