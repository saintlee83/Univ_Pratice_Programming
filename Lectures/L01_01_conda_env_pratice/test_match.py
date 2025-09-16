import sys

print("__file__", __file__, flush=True)
print("sys.version		 =", sys.version, flush=True)
print("sys.version_info=", sys.version_info, flush=True)
print("-" * 10, flush=True)
if sys.version_info < (3, 10) :
	print("Python 3.10 이상이 필요함")
	sys.exit(1)	

else :
	from match_py310 import http_status

	print(http_status(200))
	print(http_status(404))
	print(http_status(503))
	print(http_status(123))