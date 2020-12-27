from sqlalchemy.orm import relationship

import base
from sqlalchemy import Column, Integer, String, Date, ForeignKey

class Person(base.Base):
    __tablename__ = 'Person'
    id_person = Column('id_person', Integer,  primary_key=True)
    numb_person = Column('numb_person', Text) 
    name_person = Column('name_person', Text) 
    adress_person = Column('adress_person', Text)
    order = relationship('Order') 

    def __repr__(self):
        return "<Person(id_peson='{}', numb_person='{}', name_person='{}', adress_person='{}')>"\
            .format(self.id_person, self.numb_person, self.name_person, self.adress_person)

class Order(base.Base):
    __tablename__ = 'Order'
    id_order = Column('id_order', Integer,  primary_key=True)
    id_person = Column('id_person', Integer, ForeignKey('Person.id_person')) 
    date_order = Column('date_order', Text) 
    order/dish = relationship('Order/Dish') 

    def __repr__(self):
        return "<Order(id_order='{}', id_person='{}', date_order='{}')>"\
            .format(self.id_order, self.id_person, 	self.date_order)

class License(base.Base):
    __tablename__ = 'License'
    id_license = Column('id_license', Integer,  primary_key=True)
    id_restaurant = Column('id_restaurant', Integer, ForeignKey('Restaurant.id_restaurant')) 
    num_license = Column('num_license', Text) 

    def __repr__(self):
        return "<License(id_license='{}', id_restaurant='{}',num_license='{}')>"\
            .format(self.id_license, self.id_restaurant, self.num_license)

class Restaurant(base.Base):
    __tablename__ = 'Restaurant'
    id_restaurant = Column('id_restaurant ', Integer,  primary_key=True)
    title_rest = Column('title_rest’, Text) 
    numb_rest = Column('numb_rest', Text)              
    adress_rest = Column('adress_rest', Text)                		
    license = relationship('License')                         	
    dish = relationship('Dish')

    def __repr__(self):
        return "<Restaurant(id_restaurant='{}', title_rest='{}', numb_rest='{}', adress_rest='{}')>"\
            .format(self.id_restaurant, self.title_rest, self.numb_rest, self.adress_rest)

class Dish(base.Base):
    __tablename__ = 'Dish'
    id_dish = Column('id_dish', Integer,  primary_key=True)
    amount = Column('amount’, Text) 
    name_dish = Column('name_dish', Text)                          
    id_restaurant = Column('id_restaurant', Integer, ForeignKey('Restaurant.id_restaurant')) 


    def __repr__(self):
        return "<Dish(id_dish='{}', amount='{}', name_dish='{}', id_restaurant='{}')>"\
            .format(self.id_dish, self.amount, self.name_dish, self.id_restaurant)

class Order/Dish(base.Base):
    __tablename__ = 'Order/Dish'
    id_dish = Column('id_dish', Integer,  ForeignKey('Dish.id_dish'))
    id_order = Column('id_order', Integer,  ForeignKey('Order.id_order')) 
    

    def __repr__(self):
        return "<Order/Dish(id_dish='{}', id_order='{}')>"\
            .format(self.id_dish, self.id_order)

