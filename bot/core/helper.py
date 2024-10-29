import random

def formatst(settings):
    return settings.REF_ID if random.randint(0, 100) <= 85 and settings.REF_ID != '' else 'ZadWdla7'
