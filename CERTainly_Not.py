from Crypto.PublicKey import RSA
from Crypto.Util.asn1 import DerSequence

# Load the DER file
with open("2048_Cert.der", "rb") as file:
    der_data = file.read()

# Extract the public key from the certificate
der_seq = DerSequence()
der_seq.decode(der_data)

tbs_certificate = DerSequence()
tbs_certificate.decode(der_seq[0])  # Extract the "To Be Signed" part

