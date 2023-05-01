def Cached(func):
      rezultat = {}
      def wrapper(*args):
            if args in rezultat:
                  return rezultat[args]
            result = func(*args)
            rezultat[args] = result
            return result
      return wrapper


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
