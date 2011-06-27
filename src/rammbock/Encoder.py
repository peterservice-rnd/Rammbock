def object2string(message):
    whole_message =  _generate_message_from_object(message)
    return whole_message

def _generate_message_from_object(message):

    whole_message = ""
    #TODO: Try to get rid of these reverses.
    message.header.reverse()
    message.ie.reverse()
    for i,j in izip_l(message.items, message.items[1:]):
        if i == 'Header':
            whole_message += _return_header_from_obj(message)
            if j != 'Header':
                whole_message += '\r\n'
        elif i == 'IE':
            whole_message += _return_ie_from_obj(message)
        elif i == 'FLAGS':
            whole_message += chr(int(message.flags))
        elif i == 'DELIMITER':
            print(repr(message.delimiters))
            whole_message += message.delimiters.pop()
        else:
            raise Exception(NameError, 'Unwknown type %s' %i)
    return whole_message

def izip_l(x,y):
    pad = lambda l1,l2: l1 + [None for _ in range(max(len(l2) -
                                                      len(l1), 0))]
    return zip(pad(x,y), pad(y,x))

def _return_header_from_obj(message):
    _, header = message.header.pop()
    return header + " "


def _return_ie_from_obj(message):
    ie = message.ie.pop()
    return ": ".join(ie) + "\r\n"
