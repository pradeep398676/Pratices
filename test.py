store1 = [
    { "item_name": "Laptop", "quantity": 5, "price": 1300, "store_name": "StoreA" },
    { "item_name": "Smartphone", "quantity": 10, "price": 700, "store_name": "StoreA" },
    { "item_name": "Headphones", "quantity": 7, "price": 100, "store_name": "StoreA" }
]

store2 = [
    { "item_name": "Laptop", "quantity": 11, "price":1200, "store_name": "StoreB" },
    { "item_name": "Smartphone", "quantity": 8, "price": 900, "store_name": "StoreB" },
    { "item_name": "Smartwatch", "quantity": 5, "price": 200, "store_name": "StoreB" }
]

# more sale from store store1 and store2 in terms of quantity
# More price from store store1 and store2 in terms of price

def home(**kwargs):
    store = kwargs
    newdict = {}

    for i,j  in store.items():
        max_quantity = 0
        max_orice = 0
        for k in j:
            # print(k.get('item_name'),k.get('quantity'),k.get('price'))
            l=[]
            if newdict.get(k.get('item_name')):
                if newdict.get(k.get('item_name'))[0] < k.get('quantity'):
                    newdict.get(k.get('item_name'))[0] = ('Quantity High',k.get('quantity'),k.get('store_name'))
                else:
                    newdict.get(k.get('item_name'))[0] = ('Quantity High', newdict.get(
                        k.get('item_name'))[0], newdict.get(k.get('item_name'))[2])
              
                if newdict.get(k.get('item_name'))[1] < k.get('price'):
                    newdict.get(k.get('item_name'))[1] = ('Price High', k.get('price'), k.get('store_name'))
                else:
                    newdict.get(k.get('item_name'))[1] = ('Price High', newdict.get(
                        k.get('item_name'))[1], newdict.get(k.get('item_name'))[2])

                
            else:
                # print(k['item_name'])
                l.append(k['quantity'])
                l.append(k['price'])
                l.append(k['store_name'])
                newdict[k.get('item_name')] = l
                
    return newdict

k = home(store1=store1,store2=store2)

# print('final_result',k)
for final_item, item_detail in k.items():
    if type(item_detail[0]) != int:
        item_detail.pop()
        k[final_item]=item_detail
    else:
        k[final_item] = item_detail
print('final_result',k)
     
home(store1=store1,store2=store2)



def home(**kwargs):
    newdict = {}

    for store_items in kwargs.values():
        for item in store_items:
            item_name = item["item_name"]
            quantity = item["quantity"]
            price = item["price"]
            store_name = item["store_name"]
            
            if item_name not in newdict:
                # Initialize with quantity and price info
                newdict[item_name] = {
                    'max_quantity': (quantity, store_name),
                    'max_price': (price, store_name)
                }
            else:
                # Update max quantity if higher
                if quantity > newdict[item_name]['max_quantity'][0]:
                    newdict[item_name]['max_quantity'] = (quantity, store_name)
                # Update max price if higher
                if price > newdict[item_name]['max_price'][0]:
                    newdict[item_name]['max_price'] = (price, store_name)

    # Format the result to return only the relevant data
    result = {}
    for item_name, details in newdict.items():
        result[item_name] = {
            'max_quantity': details['max_quantity'],
            'max_price': details['max_price']
        }

    return result


store1 = [
    { "item_name": "Laptop", "quantity": 5, "price": 1300, "store_name": "StoreA" },
    { "item_name": "Smartphone", "quantity": 10, "price": 700, "store_name": "StoreA" },
    { "item_name": "Headphones", "quantity": 7, "price": 100, "store_name": "StoreA" }
]

store2 = [
    { "item_name": "Laptop", "quantity": 11, "price": 1200, "store_name": "StoreB" },
    { "item_name": "Smartphone", "quantity": 8, "price": 900, "store_name": "StoreB" },
    { "item_name": "Smartwatch", "quantity": 5, "price": 200, "store_name": "StoreB" }
]

k = home(store1=store1, store2=store2)
print('final_result:', k)

        
        
#===============================================================================================

class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")
        super().speak()


class Cat(Animal):
    def speak(self):
        print("The cat meows")

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Demonstrating polymorphism
dog.speak()  # Output: The dog barks
cat.speak()  # Output: The cat meows
