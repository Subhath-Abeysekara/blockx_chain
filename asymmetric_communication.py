from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.primitives import serialization
# Generate private key
private_key = ec.generate_private_key(ec.SECP256K1())
print(private_key)
# Serialize the private key to bytes (PEM format)
private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Generate public key from the private key
public_key = private_key.public_key()
print(public_key)
# Serialize the public key to bytes (PEM format)
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("Private Key:")
print(private_key_bytes.decode('utf-8'))
print("\nPublic Key:")
print(public_key_bytes.decode('utf-8'))

# Load the public key (if you have it serialized, otherwise use the generated key directly)
public_key = serialization.load_pem_public_key(public_key_bytes)

# Example transaction data
transaction_data = b"This is a transaction."

# Load private key (if you have it serialized, otherwise use the generated key directly)
private_key = serialization.load_pem_private_key(
    private_key_bytes,
    password=None
)

# Create a hash of the transaction data
digest = hashes.Hash(hashes.SHA256())
digest.update(transaction_data)
hash_value = digest.finalize()

# Sign the hash using the private key
signature = private_key.sign(
    hash_value,
    ec.ECDSA(Prehashed(hashes.SHA256()))
)

print("Signature:")
print(signature)


# Verify the signature
try:
    public_key.verify(
        signature,
        hash_value,
        ec.ECDSA(Prehashed(hashes.SHA256()))
    )
    print("Signature is valid.")
except Exception as e:
    print("Signature is invalid:", e)

