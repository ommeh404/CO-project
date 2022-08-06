


import math
print("**************************************** Type 1 *********************************************")
print()
Dict = {'Bit addressable memory' : 1 ,'Nibble addressable memory' : 4, 'Byte addressable memory' : 8} 

#Type1 

inst_length=int(input("Enter your Instruction Length: "))
reg_length=int(input("Enter Register Length: "))

#Initial input
print()
print("Enter your initial input:")
inp_mem=input("Input Memory Space: ")

mem_unit = {"kb" : 2**10 , "mb" : 2**20 , "gb" : 2**30 , "kB" : 2**18 , "mB" : 2**28 , "gB" : 2**38}
inp_mem=inp_mem.split()
if(inp_mem[1]=='kb'):
    bits=int(inp_mem[0])*(2**10)                      
    x = math.log(bits) / math.log(2)                  

elif(inp_mem[1]=='mb'):
    bits=int(inp_mem[0])*(2**10)                      
    x = math.log(bits) / math.log(2) 

if(inp_mem[1]=='gb'):
    bits=int(inp_mem[0])*(2**10)                      
    x = math.log(bits) / math.log(2) 

if(inp_mem[1]=='gB'):
    bits=int(inp_mem[0])*(2**10)                      
    x = math.log(bits) / math.log(2)     

if(inp_mem[1]=='kB'):
    bits=int(inp_mem[0])*(2**10)                      
    x = math.log(bits) / math.log(2) 

if(inp_mem[1]=='mB'):
    bits=int(inp_mem[0])*(2**10)                      
    x = math.log(bits) / math.log(2)     
#print(x)
print()
print("1.Bit addressable memory")
print("2.Byte addressable memory")
print("3.Nibble addressable memory")
print("4.Word addressable memory ")
print()
address_type=input("Enter Address Type option: ")
if(address_type=="2"):
    address_pins=2**x/Dict["Byte addressable memory"]                        
    y=math.log(address_pins)/math.log(2)          
elif(address_type=="3"):
    address_pins=2**x/Dict["Nibble addressable memory"] 
    y=math.log(address_pins)/math.log(2)

elif(address_type=="1"):
    address_pins=2**x/2**1
    y=math.log(address_pins)/math.log(2)

elif(address_type=="4"):
    address_pins=2**x/2**4
    y=math.log(address_pins)/math.log(2)

#print(y)


print()
print("The minimum bits needed for architecture: ", y)
print("The number of bits need by opcode: ",inst_length - y - reg_length)
print("The number of filler bits in Instruction type 2: ",inst_length - (inst_length - y - reg_length) - reg_length)
print("Maximum numbers of instructions this ISA can support: ",2**(inst_length-y-reg_length))
print("Maximum number of registers this ISA can support: ",2**reg_length)
print()

print("Enter current input: ")
bitCPU=int(input("Enter the number bits in CPU: "))
print()
print("1.Bit addressable memory")
print("2.Byte addressable memory")
print("3.Nibble addressable memory")
print("4.Word addressable memory: ")
print()
address_type2=input("Enter the enhanced address type option: ")
if(address_type2=="4"):
    g=math.log(bitCPU)/math.log(2)
    print()
    new_pins=2**x/2**g                  

elif(address_type2=='2'):
    print()
    new_pins=2**x/Dict["Byte addressable memory"]

elif(address_type2=='1'):
    print()
    new_pins=2**x/2

elif(address_type2=='3'):
    print()
    new_pins=2**x/Dict["Nibble addressable memory"]

z=math.log(new_pins)/math.log(2)                       
output=y-z                                             
if(y>z):
    print("Number of pins saved: -",int(output))

else:
    print("Number of pins required: +",int(output))

print()
print("*************************************** Type 2 ************************************************")
print()
bitCPU = input("Enter the number bits in CPU: ") 
bitCPU = bitCPU.split()
address_pins = input("Enter the number of address pins: ") 
address_pins = address_pins.split()
print()
print("1.Bit addressable memory")
print("2.Byte addressable memory")
print("3.Nibble addressable memory")
print("4.Word addressable memory")
print()
address_memory = int(input("Enter the type of addressable memory: "))

number_address = 2**int(address_pins[0])  



if(address_memory == 1):
    a = number_address/8             
    b = a/1024                       
    c = b/1024                         
    d = c/1024                       

    print()
    final_output = Dict["Bit addressable memory"]*d
    print("The size of main memory is: ",int(final_output),'GB')  

elif(address_memory == 2):
    a = number_address/8             
    b = a/1024                       
    c = b/1024                         
    d = c/1024                       

    print()
    final_output = Dict["Byte addressable memory"]*d
    print("The size of main memory is: ",int(final_output),'GB')  

elif(address_memory == 3):
    a = number_address/8             
    b = a/1024                       
    c = b/1024                         
    d = c/1024                       

    print()
    final_output = Dict["Nibble addressable memory"]*d
    print("The size of main memory is: ",int(final_output),'GB')   

elif(address_memory == 4):
    a = number_address/8             
    b = a/1024                       
    c = b/1024                         
    d = c/1024                       

    print()
    final_output = d*int(bitCPU[0])
    print("The size of main memory is: ",int(final_output),"GB")
