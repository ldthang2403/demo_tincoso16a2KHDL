# var1 is in the global namespace
var1 = 5
def some_func():
# var2 is in the local namespace
   var2 = 6
   print("giá trị biến var2 trong local name hàm some_func là : ",var2)
   def some_inner_func():
#var3 is in the nested local namespace #
      var3 = 7
      print("Giá trị biến var3 trong nested local namespace là: ", var3)
   some_inner_func()
print("giá trị biến var trong không gian global namespace là: ", var1)

some_func()
