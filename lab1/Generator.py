import random

class Generator:
   def __init__(self, n):
      self.n=n

   def generate_matrix(self):
      if self.n < 2 or not isinstance(self.n, int):
         # Assuming self.n should be an integer greater than or equal to 2
         print("Cannot be less than 2 or float")
         return

      data = [[]]

      def get_random_number():
         return format(random.uniform(0, 100), '.5f')


      for i in range(self.n):
         data[0].append([float(get_random_number()) for j in range(self.n + 1)])

      data += [1 * 10 ** -(random.randint(1, 10))]

      return data
