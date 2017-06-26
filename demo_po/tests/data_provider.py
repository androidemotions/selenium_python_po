import time
from demo_po.data.customer import Customer


def current_time_millis():
    return int(round(time.time() * 1000))


test_customers = [Customer(firstname="John", lastname="Sparrow", phone="+191156233",
                           address="5th Street 15", postcode="11111", city="New York",
                           country="US", zone="NY",
                           email="john%s@gmail.com" % current_time_millis(),
                           password="******"),
                  Customer(firstname="John2", lastname="Sparrow2", phone="+191156233",
                           address="5th Street 15", postcode="11111", city="New York",
                           country="US", zone="NY",
                           email="john%s@gmail.com" % (current_time_millis()+1),
                           password="******")

                  # ...
                  ]
