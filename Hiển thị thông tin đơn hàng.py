#!/usr/bin/env python
# coding: utf-8

# Viết chương trình hỏi người dùng đã chi bao nhiêu tiền tại cửa hàng.
# 
# Nếu họ chi ít hơn 75$, họ sẽ không được giảm giá.
# 
# Nếu họ chi 75$ trở lên, họ sẽ được giảm giá 15$.
# 
# Nếu người dùng chi từ 100$ trở lên, họ sẽ được giảm giá 25$.
# 
# Nếu người dùng chi từ 150$ trở lên, họ sẽ được giảm giá 50$.
# Sau đó in ra tổng số tiền mà người dùng phải thanh toán.

# In[ ]:


m = float(input('Số tiền quý khách đã chi trả cho cửa hàng là : '))

if m <75:
    print('Số tiền quý khách cần trả là ', m )
elif m >75 and m<=100:
    print('Số tiền quý khách cần trả là ', m -15)
elif m>100 and m <=150:
    print('Số tiền quý khách cần trả là ', m -25)
else:
    print('Số tiền quý khách cần trả là ', m -50)

