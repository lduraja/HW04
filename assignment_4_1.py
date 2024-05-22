def encode_message(code, message):
    """
    Encode a message by shifted substitution table
    :param str code: code word to create shifted substitution table
    :param message: message to be encoded
    :rtype: str
    :return: encoded message
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = list(code.upper())
    message = list(message.upper())
    nove = []
    substitution_table = code

    last_letter_index = alphabet.index(code[-1]) + 1
    for i in range(last_letter_index, len(alphabet)):
        if alphabet[i] not in substitution_table:
            substitution_table += alphabet[i]

    if len(substitution_table) < len(alphabet):
        for character in alphabet:
            if character not in substitution_table:
                substitution_table += character

    for i in message:
        for zakod, normal in zip(code, alphabet):
            if i == normal:
                nove.append(i.replace(normal, zakod))

    encoded_message = "".join(nove)

    return encoded_message


if __name__ == "__main__":
    code = "ALGORITMUS"
    message = "hello"
    encoded_message = encode_message(code, message)
    print(encoded_message)
