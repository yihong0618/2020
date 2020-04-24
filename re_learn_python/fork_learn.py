import os

a = 2
pid = os.fork()
pid = os.fork()
print(a, pid, os.getpid())
# import os
# import time

# for i in range(2):
#     print("I'm about to be a dad!")
#     time.sleep(5)
#     pid = os.fork()
#     if pid == 0:
#         print("I'm {}, a newborn that knows to write to the terminal!".format(os.getpid()))
#     else:
#         print("I'm the dad of {}, and he knows to use the terminal!".format(pid))
#         os.waitpid(pid, 0)
