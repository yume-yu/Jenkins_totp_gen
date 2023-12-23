import sys
import pyotp

secret = sys.argv[1]
print(pyotp.TOTP(secret).now())
