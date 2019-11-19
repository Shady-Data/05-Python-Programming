# Endless recursion
def forever_recursion(times):
    annoying_message(times)

def annoying_message(times):
    if times > 0:
        print('Nudge Nudge, Wink Wink, Say No More Say No More')
        annoying_message(times -1)

forever_recursion(995)