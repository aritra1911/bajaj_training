from pet_model import Pet, db

db.create_all()

sib = Pet('Siberian Cat', 'Dolly', 'Kapil', 5)
hm = Pet('Himalyan Cat', 'Molly', 'Rahul', 3)
rs = Pet('Russian Cat', 'Jelly', 'Pradan', 4)
db.session.add_all((sib, hm, rs))
db.session.commit()

print(sib)
print(hm)
print(rs)
print(sib.id)
print(hm.id)
print(rs.id)