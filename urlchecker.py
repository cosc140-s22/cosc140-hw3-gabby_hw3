#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url):
  scheme, url = url.split("://")
  
  if not scheme == "http" and not scheme == "https":
    return False

  
  
  pound_count = url.count("#")
  question_count = url.count("?")

  if pound_count > 1 or question_count > 1:
    return False
  elif pound_count == 1 and question_count == 1:
    if url.find("#") > url.find("?"):
      return False

  if url.count(" ") > 0:
    return False

  if url.count("/") == 0:
    return False
  
  host, path = url.split("/", 1)

  if path.count(":") > 0:
    return False

  if host.count(":") > 1:
    return False
  elif host.count(":") == 1:
    hostname, port = host.split(":")
    if not port.isdigit():
      return False
    if hostname == "":
      return False
  else:
    if host == "":
      return False
  
  return True


def testurl():
  urls = [ # valid
    ['https://example.com/', True],
    ['http://example.com/', True],
    ['http://example.com/?query', True],
    ['http://example.com/#fragment', True],
    ['http://example/', True],
    ['http://example/path/', True],
    ['http://example/path', True],
    ['https://example.com:3000/path#fragment?query', True],
    ['https://example.com/path#fragment?query', True],
    # invalid
    ['htt://example/', False],
    ['httpss://example/', False],
    ['https://example/:3000', False],
    ['https://example/?:3000?', False],
    ['https://example/?:3000#', False],
    ['https://example/xy z', False],
    ['https://example/xyz:', False],
    ['https://example', False],
    ['https:///test', False]
  ]
  for url,expected in urls:
    if urlchecker(url) != expected:
      print(f"{url} is not valid, but your function claimed the opposite")
    else:
      print(f"{url} - ok")


testurl()
