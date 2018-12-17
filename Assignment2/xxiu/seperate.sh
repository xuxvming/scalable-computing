#!/bin/sh
# Script seperating hashes

awk '$1 ~ /\$pbkdf2-sha256\$/' xiux.hashes > pbkdf2.hashes
awk '$1 ~ /\$1\$/' xiux.hashes > md5crypt.hashes
awk '$1 ~ /\$5\$/' xiux.hashes > sha256.hashes
awk '$1 ~ /\$6\$/' xiux.hashes > sha512.hashes
awk '$1 ~ /\$argon2i\$/' xiux.hashes > argon2.hashes
awk 'length($1) < 20' xiux.hashes > des.hashes
