## To have `tkinter`
It seems that in Arch Linux to have the compiled Python equipped with `tkinter`, one must
- first **`pacman -S tk`**
- then **compile python source code** like usual


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

## Here's how to import a key id
There should be **no spaces btw** the alphanumerics.
```bash
~/downloads ❯❯❯ gpg --receive-keys "B269 95E3 1025 0568"
gpg: "B269 95E3 1025 0568" not a key ID: skipping
~/downloads ❯❯❯ gpg --receive-keys "B26995E310250568"
gpg: key B26995E310250568: public key "Łukasz Langa (GPG langa.pl) <lukasz@langa.pl>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```
We import two more keys and then verify:
```bash
~/downloads ❯❯❯ gpg --receive-keys "2D347EA6AA65421D"
gpg: key 2D347EA6AA65421D: public key "Ned Deily (Python release signing key) <nad@python.org>" imported
gpg: Total number processed: 1
gpg:               imported: 1
~/downloads ❯❯❯ gpg --receive-keys "FB9921286F5E1540"
gpg: key FB9921286F5E1540: public key "Ned Deily <nad@acm.org>" imported
gpg: Total number processed: 1
gpg:               imported: 1
~/downloads ❯❯❯ ll Python-3.*
-rw-r--r-- 1 phunc20 wheel 17202980 Dec 17 23:29 Python-3.6.12.tar.xz
-rw-r--r-- 1 phunc20 wheel      833 Dec 17 23:29 Python-3.6.12.tar.xz.asc
-rw-r--r-- 1 phunc20 wheel 24377280 Dec 17 23:30 Python-3.8.6.tgz
-rw-r--r-- 1 phunc20 wheel      833 Dec 17 23:30 Python-3.8.6.tgz.asc
-rw-r--r-- 1 phunc20 wheel 17389636 Dec 17 23:30 Python-3.7.9.tar.xz
-rw-r--r-- 1 phunc20 wheel      833 Dec 17 23:30 Python-3.7.9.tar.xz.asc
~/downloads ❯❯❯ gpg --verify Python-3.6.12.tar.xz.asc
gpg: assuming signed data in 'Python-3.6.12.tar.xz'
gpg: Signature made Sat 15 Aug 2020 02:00:24 PM +07
gpg:                using RSA key 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
gpg: Good signature from "Ned Deily (Python release signing key) <nad@python.org>" [unknown]
gpg:                 aka "Ned Deily <nad@baybryj.net>" [unknown]
gpg:                 aka "keybase.io/nad <nad@keybase.io>" [unknown]
gpg:                 aka "Ned Deily (Python release signing key) <nad@acm.org>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 0D96 DF4D 4110 E5C4 3FBF  B17F 2D34 7EA6 AA65 421D
~/downloads ❯❯❯ gpg --verify Python-3.8.6.tgz.asc
gpg: assuming signed data in 'Python-3.8.6.tgz'
gpg: Signature made Wed 23 Sep 2020 08:58:06 PM +07
gpg:                using RSA key E3FF2839C048B25C084DEBE9B26995E310250568
gpg: Good signature from "Łukasz Langa (GPG langa.pl) <lukasz@langa.pl>" [unknown]
gpg:                 aka "Łukasz Langa <lukasz@python.org>" [unknown]
gpg:                 aka "Łukasz Langa (Work e-mail account) <ambv@fb.com>" [unknown]
gpg:                 aka "[jpeg image of size 24479]" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: E3FF 2839 C048 B25C 084D  EBE9 B269 95E3 1025 0568
~/downloads ❯❯❯ gpg --verify Python-3.7.9.tar.xz.asc
gpg: assuming signed data in 'Python-3.7.9.tar.xz'
gpg: Signature made Sat 15 Aug 2020 01:38:04 PM +07
gpg:                using RSA key 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
gpg: Good signature from "Ned Deily (Python release signing key) <nad@python.org>" [unknown]
gpg:                 aka "Ned Deily <nad@baybryj.net>" [unknown]
gpg:                 aka "keybase.io/nad <nad@keybase.io>" [unknown]
gpg:                 aka "Ned Deily (Python release signing key) <nad@acm.org>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 0D96 DF4D 4110 E5C4 3FBF  B17F 2D34 7EA6 AA65 421D
```
