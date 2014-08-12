
# An offline key generator for Stellar

Usage
-----


```
> python stellar_keygen.py
> python stellar_keygen.py <password>
```

Without a password to generate keys from, a random seed will be generated.

Outputs are same as you'd get from "./stellard create_keys":

```
> Account ID: gn83y9aySyjMbobakGcY8TUECuS4hbpEYn
> Seed:       s3cPNsNm7mG66PSZiTtZnfmyG7ficbhQgJ842Uyt1G8epVgUCst
> Public Key: pEWwhwmenHT1jyRwwCTHhTagJLocuy5m53RBFxU23DUz4UwNtCx
```
Account ID is your address, Seed is your secret key

Installing Sodium
-----------------

Download the tarball: https://download.libsodium.org/libsodium/releases/LATEST.tar.gz

```
> tar xzf LATEST.tar.gz
> cd libsodium-0.6.1/
> ./configure
> make && make check && sudo make install
> pip install pysodium
```
