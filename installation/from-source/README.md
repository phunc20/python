


## Verify authenticity of the source file
01. **import** the public key from the signer: either by `gpg --import \<key_file\>` or by `gpg --recv-keys \<key_id\>`
02. **download** the signature corresponding to the source file (e.g. the `Python-3.7.9.tar.xz.asc` below)
03. **verify** the signature by `gpg --verify \<source_file\> [\<signature\>]`, where `\<signature\>` is _optional_ if the source file is **named similarly**

```bash
[phunc20@tako-x60 Downloads]$ gpg --import pgp_keys.asc
gpg: key 2D347EA6AA65421D: 3 signatures not checked due to missing keys
gpg: key 2D347EA6AA65421D: public key "Ned Deily (Python release signing key) <nad@python.org>" imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg: no ultimately trusted keys found
[phunc20@tako-x60 Downloads]$ gpg --verify Python-3.7.9.tar.xz.asc
gpg: assuming signed data in 'Python-3.7.9.tar.xz'
gpg: Signature made Sat 15 Aug 2020 01:38:04 PM +07
gpg:                using RSA key 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
gpg: Good signature from "Ned Deily (Python release signing key) <nad@python.org>" [unknown]
gpg:                 aka "Ned Deily (Python release signing key) <nad@acm.org>" [unknown]
gpg:                 aka "Ned Deily <nad@baybryj.net>" [unknown]
gpg:                 aka "keybase.io/nad <nad@keybase.io>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 0D96 DF4D 4110 E5C4 3FBF  B17F 2D34 7EA6 AA65 421D
[phunc20@tako-x60 Downloads]$ gpg --verify Python-3.7.9.tar.xz.asc Python-3.7.9.tar.xz
gpg: Signature made Sat 15 Aug 2020 01:38:04 PM +07
gpg:                using RSA key 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
gpg: Good signature from "Ned Deily (Python release signing key) <nad@python.org>" [unknown]
gpg:                 aka "Ned Deily (Python release signing key) <nad@acm.org>" [unknown]
gpg:                 aka "Ned Deily <nad@baybryj.net>" [unknown]
gpg:                 aka "keybase.io/nad <nad@keybase.io>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 0D96 DF4D 4110 E5C4 3FBF  B17F 2D34 7EA6 AA65 421D
```

