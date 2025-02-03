vouvels=['a','e','i','o','u']
def translate(text):
    result =""
    for letter in text:
        if letter in 'AEIOUaeiou':
            result=result+"z"
        else:
            result=result+letter
    return result

print(translate(input("Input a text "))) 