#!/usr/bin/env python
import sys
import argparse
from slackclient import SlackClient

def main():
	ap = argparse.ArgumentParser()
	ap.add_argument('--channel', default='#general')
	ap.add_argument('--msg', default=None)
	ap.add_argument('--token-file', default='./slacktoken.txt')
	args = ap.parse_args()
	if args.msg is None:
		return 1
	with open(args.token_file, 'r') as f:
		token = f.read().rstrip()
	sc = SlackClient(token)
	print sc.api_call(
		'chat.postMessage',
		channel=args.channel,
		text=args.msg,
		as_user=True
	)
	return 0

if __name__ == '__main__':
	sys.exit(main())
