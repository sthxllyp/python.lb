import mymodule2
if __name__ == "__main__":
  list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  k = 5

  list_b = mymodule2.filter_list(list_a, k)
  print(list_b)   