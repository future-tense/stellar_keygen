
import hashlib
import pysodium
import sys
import os


VER_SEED = chr(33)
VER_ACCOUNT_ID = chr(0)
VER_ACCOUNT_PUBLIC = chr(67)


def b58encode(v):

	__b58chars = 'gsphnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCr65jkm8oFqi1tuvAxyz'
	__b58base = len(__b58chars)

	long_value = int(v.encode("hex_codec"), 16)

	result = ''
	while long_value >= __b58base:
		long_value, mod = divmod(long_value, __b58base)
		result += __b58chars[mod]
	result += __b58chars[long_value]

	z = 0
	while v[z] == '\0':
		z += 1

	return __b58chars[0]*z + result[::-1]


def get_seed_generic(s):
	m = hashlib.sha512()
	m.update(s)
	return m.digest()[0:32]


def get_seed_random():
	return os.urandom(32)


def hash160(s):
	m = hashlib.sha256()
	m.update(s)
	h = m.digest()

	m = hashlib.new('ripemd160')
	m.update(h)
	t = m.digest()
	return t


def sha256hash(s):

	s = s if s else ' '

	m = hashlib.sha256()
	m.update(s)
	hash1 = m.digest()

	m = hashlib.sha256()
	m.update(hash1)
	hash2 = m.digest()
	return hash2


def four_byte_hash256(s):
	return sha256hash(s)[0:4]


def to_string(ver, value):

	s = ver + value
	s += four_byte_hash256(s)
	return b58encode(s)

#-------------------------------------------------------------------------------


def human_seed(s):
	return to_string(VER_SEED, s)


def human_account_id(s):
	s = hash160(s)
	return to_string(VER_ACCOUNT_ID, s)


def human_account_public(s):
	return to_string(VER_ACCOUNT_PUBLIC, s)

#-------------------------------------------------------------------------------


if __name__ == '__main__':

	if len(sys.argv) > 1:
		seed = get_seed_generic(sys.argv[1])
	else:
		seed = get_seed_random()

	public, _ = pysodium.crypto_sign_seed_keypair(seed)

	print 'Account ID: ', human_account_id(public)
	print 'Seed:       ', human_seed(seed)
	print 'Public Key: ', human_account_public(public)
