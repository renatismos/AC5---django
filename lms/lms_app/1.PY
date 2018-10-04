class MinhaExcessao(Exception): pass
def func():
    try:
        print(1)
        raise MinhaExcessao('erro')
        print(2)
    except MinhaExcessao:
        print(3)
    except Exception:
        print (4)
    else:
        print(5)
    finally:
        print(6)

func()