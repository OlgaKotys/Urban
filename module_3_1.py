calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return(len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [item.lower() for item in list_to_search]

print(string_info('University'))
print(string_info('Home'))
print(string_info('Incomprehensibility'))
print(is_contains('Forest', ['rest', 'FoR', 'foREST']))
print(is_contains('apartment', ['moment', 'apart']))
print(calls)