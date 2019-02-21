#Предполагается, что скидки в 5% и в 20% не суммируются!
film=input('Введите название фильма\n')
data=input('Выберите дату сеанса (сегодня или завтра)\n')
time=int(input('Выберите время сеанса\n'))
number=int(input('Выберите количество билетов\n'))
if data==('сегодня'):
    if number<20:
        if film==('Пятница'):
            if time==12:
                print ("Цена билетов составит", 250*number)
            elif time==16:
                print ("Цена билетов составит", 350*number)
            elif time==20:
                print ("Цена билетов составит", 350*number)
        if film==('Чемпионы'):
            if time==10:
                print ("Цена билетов составит", 250*number)
            elif time==13 or time==16:
                print ("Цена билетов составит", 350*number)
        if film==('Пернатая банда'):
            if time==10:
                print ("Цена билетов составит", 350*number)
            elif time==14 or time==18:
                print ("Цена билетов составит", 450*number)
    if number>=20:
        if film==('Пятница'):
            if time==12:
                print ("Цена билетов составит", 250*number*0.8)
            elif time==16:
                print ("Цена билетов составит", 350*number*0.8)
            elif time==20:
                print ("Цена билетов составит", 350*number*0.8)
        if film==('Чемпионы'):
            if time==10:
                print ("Цена билетов составит", 250*number*0.8)
            elif time==13 or time==16:
                print ("Цена билетов составит", 350*number*0.8)
        if film==('Пернатая банда'):
            if time==10:
                print ("Цена билетов составит", 350*number*0.8)
            elif time==14 or time==18:
                print ("Цена билетов составит", 450*number*0.8)
if data==('завтра'):
    if number<20:
        if film==('Пятница'):
            if time==12:
                print ("Цена билетов составит", 250*number*0.95)
            elif time==16:
                print ("Цена билетов составит", 350*number*0.95)
            elif time==20:
                print ("Цена билетов составит", 350*number*0.95)
        if film==('Чемпионы'):
            if time==10:
                print ("Цена билетов составит", 250*number*0.95)
            elif time==13 or time==16:
                print ("Цена билетов составит", 350*number*0.95)
        if film==('Пернатая банда'):
            if time==10:
                print ("Цена билетов составит", 350*number*0.95)
            elif time==14 or time==18:
                print ("Цена билетов составит", 450*numbe*0.95)
    if number>=20:
        if film==('Пятница'):
            if time==12:
                print ("Цена билетов составит", 250*number*0.8*0.95)
            elif time==16:
                print ("Цена билетов составит", 350*number*0.8*0.95)
            elif time==20:
                print ("Цена билетов составит", 350*number*0.8*0.95)
        if film==('Чемпионы'):
            if time==10:
                print ("Цена билетов составит", 250*number*0.8*0.95)
            elif time==13 or time==16:
                print ("Цена билетов составит", 350*number*0.8*0.95)
        if film==('Пернатая банда'):
            if time==10:
                print ("Цена билетов составит", 350*number*0.8*0.95)
            elif time==14 or time==18:
                print ("Цена билетов составит", 450*number*0.8*0.95)
