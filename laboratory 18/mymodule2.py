def filter_list(list_a, k):

  list_b = []
  for element in list_a:
    if element != k:
      list_b.append(element)

  return list_b