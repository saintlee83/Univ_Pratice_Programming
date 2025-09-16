def http_status(status):
	match status :
		case 200:
			return "OK"
		case 404 | 410 :
			return "Not Found"
		case x if 500 <= x < 600:
			return "Server Error"
		case _ :
			return "Unknown"