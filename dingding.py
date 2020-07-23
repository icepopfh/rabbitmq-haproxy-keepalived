#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:icepopfh

import time
import hmac
import hashlib
import base64
import urllib.parse
import urllib
import socket
import json
import requests
import fcntl
import struct

# def get_access_token2():
# 	# 合成加密url
# 	# python2
# 	Initialize_url = "https://oapi.dingtalk.com/robot/send?access_token=xxxxxx"
# 	timestamp = long(round(time.time() * 1000))
# 	secret = 'xxxxxx'
# 	secret_enc = bytes(secret).encode('utf-8')
# 	string_to_sign = '{}\n{}'.format(timestamp, secret)
# 	string_to_sign_enc = bytes(string_to_sign).encode('utf-8')
# 	hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
# 	sign = urllib.quote_plus(base64.b64encode(hmac_code))
# 	url = "%s&timestamp=%s&sign=%s" % (Initialize_url, timestamp, sign)
# 	return url

def get_access_token3():
	# 合成加密url
	# python3
	Initialize_url = "https://oapi.dingtalk.com/robot/send?access_token=xxxxxx"
	timestamp = str(round(time.time() * 1000))
	secret = 'xxxxxx'
	secret_enc = secret.encode('utf-8')
	string_to_sign = '{}\n{}'.format(timestamp, secret)
	string_to_sign_enc = string_to_sign.encode('utf-8')
	hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
	sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
	url = "%s&timestamp=%s&sign=%s" % (Initialize_url, timestamp, sign)
	return url

def get_ip_address(ifname):
	# 根据网卡名称，获取IP
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
	s.fileno(),
	0x8915,  # SIOCGIFADDR
	struct.pack('256s', ifname[:15])
	)[20:24])

def send_text():
	# 发送文本
	LocalIp = get_ip_address("ens192")
	theme = "keepalived状态提醒"
	content = "节点宕机，请及时查看！"
	message_format = "[%s]  %s%s"
	message = message_format % (theme, LocalIp, content)
	data = {"msgtype": "text",
	        "text": {
		        "content": message
	        }
	        }
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	requests.post(get_access_token3(), data=json.dumps(data), headers=headers)

send_text()

