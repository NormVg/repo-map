Contents:
a = {
    "seq":seq,
    "date" : date,
    "main-meter" : mm,
    "motor" : motor,
    "slave" : slave,
    "bill-rs" : bill,
    "bill-ground" : ground,
    "bill-first" : first,
}
db.insert_one(a)
a =  db.find({})
b = []
for i in a:
    b.insert(i['seq'],i)
b.reverse()
return b
a = all_data()
a.reverse()
b = len(a)
c = a[b-1]
mm = float(mm) - float(c['main-meter'])
motor = float(motor) - float(c['motor'])
slave = float(slave) - float(c['slave'])
each_motor = motor/2
one = (mm - slave) - each_motor
# two =  slave - each_motor
ground = int((one/mm)*bill)
first = bill - ground # float((two/mm)*bill)
return b,ground,first
d = datetime.now()
return f"{d.day}/{d.month}/{d.year}"
