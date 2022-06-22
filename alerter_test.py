from alerter import *
from alerter import alert_failure_count

alert_in_celcius(400.5)
alert_in_celcius(303.6)
assert (alert_failure_count == 2)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')