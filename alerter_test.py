from alerter import *
from alerter import alert_failure_count

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if celcius >= 100:
        return 200
    else:
        return 500
        
alert_in_celcius(400.5)
alert_in_celcius(303.6)
assert (alert_failure_count == 2)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')