# var is in the global namespace
var = 5
def some_func():
# var is in the local namespace
   var = 6
   print("giá trị biến var2 trong local hàm some_func là : ",var)
   def some_inner_func():
#var3 is in the nested local namespace #
     var = 7
     print("Giá trị biến var3 trong nested local namespace là: ", var)
   some_inner_func()
print("giá tri biến var trong không gian global namespace là: ", var)
some_func()
print("Giá trị biến var sau khi gọi hàm some_func() là ", var)