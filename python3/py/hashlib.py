#coding=utf-8

import hashlib
t = hashlib.md5()
tt = hashlib.sha256()
tt.update(b"wangzongyi")
tt.hexdigest()


