#classobj
class laptop:
    price=0
    processor=""
    ram=""

mac=laptop()
windows=laptop()

mac.price=90000
mac.processor="M3.M4.M5"
mac.ram="16.32"

windows.price=60000
windows.processor="Intel.AMD"
windows.ram="16.32"

print(mac.price)
print(windows.price)

print(mac.processor)
print(windows.processor)