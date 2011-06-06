def safepost(request, key):
    try:
        return request.POST[key]
    except MultiValueKeyDictError:
        return ''
