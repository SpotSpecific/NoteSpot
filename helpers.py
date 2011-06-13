def safepost(request, key):
    try:
        return request.POST[key]
    except MultiValueDictKeyError:
        return ''

def safeget(request, key):
    try:
        return request.GET[key]
    except MultiValueDictKeyError:
        return ''
