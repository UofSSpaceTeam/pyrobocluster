
from robocluster import SerialDevice, Device
import robocluster.util; robocluster.util.DEBUG = True

driver = SerialDevice('/dev/ttyACM0', 'rover')

@driver.every('1s')
async def print_name():
    print(driver.name)

tester = Device('tester', 'rover')

@tester.every('1s')
async def blarg():
    await tester.publish('blarg', 27)


try:
    driver.start()
    tester.start()
    driver.wait()
    tester.wait()
except KeyboardInterrupt:
    driver.stop()
    tester.stop()

