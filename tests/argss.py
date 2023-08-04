import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="echo the string you use here", required=False)
parser.add_argument("-iss","--iserver", help="| client | server |", action="store_true") # false default
parser.add_argument("-np","--nport", help="network port", type=int, default=9909)
parser.add_argument("-nh","--nhost", help="network ip", default="127.0.0.1")
# note -h is used by other app args.
args = parser.parse_args()


print(args)
