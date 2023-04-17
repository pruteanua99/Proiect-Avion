def Cached(func):
      rezultat = {}
      def wrapper(*args):
            if args in rezultat:
                  return rezultat[args]
            result = func(*args)
            rezultat[args] = result
            return result
      return wrapper
