import os
from cryptography.hazmat.primitives import serialization
from env import pem_password

import hashlib

def get_public_key_fingerprint(public_key, hash_algo='sha256'):
    if hash_algo.lower() == 'sha256':
        hash_obj = hashlib.sha256()
    elif hash_algo.lower() == 'md5':
        hash_obj = hashlib.md5()
    else:
        raise ValueError("Unsupported hash algorithm. Use 'sha256' or 'md5'.")

    # Update the hash object with the public key
    hash_obj.update(public_key)

    # Get the hexadecimal digest of the hash
    fingerprint = hash_obj.hexdigest()

    return fingerprint

def check_contract_availability(public_key):
    blocks = os.listdir(f"contracts/")
    print(blocks)
    directory = 'contracts/'
    file_path = os.path.join(directory, f'{public_key}.txt')
    print(file_path)
    if os.path.isfile(file_path):
        return True
    else:
        return False

def validate_pem_file(pem_data_encrypted):
    private_key_encrypted = serialization.load_pem_private_key(
        pem_data_encrypted,
        password=pem_password,
    )
    print(private_key_encrypted)
    pem = private_key_encrypted.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = private_key_encrypted.public_key()
    print(public_key)
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_pem_str = public_pem.decode("utf-8")
    public_key_lines = public_pem_str.splitlines()
    public_key_base64 = ''.join(public_key_lines[1:-1])
    public_key = public_key_base64.replace("/", "")
    print("Public Key =>", public_key)
    contract_id = get_public_key_fingerprint(public_pem, 'sha256')
    print(f"Public key fingerprint (SHA-256): {contract_id}")
    if check_contract_availability(contract_id):
        return {
            "state":True,
            "contract_id":contract_id
        }
    else:
        return {
            "state":False
        }

# pem_data_encrypted = b"""
# -----BEGIN ENCRYPTED PRIVATE KEY-----
# MIIFNTBfBgkqhkiG9w0BBQ0wUjAxBgkqhkiG9w0BBQwwJAQQhlz8pBcxE22itUqr
# gT2gzgICCAAwDAYIKoZIhvcNAgkFADAdBglghkgBZQMEASoEEEwfwhltCSnN8NQ1
# Kb3o5O0EggTQn+U1TNftMdph1fLloGXoM0Q6T1BU5DCZdFSRGiXvmCekRCb9j6qR
# +ZN20Uwo2VRkrlV2Kih5Ph5EYsCEwXf5u+8BFnt4pJGQ1L4TMKgrkWPiP6yOpQ3B
# 07pniWKYhAOap1XvWhBUUx37LJEo6DA0t5sUFm0iabbIyTVaCB+RLIVqSfuwDvYI
# XlIh/ri2EKE1bd9T8VW2UC4PdsrJyZp3BJtZuK7eu9XUD4j5Ma8tZGwmwTuIlyBh
# cOUi0ixC1cmoEuum7TGb5A5EHPVj3gsWEIuPdZPtgIs+3lWLKqWwbxTO4W8hMDnA
# lylyKu/ZJrUdq7FYa+/zZiyVkMcb7rdbYHTam4GN0nxCpNEPAzQxCnPdBw/Xj1IZ
# PsRGfvQHtw8imHYJNTB52G0dfVqqiFbHjFgmHGCVByi/ylXROAgX0d4L8eatDSo/
# W8Du3Lo31rkqZkMWv9GA02QDLJr4ipKqs9k9PlvaVq0hi7+LdCjwCB7YBb+VTGRt
# pWQ5iNhZsfUtRleUr+1NqMQAnO44RFNy2J3RViUEZ4MYtnqEjjPAzMLcIx/BSQN0
# KSHlrLbRiewrPNVJt6E/Rir8Sbj3eVC0MDmEUCxwx8knoAF4Bd1ETgdxgxhMSA55
# AZE8pI8SEld+ive5wXyODS+ccJFhQHyc33hpgJKyE552EA2jD7JCr0DULrrUxyqB
# yFcEjiG2TEaQybtSdoRT71d6TIO7ZpthexvChw3F61KWQyXwC65YuKI0pg275i5a
# jnhmlkLvzeS+15YxQv7bJ+OIWnzU+wxEfkdIuBQeoqH9JJcrlHjDOk0/7C4V473R
# 1oVvo1tx77TCssnMIu9f4cs+HsyMZTY7ium9p1LPO4DyS2eabPh1mnaH+z6c1297
# 1gpIHbujhmRY0iTEZwnhdpz6lMB8VKIAS3Pt4mEd8oIFIb13yPswUZUYKht1JfPc
# r/uqshY3dPOChXLwID3BZnm7zIKSgfr4izvwOP2a8QCU4kZM9YiNNMCVQewt9Frv
# yVO68cDDggmZF4hUDpHSu+GxkDhaCA3QiY7WfWm5OyFvCWP7Zqs5p7bpouTwvDat
# U55jstKh7alLe0dhsic5FRAvBWfYTivCf+AeWlO+RPndVGTNVxw2GH5EWz7zEyCA
# VGn39MD4jzlJCsF/C4tdAxtrpujxcWkFYfzbZu3VFL/SoDpNRXQ8AnhZUddy3uTt
# gzfV0AhSMhkUDmodRDKG8Cn4JzgcQclTt2wdmhukH0YvooctzLlwrJJTzDosNO0G
# ULUfe0Stck+jedkJ3/9WeFyoqmnoZpBiedPKCDZhkE2/iKxIjL5TeoVTT1vghAJN
# GMf7JO0bpAktaDwU2Xu7haldoqxgoV0Vo8K0BB7VF28pwGDCu4jZvwOWDT+Wg9+3
# z7us1OzM7k1KrkfF5x/siof7yL6Ef1Z3FF+elo830qPFvs/0efh8Wjv08z3q9m5E
# bmOjNtFUvyFbrod28bpbtX2JJ2jLzTVQ3ToSyPjA3xvuDUAfgq5jTC3knMLxMnzj
# alFwCsuCoAgZMeZ9X5kgkrOGBYd+dP3hOFkv8x2s1snsUBuQUhdp9oVldz3hfTbr
# nmRqDnZ0kgTFRIe25EGLUoGc2U4Rz9Y95ZBgNCWKGb7Isk9VbMr4QHA=
# -----END ENCRYPTED PRIVATE KEY-----
# """
# validate_pem_file(pem_data_encrypted)