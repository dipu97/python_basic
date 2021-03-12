user={'DIPU':[35000,'Dhaka','01771974774'],'SAGOR':[55000,'Chandigarh','7297454876']}
print(user)
keys=user.keys()
for eachkey in keys:
    print('The User is:',eachkey,'his/her info are:')
    for eachinfo in user[eachkey]:
        print(eachinfo)