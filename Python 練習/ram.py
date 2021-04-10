

blockSize = [100, 100, 500, 600, 200, 300, 200, 600]
state = [999, -1, -1, 999,-1,-1,999,-1]
processSize = [212, 417, 112, 426]

for i in range(len(state)):
    if state[i] == int(999):
        state[i] = 0
    else:
        state[i] = 1


state_temp=[] # 計算用 0 100 100 500 0...
for i in range(len(blockSize)):
    state_temp.append(blockSize[i]*state[i])

left_spacetemp = state_temp # 儲存用


def First_fit(blockSize,state_temp,processSize):

    state_temp=[] # 計算用 0 100 100 500 0...
    for i in range(len(blockSize)):
        state_temp.append(blockSize[i]*state[i])

    left_spacetemp = state_temp # 儲存用

    address = []
    temp = []
    left_spacetemp = state_temp
    left_space = []
    blockSize_test = 0
    for i in blockSize:
        blockSize_test = blockSize_test + i

    for i in processSize:
        address_temp = 0
        # print(i)
        for x in range(len(left_spacetemp)):

            if i < left_spacetemp[x]:
                left_spacetemp[x] = left_spacetemp[x] - i
                left_space.append(left_spacetemp[x])
                
                address_temp = blockSize[x] - left_spacetemp[x] + address_temp - i
                # address_temp = address_temp + i
                break
            else:
                address_temp = address_temp + blockSize[x]

        if blockSize_test == address_temp:
            address.append("Not Allocated")
            left_space.append("Not Allocated")
            break

        address_temp = address_temp + i
        address.append(address_temp)
            
    # print(address)
    # print(left_space)  
    return address,left_space





first_address,fisrst_leftspace = First_fit(blockSize,state_temp,processSize)
print("first_address: ",first_address,"fisrst_leftspace: ",fisrst_leftspace)









