def parse(query: str) -> dict:
    mydict = {}

    if "?" in query:
        params = query.split("?")[1].split("&")

        for item in params:
            if "=" in item:
                key, value = item.split("=")
                print(mydict)
                mydict[key] = value
                print(mydict)

    return mydict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}



def parse_cookie(query: str) -> dict:
    mydict = {}

    if query.count(';') != 0:
        cookies = query.split(';')

        for cookie in cookies:
            cookie_parts = cookie.strip().split('=', 1)
            if len(cookie_parts) == 2:
                key, value = cookie_parts
                mydict[key] = value


    return mydict


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
