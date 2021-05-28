import platform

bit=platform.architecture()[0]

if bit=="64bit":

    import jutt

    jutt.reg()

elif bit=="32bit":

    import jatti

    jatti.reg()
