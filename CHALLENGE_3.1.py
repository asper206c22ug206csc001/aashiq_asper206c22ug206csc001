'''Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found. '''


def linear_search_product(product_list, target_product):
  indices = []
  for i in range(len(product_list)):
    if product_list[i] == target_product:
      indices.append(i)
  return indices


products = ['Apple', 'Banana', 'Orange', 'Apple', 'Grapes', 'Banana']
target_product = 'Apple'
result_indices = linear_search_product(products, target_product)
print("Indices of", target_product, "in the product list:", result_indices)
