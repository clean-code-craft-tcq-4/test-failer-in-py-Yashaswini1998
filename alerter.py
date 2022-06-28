alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if celcius >= 100:
        return 200
    else:
        return 500

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1
    return alert_failure_count

alert_in_celcius(400.5)
alert_in_celcius(303.6)
alert_in_celcius(212)
alert_in_celcius(3.6)
alert_in_celcius(5.6)
assert (alert_failure_count == 2)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
